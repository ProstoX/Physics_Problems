## 14. RLC Circuit

Write down the differential equation for a series RLC circuit with a voltage source $V$, a resistor $R$, an inductor $L$, and a capacitor $C$. Assume the current is $I(t)$ and the voltage across the capacitor is $V_C(t)$. Compare this to the equation of a damped harmonic oscillator. What are the analogies between the terms in the two equations?

---

## RLC Circuit and Its Analogy to a Damped Harmonic Oscillator

### Meaning of Symbols and Units

| Symbol | Meaning | Units |
| --- | --- | --- |
| $V(t)$ | Applied voltage source | volts (V) |
| $R$ | Resistance | ohms ($\Omega$) |
| $L$ | Inductance | henries (H) |
| $C$ | Capacitance | farads (F) |
| $I(t)$ | Current in the circuit | amperes (A) |
| $V_C(t)$ | Voltage across the capacitor | volts (V) |
| $t$ | Time | seconds (s) |

---

### Step 1 — Apply Kirchhoff’s Voltage Law

For a series RLC circuit, the sum of voltage drops equals the source voltage:


$$V(t) = V_R + V_L + V_C$$

The voltage across each component is:

* **Resistor:** $V_R = RI$
* **Inductor:** $V_L = L\frac{dI}{dt}$
* **Capacitor:** $V_C = \frac{1}{C}\int I \, dt$

Substituting into Kirchhoff’s law:


$$V(t) = RI + L\frac{dI}{dt} + \frac{1}{C}\int I \, dt$$

---

### Step 2 — Convert to a Differential Equation

Differentiate both sides with respect to time:


$$\frac{dV}{dt} = L\frac{d^2 I}{dt^2} + R\frac{dI}{dt} + \frac{1}{C}I$$

Rearranging:


$$L\frac{d^2 I}{dt^2} + R\frac{dI}{dt} + \frac{1}{C}I = \frac{dV}{dt}$$

#### Final Differential Equation

For the case of no external driving voltage ($V = 0$):


$$L\frac{d^2 I}{dt^2} + R\frac{dI}{dt} + \frac{1}{C}I = 0$$

---

### Comparison to a Damped Harmonic Oscillator

The equation for a damped harmonic oscillator is:


$$m\frac{d^2 x}{dt^2} + b\frac{dx}{dt} + kx = 0$$

| Symbol | Meaning |
| --- | --- |
| $m$ | Mass |
| $b$ | Damping coefficient |
| $k$ | Spring constant |
| $x(t)$ | Displacement |

#### Analogy Between the Two Systems

Match the terms in both equations:

| Mechanical Oscillator | RLC Circuit | Physical Meaning |
| --- | --- | --- |
| $m$ | $L$ | Inertia / energy storage |
| $b$ | $R$ | Damping / energy loss |
| $k$ | $\frac{1}{C}$ | Restoring force |
| $x(t)$ | $I(t)$ | Dynamic variable |

* The **inductor** behaves like mass, resisting rapid changes in current.
* The **resistor** behaves like friction, dissipating energy.
* The **capacitor** behaves like a spring, storing and releasing energy.

---

### Physical Interpretation

An RLC circuit can oscillate because energy continuously transfers between the magnetic field of the inductor and the electric field of the capacitor. The resistor gradually removes energy from the system, causing the oscillations to decay over time, exactly like friction damps a mechanical oscillator.