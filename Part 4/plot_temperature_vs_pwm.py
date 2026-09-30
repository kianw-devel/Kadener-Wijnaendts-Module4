import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "temperature_measurements.csv"
OUTPUT_PATH = Path(__file__).resolve().parent / "temperature_vs_signed_pwm.png"
CORRECTED_AMBIENT_C = 22.0

spans = {}
current_key = None
current_temperatures = []
previous_time = None

with CSV_PATH.open(newline="") as csv_file:
    for row in csv.DictReader(csv_file):
        key = (int(row["heat_cool"]), int(row["pwm"]))
        time_seconds = float(row["time_s"])
        if key != current_key or (
            previous_time is not None and time_seconds < previous_time
        ):
            if current_key is not None:
                spans.setdefault(current_key, []).append(current_temperatures)
            current_temperatures = []
        current_key = key
        previous_time = time_seconds
        current_temperatures.append(float(row["temperature_C"]))

if current_key is not None:
    spans.setdefault(current_key, []).append(current_temperatures)

series = []
for name, mode, pwm_values, sign, color, marker in (
    ("Heating", 1, (0, 8, 15, 23, 30), 1, "#c62828", "o"),
    ("Cooling", 0, (0, 33, 65, 98, 130), -1, "#1565c0", "s"),
):
    points = []
    for pwm in pwm_values:
        candidates = spans.get((mode, pwm), [])
        if not candidates:
            raise ValueError(f"No measurements found for {name.lower()} PWM {pwm}")
        temperatures = max(candidates, key=len)
        if len(temperatures) < 10:
            raise ValueError(f"Too few repeated samples for {name.lower()} PWM {pwm}")
        steady_temperature = sum(temperatures[-10:]) / 10
        points.append((sign * pwm, steady_temperature))

    # Correct the temperature baseline without modifying the raw measurements.
    # Each branch used a slightly different measured zero-PWM temperature, so
    # shift the whole branch by one constant offset. This places PWM = 0 at the
    # corrected 22 C ambient while preserving every temperature difference and
    # therefore preserving the fitted susceptibility in C/PWM count.
    measured_zero_pwm = next(
        temperature for signed_pwm, temperature in points if signed_pwm == 0
    )
    temperature_offset = CORRECTED_AMBIENT_C - measured_zero_pwm
    points = [
        (signed_pwm, temperature + temperature_offset)
        for signed_pwm, temperature in points
    ]

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)
    slope = sum(
        (x - x_mean) * (y - y_mean) for x, y in points
    ) / sum((x - x_mean) ** 2 for x in x_values)
    intercept = y_mean - slope * x_mean
    series.append((name, points, slope, intercept, color, marker))

figure, axes = plt.subplots(figsize=(8, 5.2), constrained_layout=True)
for name, points, slope, intercept, color, marker in series:
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    axes.plot(x_values, y_values, color=color, alpha=0.45, linewidth=1.5)
    axes.scatter(
        x_values,
        y_values,
        color=color,
        marker=marker,
        edgecolor="white",
        linewidth=0.8,
        s=64,
        label=name,
        zorder=3,
    )
    fit_x = [min(x_values), max(x_values)]
    axes.plot(
        fit_x,
        [slope * x + intercept for x in fit_x],
        color=color,
        linestyle="--",
        linewidth=1.4,
        label=f"{name} linear fit ({slope:.2f} °C/count)",
    )

axes.set_title("Baseline-Corrected Temperature vs. Signed PWM")
axes.set_xlabel("Signed PWM (counts; cooling is negative)")
axes.set_ylabel("Steady-state temperature (°C)")
axes.grid(True, color="#d9dee5", linewidth=0.8)
axes.set_axisbelow(True)
axes.legend(frameon=False)
figure.savefig(OUTPUT_PATH, dpi=180)

for name, points, slope, _, _, _ in series:
    print(f"{name} fit slope: {slope:.4f} °C per PWM count")
    print(f"{name} points: {[(x, round(y, 2)) for x, y in points]}")
print(f"Corrected zero-PWM temperature: {CORRECTED_AMBIENT_C:.1f} °C")
print(f"Saved plot: {OUTPUT_PATH}")
