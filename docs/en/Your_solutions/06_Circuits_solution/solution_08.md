## 8. AC Voltage Equation

The current in an AC circuit is given by $I(t) = 2 \sin(120\pi t)$. If the circuit consists of a single $50\,\Omega$ resistor, what is the equation for the voltage $V(t)$ across it?

---

# 8. AC Voltage Equation

Let:

* (I(t)) = current in **amperes (A)**
* (V(t)) = voltage in **volts (V)**
* (R) = resistance in **ohms ((\Omega))**
* (t) = time in **seconds (s)**

## Solution

We are given:

[
I(t) = 2\sin(120\pi t)
]

and the circuit has a single resistor:

[
R = 50,\Omega
]

For a resistor, Ohm’s law applies:

[
V(t) = R,I(t)
]

Substitute the given current and resistance:

[
V(t) = 50 \cdot 2\sin(120\pi t)
]

[
V(t) = 100\sin(120\pi t)
]

## Answer

[
\boxed{V(t) = 100\sin(120\pi t)\ \text{V}}
]

## Why this works

A resistor does not change the phase of the current and voltage, so the voltage has the same sine form as the current. The only change is that the amplitude is multiplied by the resistance.

## Prompt for another AI to create a single-file HTML visualization

Create a single-file HTML page with embedded CSS and JavaScript that visualizes an AC current and voltage for a resistor. The page should show two synchronized sine waves:

* Current: (I(t) = 2\sin(120\pi t)) A
* Voltage: (V(t) = 100\sin(120\pi t)) V

Requirements:

1. Use a clean, modern layout.
2. Display both formulas clearly at the top.
3. Plot current and voltage on the same time axis, using separate labeled lines.
4. Include a moving time marker or animation so the waves appear dynamic.
5. Add axis labels with units:

   * time in seconds
   * current in amperes
   * voltage in volts
6. Show the resistor value (R = 50,\Omega) and the relation (V = IR).
7. Keep everything in one HTML file with no external libraries unless absolutely necessary.
8. Make the visualization responsive and easy to read.
9. Add a short explanation section below the graph.
