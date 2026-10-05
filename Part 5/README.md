# Part 5: Guided Heating/Cooling Energy-Balance Analysis

## 1. Measure the Two Slopes

From the approximately linear region of your graph, determine

$$
 m_h = \frac{dT_h}{du}, \qquad m_c = \frac{dT_c}{du}, \qquad r = \frac{m_h}{m_c}.
$$

Using the data from Part 4:

- $m_h \approx 0.49\ \text{°C per PWM count}$
- $m_c \approx 0.20\ \text{°C per PWM count}$
- $r = \frac{m_h}{m_c} \approx \frac{0.49}{0.20} \approx 2.45$

### Fit ranges used

- Heating fit: approximately $u = 0$ to $30$ PWM
- Cooling fit: approximately $u = 0$ to $-130$ PWM (or 0 to 130 in magnitude)

Report both slopes with units of °C per PWM count. State the PWM range used for each fit and note any visible curvature.

### Notes

- The heating data is close to linear over the measured range.
- The cooling data is also approximately linear, with mild curvature at the strongest cooling end.
- The measured slopes are reported in °C per PWM count.

---

## 2. Use Steady-State Energy Balance

At steady state,

$$
G(T-T_0)=\dot Q_{\mathrm{TEC}}.
$$

For PWM control, the current is $I$ during a fraction $D$ of the cycle and $0$ during the rest, so

$$
\langle I \rangle = \frac{1}{\tau}\int_0^\tau I(t)\,dt
= \frac{1}{\tau}(I\,D\tau)=DI,
$$

and

$$
\langle I^2 \rangle = \frac{1}{\tau}\int_0^\tau I^2(t)\,dt
= \frac{1}{\tau}(I^2D\tau)=DI^2.
$$

This is the key point: $\langle I^2 \rangle \neq \langle I \rangle^2$ in general. The Peltier term depends on the mean current, while the Joule term depends on the mean of the squared current. With fixed on-state current, both terms scale linearly with duty cycle $D$, so the temperature-vs-PWM relation stays approximately linear. If we incorrectly used $\langle I^2 \rangle=\langle I \rangle^2=D^2I^2$, the Joule term would become quadratic in duty cycle and the susceptibility would change with $D$.

The PWM-control prediction is therefore consistent with the approximately linear temperature-versus-PWM relationship measured in Part 4, with only a small amount of curvature visible at the most extreme cooling points.

The heating and cooling branches are then

$$
\dot Q_{\mathrm{TEC},h}=d(\dot Q_P+\dot Q_J),
\qquad
\dot Q_{\mathrm{TEC},c}=d(\dot Q_P-\dot Q_J),
$$

with $d=u/255$. Substituting into the steady-state balance and differentiating gives

$$
\frac{dT_h}{dd}=\frac{\dot Q_P+\dot Q_J}{G},
\qquad
\frac{dT_c}{dd}=\frac{\dot Q_P-\dot Q_J}{G}.
$$

Because $d=u/255$, the measured slopes with respect to signed PWM differ from the intrinsic slopes by the same constant factor, so

$$
 r=\frac{m_h}{m_c}=\frac{\dot Q_P+\dot Q_J}{\dot Q_P-\dot Q_J}.
$$

Solving for the heat-rate ratio,

$$
\frac{\dot Q_J}{\dot Q_P}=\frac{r-1}{r+1}.
$$

Using the measured value $r\approx 2.45$,

$$
\frac{\dot Q_J}{\dot Q_P}\approx \frac{2.45-1}{2.45+1}=\frac{1.45}{3.45}\approx 0.42.
$$

So the Joule heating is about 42% of the Peltier heating. This matches the near-linear Part 4 graph, with only mild curvature at the strongest cooling end. The PWM-control prediction is therefore consistent with the approximately linear temperature-versus-PWM relationship measured in Part 4, with only a small amount of curvature visible at the most extreme cooling points.

---

## 3. Find and Use the Datasheet Maximum-Current Data

From the Laird CP14-127-045 datasheet at a hot-side temperature of $27^\circ\text{C}$, the relevant values and operating conditions are:

- **Module resistance:** $R_M = 1.50\ \Omega$ is the module's effective electrical resistance for the datasheet model at a hot-side temperature of $27^\circ\text{C}$.
- **Maximum current:** $I_{\max} = 8.6\ \text{A}$ is the manufacturer's maximum rated current for the module at the $27^\circ\text{C}$ hot-side condition.
- **Maximum cold-side heat pumping:** $Q_{c,\max} = 71.3\ \text{W}$ is the largest cold-side heat-removal rate at $\Delta T=0$ under the datasheet maximum-current condition with the hot side at $27^\circ\text{C}$.
- **Maximum temperature difference:** $\Delta T_{\max} = 70.5^\circ\text{C}$ is the largest hot-to-cold face temperature difference at zero cold-side heat load, under the datasheet maximum-current condition with the hot side at $27^\circ\text{C}$.

The corresponding voltage at this maximum-current condition is $V_{\max} = 13.9\ \text{V}$.
These are the manufacturer maximum-current conditions, and they define the rated operating point for the module. They are not necessarily the exact conditions in our apparatus, but they provide the correct values for the model. The actual current depends on the power-supply voltage and current limit, the H-bridge voltage drop, the wiring, and the TEC resistance.

At $\Delta T = 0$, the passive conduction term is zero, so a simple symmetric TEC model assigns half of the total Joule heat to each face. Therefore, the object-face Joule heat rate at the maximum current is

$$
\dot Q_{J,\max} = \frac{1}{2} I_{\max}^2 R_M.
$$

Substituting the datasheet values gives

$$
\dot Q_{J,\max}
=\frac{1}{2}(8.6\ \text{A})^2(1.50\ \Omega)
=55.47\ \text{W}
\approx55.5\ \text{W}.
$$

Cooling at the object face is the Peltier heat pumping minus this Joule heat:

$$
Q_{c,\max} = \dot Q_{P,\max} - \dot Q_{J,\max}.
$$

So,

$$
\dot Q_{P,\max} = Q_{c,\max} + \dot Q_{J,\max}.
$$

Therefore,

$$
\dot Q_{P,\max}
=71.3\ \text{W}+55.47\ \text{W}
=126.77\ \text{W}
\approx126.8\ \text{W}.
$$

Then the datasheet maximum-current prediction is

$$
r_{\mathrm{Laird},\max}
=\frac{\dot Q_{P,\max} + \dot Q_{J,\max}}
{\dot Q_{P,\max} - \dot Q_{J,\max}}
=\frac{126.77+55.47}{126.77-55.47}
=\frac{182.24}{71.30}
\approx2.56.
$$

Thus the manufacturer-based maximum-current prediction is $r_{\mathrm{Laird},\max}\approx2.56$. This is close to the measured apparatus value $r\approx2.45$, which is about 4% lower than the datasheet-model prediction.
