## 9. Vertical throw with drag

We have the equation of motion:

$$
m\frac{dv}{dt} = -mg - kv
$$

with initial conditions $v(0)=v_0$, $x(0)=10$.

* Solve the equation by analytical methods.
* Determine the maximum height.
* Compare with the case without drag.
* Perform a numerical simulation using HTML or Pythyon.

---

Here is the step-by-step solution to the vertical throw problem with linear drag, including the mathematical derivations, the requested Python simulation, and the prompt for your HTML visualization.

### Variable Definitions

Before solving the equations, here is a breakdown of the variables used and their standard units:

* **$m$**: Mass of the projected object. Measured in kilograms (kg).
* **$v$**: Velocity of the object at time $t$. Measured in meters per second (m/s).
* **$t$**: Time elapsed since the throw. Measured in seconds (s).
* **$g$**: Acceleration due to gravity (approx. 9.81 m/s² on Earth). Measured in meters per second squared (m/s²).
* **$k$**: Linear drag coefficient, representing the strength of air resistance. Measured in kilograms per second (kg/s) or Newton-seconds per meter (N·s/m).
* **$x$**: Vertical position or height of the object. Measured in meters (m).
* **$v_0$**: Initial upward velocity at $t=0$. Measured in meters per second (m/s).
* **$x_0$**: Initial height at $t=0$ (given as 10 m).

---

### Part 1: Analytical Solution

**Goal:** Solve the differential equation $m\frac{dv}{dt} = -mg - kv$ to find velocity $v(t)$ and position $x(t)$.

#### Step 1: Solve for Velocity $v(t)$
We start by rearranging the equation of motion to separate the variables $v$ and $t$:
$$\frac{dv}{dt} = -g - \frac{k}{m}v$$
$$\frac{dv}{g + \frac{k}{m}v} = -dt$$

Integrate both sides. The left side from $v_0$ to $v$, and the right side from $0$ to $t$:
$$\int_{v_0}^{v} \frac{dv}{g + \frac{k}{m}v} = \int_{0}^{t} -dt$$

Using the substitution rule, the integral on the left yields a natural logarithm:
$$\frac{m}{k} \ln \left| \frac{g + \frac{k}{m}v}{g + \frac{k}{m}v_0} \right| = -t$$

Multiply by $\frac{k}{m}$ and exponentiate both sides to isolate $v$:
$$\frac{g + \frac{k}{m}v}{g + \frac{k}{m}v_0} = e^{-\frac{k}{m}t}$$
$$g + \frac{k}{m}v = \left( g + \frac{k}{m}v_0 \right) e^{-\frac{k}{m}t}$$

Finally, subtract $g$ and multiply by $\frac{m}{k}$ to get the velocity function:
$$v(t) = \left( v_0 + \frac{mg}{k} \right) e^{-\frac{k}{m}t} - \frac{mg}{k}$$

*(Note: $\frac{mg}{k}$ represents the terminal velocity of the object).*

#### Step 2: Solve for Position $x(t)$
Since velocity is the derivative of position ($v = \frac{dx}{dt}$), we integrate $v(t)$ to find $x(t)$:
$$x(t) = \int v(t) dt$$
$$x(t) = \int \left[ \left( v_0 + \frac{mg}{k} \right) e^{-\frac{k}{m}t} - \frac{mg}{k} \right] dt$$

Evaluating the integral gives us:
$$x(t) = -\frac{m}{k} \left( v_0 + \frac{mg}{k} \right) e^{-\frac{k}{m}t} - \frac{mg}{k}t + C$$

To find the constant $C$, we use the initial condition $x(0) = 10$:
$$10 = -\frac{m}{k} \left( v_0 + \frac{mg}{k} \right) e^{0} - 0 + C$$
$$C = 10 + \frac{m}{k} \left( v_0 + \frac{mg}{k} \right)$$

Substitute $C$ back into the equation to get the final position function:
$$x(t) = 10 + \frac{m}{k} \left( v_0 + \frac{mg}{k} \right) \left( 1 - e^{-\frac{k}{m}t} \right) - \frac{mg}{k}t$$

---

### Part 2: Determine the Maximum Height

**Goal:** Find the exact peak height the object reaches before falling back down.

**Step 1: Find the time of maximum height ($t_{max}$).**
At the maximum height, the object momentarily stops moving upward, so $v(t_{max}) = 0$.
$$0 = \left( v_0 + \frac{mg}{k} \right) e^{-\frac{k}{m}t_{max}} - \frac{mg}{k}$$
$$e^{-\frac{k}{m}t_{max}} = \frac{\frac{mg}{k}}{v_0 + \frac{mg}{k}}$$

