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

---

# A2: TEC Heating and Cooling Analysis

## 1. Part 4: Combined Graph and Fits

![Heating and cooling temperature versus signed PWM with linear fits](Part%204/temperature_vs_signed_pwm.png)

The graph combines the steady-state heating and cooling measurements using signed PWM, with heating positive and cooling negative. The heating fit used $u=0$ to $30$ PWM, while the cooling fit used $u=0$ to $-130$ PWM. The heating data are close to linear over the measured range. The cooling data are also approximately linear, although there is mild curvature near the strongest cooling point; therefore, the reported cooling slope is an overall fit across the measured range rather than a strictly local slope.

## 2. Part 5.1: Measured Slopes

The fitted heating and cooling-slope magnitudes are

$$
m_h\approx0.49\ \frac{^\circ\mathrm C}{\text{PWM count}},
\qquad
m_c\approx0.20\ \frac{^\circ\mathrm C}{\text{PWM count}}.
$$

Their measured ratio is

$$
r=\frac{m_h}{m_c}
=\frac{0.49}{0.20}
\approx2.45.
$$

Thus, one additional heating PWM count changes the steady temperature about 2.45 times as much as one additional cooling PWM count in magnitude. The visible cooling curvature makes the fitted value somewhat dependent on the selected range, but the single fit captures the main heating-cooling asymmetry.

## 3. Part 5.2: PWM and the Slope-Ratio Model

For PWM duty cycle $D$, the current equals $I$ during the on-time $D\tau$ and zero during the remainder of a period $\tau$. Therefore,

$$
\langle I\rangle
=\frac{1}{\tau}\int_0^\tau I(t)\,dt
=\frac{I(D\tau)}{\tau}
=DI,
$$

and

$$
\langle I^2\rangle
=\frac{1}{\tau}\int_0^\tau I^2(t)\,dt
=\frac{I^2(D\tau)}{\tau}
=DI^2.
$$

Hence, both the Peltier contribution and Joule contribution scale linearly with duty cycle for a fixed on-state current. Let $\dot Q_P$ and $\dot Q_J$ be their full-duty object-face magnitudes, and let $G$ be the passive thermal conductance to the surroundings. At steady state,

$$
G(T_h-T_0)=D(\dot Q_P+\dot Q_J)
$$

for heating, while the cooling temperature-change magnitude obeys

$$
G|T_c-T_0|=D(\dot Q_P-\dot Q_J).
$$

Since $D=|u|/255$, the corresponding slope magnitudes are

$$
m_h=\frac{\dot Q_P+\dot Q_J}{255G},
\qquad
m_c=\frac{\dot Q_P-\dot Q_J}{255G}.
$$

Their ratio is therefore

$$
r=\frac{m_h}{m_c}
=\frac{\dot Q_P+\dot Q_J}{\dot Q_P-\dot Q_J}.
$$

Writing $x=\dot Q_J/\dot Q_P$ gives $r=(1+x)/(1-x)$. Solving,

$$
r-rx=1+x,
\qquad
r-1=x(r+1),
$$

so

$$
\frac{\dot Q_J}{\dot Q_P}=\frac{r-1}{r+1}.
$$

Using the measured ratio,

$$
\frac{\dot Q_J}{\dot Q_P}
=\frac{2.45-1}{2.45+1}
=\frac{1.45}{3.45}
\approx0.42.
$$

Thus, the object-face Joule heating is approximately 42% of the Peltier heat-transfer magnitude in this model.

## 4. Part 5.3: Laird Datasheet Calculation

The values come from the **Specifications** table on page 3 of the [Laird CP14-127-045-L1-W4.5 datasheet](https://lairdthermal.com/datasheets/datasheet-CP14-127-045-L1-W4.5.pdf), using the column for a hot-side temperature of $27^\circ\mathrm C$.

- $R_M=1.50\ \Omega$ is the module's effective electrical resistance at the stated $27^\circ\mathrm C$ hot-side condition.
- $I_{\max}=8.6\ \mathrm A$ is the maximum rated current; the table identifies it as the current at $\Delta T_{\max}$.
- $Q_{c,\max}=71.3\ \mathrm W$ is the maximum cold-side heat pumping at $\Delta T=0$.
- $\Delta T_{\max}=70.5^\circ\mathrm C$ is the maximum face-to-face temperature difference at zero cold-side heat load, $Q_c=0$.

The symmetric model assigns half of the total Joule heating to the object face:

$$
\dot Q_{J,\max}
=\frac12 I_{\max}^2R_M
=\frac12(8.6\ \mathrm A)^2(1.50\ \Omega)
=55.47\ \mathrm W.
$$

At $\Delta T=0$, the measured cold-side cooling equals the Peltier pumping minus object-face Joule heating, so

$$
\dot Q_{P,\max}
=Q_{c,\max}+\dot Q_{J,\max}
=71.3+55.47
=126.77\ \mathrm W.
$$

The maximum-current heating-to-cooling slope-ratio prediction is then

$$
r_{\mathrm{Laird},\max}
=\frac{\dot Q_{P,\max}+\dot Q_{J,\max}}
{\dot Q_{P,\max}-\dot Q_{J,\max}}
=\frac{126.77+55.47}{126.77-55.47}
=\frac{182.24}{71.30}
\approx2.56.
$$

## 5. Part 5.4: Compare the Ratios

The measured ratio $r\approx2.45$ is about 4% below the datasheet-model prediction $r_{\mathrm{Laird},\max}\approx2.56$. Exact agreement is not expected because the datasheet values describe a specified maximum-current condition, while the apparatus has different electrical and thermal conditions. In particular, $D=1$ only means that the H-bridge is continuously on; it does not guarantee $I=I_{\max}$. The actual current depends on the 12 V power supply and its current limit, H-bridge and wiring voltage drops, and the temperature-dependent TEC resistance, whereas the datasheet maximum-current point uses $V_{\max}=13.9\ \mathrm V$ with the hot side at $27^\circ\mathrm C$.

The experiment also uses PWM instead of ideal steady DC, operates at finite temperature differences, and includes passive heat paths through the supports, leads, and surrounding air. Material properties vary with temperature, and fitting a slightly curved branch with one straight line also changes the measured ratio. These effects make the modest discrepancy reasonable.

## 6. Part 5.4: Passive Conduction

When the object is hotter than room temperature, passive heat flows from the object to the room and opposes further heating. When the object is colder than room temperature, passive heat flows from the room into the object and opposes further cooling. Approximately symmetric passive conduction therefore reduces the temperature displacement in both directions. However, because it reverses direction with the temperature difference and acts similarly in magnitude for comparable positive and negative differences, it cannot by itself explain unequal heating and cooling slope magnitudes. The primary directional asymmetry in the model comes from Joule heating: it adds to the Peltier contribution during heating but subtracts from the useful Peltier contribution during cooling.
