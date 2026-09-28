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

0pwm Heating: StartTime: 27s, Temp 28C, EndTime: 100s, EndTemp: 34C
8pwm Heating: StartTime: 0s, Temp: 34C, EndTime: 125s, EndTemp: 39C
15pwm Heating: StartTime: 0s, Temp: 23C, EndTime: 165s, EndTemp: 42C
23pwm Heating: StartTime: 0s, Temp: 28C, EndTime: 130s, EndTemp: 46C
30pwm Heating: StartTime: 0s, Temp: 33C, EndTime: 125s, EndTemp: 50C

0pwm Cooling: StartTime: 0s, Temp: 51C, EndTime: 200s, EndTemp: 37C
33pwm Cooling: StartTime: 0s, Temp: 38C, EndTime: 185s, EndTemp: 30.5C
65pwm Cooling: StartTime: 0s, Temp: 30C, EndTime: 140s, EndTemp: 24.5C
98pwm Cooling: StartTime: 0s, Temp: 47C, EndTime: 207s, EndTemp: 18C
130pwm Cooling: StartTime: 0s, Temp: 33C, EndTime: 290s, EndTemp: 10.4C

# Part 4: Temperature vs. Signed PWM

![Steady-state temperature versus signed PWM](Part%204/temperature_vs_signed_pwm.png)



| Direction | PWM (counts) | Steady-state temperature (°C) |
|---|---:|---:|
| Heating | 0 | 35.60 |
| Heating | 8 | 39.20 |
| Heating | 15 | 42.89 |
| Heating | 23 | 46.09 |
| Heating | 30 | 50.45 |
| Cooling | 0 | 35.29 |
| Cooling | -33 | 30.35 |
| Cooling | -65 | 24.43 |
| Cooling | -98 | 17.83 |
| Cooling | -130 | 9.75 |

Using a straight-line fit over the measured range, the temperature susceptibility is approximately **0.49 °C per PWM count for heating** and **0.20 °C per PWM count for cooling** (with cooling plotted on the negative-PWM side). These fitted slopes are approximate overall responses.