Take the reciprocal and then the natural log of both sides:
$$e^{\frac{k}{m}t_{max}} = \frac{v_0 + \frac{mg}{k}}{\frac{mg}{k}} = 1 + \frac{kv_0}{mg}$$
$$t_{max} = \frac{m}{k} \ln \left( 1 + \frac{kv_0}{mg} \right)$$

**Step 2: Substitute $t_{max}$ into the position function.**
Plug $t_{max}$ and the simplified exponent term ($e^{-\frac{k}{m}t_{max}} = \frac{mg/k}{v_0 + mg/k}$) into $x(t)$:
$$x_{max} = 10 + \frac{m}{k} \left( v_0 + \frac{mg}{k} \right) \left( 1 - \frac{\frac{mg}{k}}{v_0 + \frac{mg}{k}} \right) - \frac{mg}{k} \left[ \frac{m}{k} \ln \left( 1 + \frac{kv_0}{mg} \right) \right]$$

Simplify the term inside the first set of brackets:
$$1 - \frac{\frac{mg}{k}}{v_0 + \frac{mg}{k}} = \frac{v_0}{v_0 + \frac{mg}{k}}$$

Multiply this by the terms in front of it:
$$x_{max} = 10 + \frac{m}{k} v_0 - \frac{m^2g}{k^2} \ln \left( 1 + \frac{kv_0}{mg} \right)$$

---

### Part 3: Compare With the Case Without Drag

When there is no air resistance ($k \to 0$), the physics simplify considerably.

* **Equation of Motion:** $m\frac{dv}{dt} = -mg \implies a = -g$
* **Velocity:** $v(t) = v_0 - gt$
* **Position:** $x(t) = 10 + v_0t - \frac{1}{2}gt^2$
* **Maximum Height:** Occurs at $t = \frac{v_0}{g}$.
    $$x_{max\ (no\ drag)} = 10 + \frac{v_0^2}{2g}$$

**Comparison Analysis:**
1.  **Peak Height:** The object will reach a strictly **lower** maximum height when drag is present. Drag acts as a non-conservative force continuously doing negative work against the object's motion, sapping its initial kinetic energy.
2.  **Time to Peak:** The object reaches its peak **faster** when drag is present. Both gravity and drag point downward while the object rises, creating a larger net deceleration than gravity alone.
3.  **Symmetry:** Without drag, the upward and downward trips take the same amount of time, and the object returns to its start point at speed $v_0$. With drag, the trip is asymmetrical. It falls slower than it rises, and returns with a speed less than $v_0$.

---

### Part 4: Numerical Simulation (Python)

Below is a Python script that uses the Euler method to simulate the vertical throw numerically. It plots both the velocity and position over time, comparing the "Drag" case with the "No Drag" case.

```python
import numpy as np
import matplotlib.pyplot as plt

# --- Physical Constants & Initial Conditions ---
m = 1.0       # Mass (kg)
g = 9.81      # Gravity (m/s^2)
k = 0.5       # Drag coefficient (kg/s)
v0 = 25.0     # Initial upward velocity (m/s)
x0 = 10.0     # Initial height (m)

dt = 0.01     # Time step for numerical integration (s)
t_end = 4.0   # Total simulation time (s)

# --- Arrays for Numerical Simulation ---
t = np.arange(0, t_end, dt)
v_num = np.zeros(len(t))
x_num = np.zeros(len(t))
v_num[0] = v0
x_num[0] = x0

# --- Euler Method Integration ---
for i in range(1, len(t)):
    # Calculate acceleration (dv/dt) at current step
    dv_dt = -g - (k/m) * v_num[i-1]
    
    # Update velocity and position
    v_num[i] = v_num[i-1] + dv_dt * dt
    x_num[i] = x_num[i-1] + v_num[i-1] * dt

# --- Ideal Case (No Drag) for Comparison ---
v_ideal = v0 - g * t
x_ideal = x0 + v0 * t - 0.5 * g * t**2

# --- Plotting the Results ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Position Plot
ax1.plot(t, x_num, label='With Drag (Numeric)', color='red', linewidth=2)
ax1.plot(t, x_ideal, label='No Drag (Analytical)', color='blue', linestyle='--')
ax1.set_title('Vertical Position over Time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Height (m)')
ax1.grid(True)
ax1.legend()

# Velocity Plot
ax2.plot(t, v_num, label='With Drag (Numeric)', color='red', linewidth=2)
ax2.plot(t, v_ideal, label='No Drag (Analytical)', color='blue', linestyle='--')
ax2.axhline(0, color='black', linewidth=1) # Zero velocity line
ax2.set_title('Vertical Velocity over Time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()
```
