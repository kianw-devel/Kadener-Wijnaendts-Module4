# Kadener-Wijnaendts-Module4

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

The measured ratio $r\approx2.45$ is around 4% lower than the result obtained from the datasheet values $r_{\mathrm{Laird},\max}\approx2.56$. It is not expected for these values to agree exactly ebcasue the datasheet describes a specific max-current condition, while the measured ratio comes from the apparatus which has different thermal and electrical conditions. $D=1$ only means that the H-bridge is on continously. It does not guarantee that $I=I_{\max}$ since the actual current depends on the 12V power supply's current limit, H-bridge wiring and voltage drops, as well as the temp-dependent TEC resistance, while the datasheet max-current point uses $V_{\max}=13.9\ \mathrm V$ with the hot side at $27^\circ\mathrm C$.

Additionally, the experiment also use PWM rather than the ideal steady DC, operates at finite temperature differences, and has passive heat paths through the suports, leads, and air. Material properties change based on the temperature. These factors make such a small discrepancy reasonable.

## 6. Part 5.4: Passive Conduction

When the temperature of the object is warmer than the ambient temperature of the room, passive heat flow goes from the object to the room, opposing further heating. When the object's temperature is colder than the ambient temperature, passive heat flow goes from the room into the object and opposes further cooling. Symmetric passive conduction therefore reduces the temperature displacement in both directions. Because it reverses direction with the temperature difference and acts similarly in magnitude for comparable positive and negative differences, it can't explain unequal heating and cooling slope magnitudes. The directional asymmetry in the model comes from Joule heating. It adds to the Peltier contribution during heating and subtracts from the useful Peltier contribution during the cooling.