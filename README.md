# Kadener-Wijnaendts-Module4

# Part 1

Record the Arduino sketch filename-did, Python filename-did, 
serial port - dev/cu.usbmodem101
power-supply voltage - 12V
and power-supply current limit in your module notes -  10 Amps

Steady State for 10C cooling - 135 pwm
Steady State for 45C heating - 30 pwm

# Part 2: PWM Values

| Direction | Temperature at maximum useful PWM | Maximum useful PWM | 0% | 25% | 50% | 75% | 100% |
|---|---:|---:|---:|---:|---:|---:|---:|
| Heat | 45 C | 30 | 0 | 8 | 15 | 23 | 30 |
| Cool | 10 C | 130 | 0 | 33 | 65 | 98 | 130 |

# Part 3

 PWM Heating and Cooling Estimates Table

| PWM | Mode | StartTime | Temp | EndTime | EndTemp |
|---|---|---:|---:|---:|---:|
| 0pwm | Heating | 27s | 28C | 100s | 34C |
| 8pwm | Heating | 0s | 34C | 125s | 39C |
| 15pwm | Heating | 0s | 23C | 165s | 42C |
| 23pwm | Heating | 0s | 28C | 130s | 46C |
| 30pwm | Heating | 0s | 33C | 125s | 50C |
| 0pwm | Cooling | 0s | 51C | 200s | 37C |
| 33pwm | Cooling | 0s | 38C | 185s | 30.5C |
| 65pwm | Cooling | 0s | 30C | 140s | 24.5C |
| 98pwm | Cooling | 0s | 47C | 207s | 18C |
| 130pwm | Cooling | 0s | 33C | 290s | 10.4C |

# Part 4: Temperature vs. Signed PWM

![Baseline-corrected temperature versus signed PWM](Part%204/temperature_vs_signed_pwm.png)

The following table uses the corrected room-temperature baseline of **22.00 °C at 0 PWM**. A constant offset was applied to each complete heating/cooling series from `temperature_measurements.csv`; the raw data were not overwritten. Because a constant vertical offset does not change $\Delta T/\Delta u$, the fitted slopes remain the same.

| Direction | PWM (counts) | Steady-state temperature (°C) |
|---|---:|---:|
| Heating | 0 | 22.00 |
| Heating | 8 | 25.60 |
| Heating | 15 | 29.29 |
| Heating | 23 | 32.49 |
| Heating | 30 | 36.85 |
| Cooling | 0 | 22.00 |
| Cooling | -33 | 17.06 |
| Cooling | -65 | 11.14 |
| Cooling | -98 | 4.54 |
| Cooling | -130 | -3.54 |

Using a straight-line fit over the corrected data, the temperature susceptibility is **0.4872 °C per PWM count for heating** and **0.1957 °C per PWM count for cooling** (approximately **0.49** and **0.20 °C per PWM count**, respectively, with cooling plotted on the negative-PWM side). These are unchanged because only the temperature baseline was shifted.
