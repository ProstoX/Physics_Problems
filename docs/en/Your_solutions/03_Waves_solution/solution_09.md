## 9. Damped oscillator

For the given equation describing a damped harmonic oscillator:

$$
m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0
$$

make interactive HTML animation with a slider for the parameter $b$ to show the behavior of the system in the underdamped, critically damped, and overdamped cases. Include graphs of $x(t)$ and the phase portrait for each case.

1. Write down the general solution.
2. Present the classification of cases: underdamped, critically damped, overdamped.
3. Solve the equation numerically (RK4).
4. Investigate the effect of parameter $b$.
5. Generate the graph of $x(t)$.
6. Generate the phase portrait.

---

### Variables and Units

Before solving the equation, let's define what each letter stands for and its standard SI unit:

* **$x$**: Displacement or position of the oscillator from its equilibrium point. Measured in meters (m).
* **$t$**: Time. Measured in seconds (s).
* **$m$**: Mass of the oscillating object. Measured in kilograms (kg).
* **$b$**: Damping coefficient, representing the strength of the resistance (like air resistance or friction). Measured in kilograms per second (kg/s) or Newton-seconds per meter (N·s/m).
* **$k$**: Spring constant, representing the stiffness of the restoring force. Measured in Newtons per meter (N/m) or kilograms per second squared (kg/s$^2$).

---

### Step 1: Write down the general solution

The equation is a second-order linear homogeneous ordinary differential equation (ODE):
$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0$$

To find the general solution, we assume a solution of the form $x(t) = e^{rt}$, where $r$ is a constant. Taking the derivatives and substituting them back into the ODE yields the characteristic equation:
$$m r^2 + b r + k = 0$$

Using the quadratic formula to solve for $r$:
$$r = \frac{-b \pm \sqrt{b^2 - 4mk}}{2m}$$

The general solution is a linear combination of the solutions for the two roots ($r_1$ and $r_2$):
$$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$
*(Where $C_1$ and $C_2$ are constants determined by initial conditions like starting position and velocity).*

---

### Step 2: Present the classification of cases

The behavior of the system depends entirely on the discriminant under the square root: $\Delta = b^2 - 4mk$. We define the damping ratio $\zeta = \frac{b}{2\sqrt{mk}}$ and the natural frequency $\omega_n = \sqrt{\frac{k}{m}}$. 

1.  **Underdamped ($b^2 < 4mk$ or $\zeta < 1$):** The discriminant is negative, resulting in complex roots. The system oscillates with an exponentially decaying amplitude. 
    **Solution form:** $x(t) = A e^{-\frac{b}{2m}t} \cos(\omega_d t + \phi)$
    *(where $\omega_d$ is the damped frequency)*
2.  **Critically Damped ($b^2 = 4mk$ or $\zeta = 1$):**
    The discriminant is zero, resulting in a single repeated real root. The system returns to equilibrium as quickly as possible without oscillating.
    **Solution form:** $x(t) = (C_1 + C_2 t) e^{-\frac{b}{2m}t}$
3.  **Overdamped ($b^2 > 4mk$ or $\zeta > 1$):**
    The discriminant is positive, resulting in two distinct negative real roots. The system slowly returns to equilibrium without oscillating. 
    **Solution form:** $x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$

---

### Step 3: Solve the equation numerically (RK4)

To solve this numerically using the Runge-Kutta 4th Order (RK4) method, we must reduce the second-order ODE into a system of two first-order ODEs. 

Let velocity $v = \frac{dx}{dt}$. 
Now we have our system:
1.  $\frac{dx}{dt} = v$
2.  $\frac{dv}{dt} = -\frac{b}{m}v - \frac{k}{m}x$

RK4 calculates the next state $(x_{n+1}, v_{n+1})$ from the current state $(x_n, v_n)$ by evaluating the derivatives at four different points within a small time step $\Delta t$, and taking a weighted average of these slopes to step forward in time. This is highly stable and accurate for visualizing trajectories over time.

---

### Step 4: Investigate the effect of parameter $b$

* When $b = 0$, the system is an **undamped** simple harmonic oscillator. It will oscillate forever.
* As $b$ increases from $0$ up to $2\sqrt{mk}$, the system oscillates, but the amplitude dies out faster and faster over time. The frequency of oscillation also slightly decreases.
* When $b$ hits exactly $2\sqrt{mk}$, the damping is just strong enough to prevent any oscillation entirely.
* As $b$ increases beyond $2\sqrt{mk}$, the "friction" becomes so immense that it acts sluggishly, taking a very long time to creep back to the $x=0$ equilibrium point.