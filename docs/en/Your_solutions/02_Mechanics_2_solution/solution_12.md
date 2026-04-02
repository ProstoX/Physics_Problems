## 12. Work and energy with a constant force

A constant force acts on a body of mass $m = 2\ \mathrm{kg}$:

$$
\vec F = [6, 2]\ \mathrm{N}
$$

The body starts with an initial velocity $\vec v(0) = (1, -1)\ \mathrm{\frac{m}{s}}$ from the point $\vec r(0)=(0,0)\ \mathrm{m}$. 
* Determine $\vec a(t)$.
* Determine $\vec v(t)$.
* Determine $\vec r(t)$.
* Draw the trajectory of the motion.
* Calculate the work done by the force at time $t=3\ \mathrm{s}$.
* Check the consistency with the work-energy theorem.

---

### Variable Definitions and Units

* **$m$**: Mass of the object, measured in kilograms (kg).
* **$t$**: Time, measured in seconds (s).
* **$\vec{F}$**: Force vector acting on the object, measured in Newtons (N).
* **$\vec{a}(t)$**: Acceleration vector, measured in meters per second squared (m/s$^2$).
* **$\vec{v}(t)$**: Velocity vector, measured in meters per second (m/s).
* **$\vec{r}(t)$**: Position vector, measured in meters (m).
* **$W$**: Work done by the force, measured in Joules (J).
* **$K$**: Kinetic energy, measured in Joules (J).

---

### Step-by-Step Solution

**Step 1: Determine the acceleration $\vec{a}(t)$**
According to Newton's Second Law, the net force acting on an object is equal to its mass times its acceleration ($\vec{F} = m\vec{a}$). Because the force is constant, the acceleration will also be constant.
$$\vec{a}(t) = \frac{\vec{F}}{m}$$
Given $\vec{F} = [6, 2]\ \mathrm{N}$ and $m = 2\ \mathrm{kg}$:
$$\vec{a}(t) = \left[\frac{6}{2}, \frac{2}{2}\right] = [3, 1]\ \mathrm{\frac{m}{s^2}}$$

**Step 2: Determine the velocity $\vec{v}(t)$**
Velocity is the integral of acceleration with respect to time ($\vec{v} = \int \vec{a} dt$). We integrate the constant acceleration and add the initial velocity vector $\vec{v}(0)$ as the constant of integration.
$$\vec{v}(t) = \vec{a}t + \vec{v}(0)$$
Given $\vec{v}(0) = (1, -1)\ \mathrm{m/s}$:
$$\vec{v}(t) = [3t, t] + [1, -1] = [3t + 1, t - 1]\ \mathrm{\frac{m}{s}}$$

**Step 3: Determine the position $\vec{r}(t)$**
Position is the integral of velocity with respect to time ($\vec{r} = \int \vec{v} dt$). We integrate each component of the velocity vector and use the initial position $\vec{r}(0) = (0,0)\ \mathrm{m}$ for the constants of integration.
$$\vec{r}(t) = \int [3t + 1, t - 1] dt$$
$$\vec{r}(t) = \left[\frac{3}{2}t^2 + t + C_x, \frac{1}{2}t^2 - t + C_y\right]$$
Since the body starts at the origin ($C_x = 0, C_y = 0$):
$$\vec{r}(t) = \left[\frac{3}{2}t^2 + t, \frac{1}{2}t^2 - t\right]\ \mathrm{m}$$

**Step 4: Draw the trajectory of the motion**
*Note: While I cannot physically draw on the screen, I have provided the prompt below for an AI to generate the visual graph. The path traced in the x-y plane is a continuous parabolic curve representing constant acceleration in 2D space.*

**Step 5: Calculate the work done by the force at time $t = 3\ \mathrm{s}$**
Work is defined as the dot product of the constant force and the displacement vector ($\Delta\vec{r}$).
$$W = \vec{F} \cdot \Delta\vec{r}$$
First, find the displacement at $t = 3\ \mathrm{s}$. Since the initial position is $(0,0)$, the displacement is simply $\vec{r}(3)$:
$$\vec{r}(3) = \left[\frac{3}{2}(3)^2 + 3, \frac{1}{2}(3)^2 - 3\right] = [13.5 + 3, 4.5 - 3] = [16.5, 1.5]\ \mathrm{m}$$
Now, calculate the dot product:
$$W = [6, 2] \cdot [16.5, 1.5] = (6 \cdot 16.5) + (2 \cdot 1.5)$$
$$W = 99 + 3 = 102\ \mathrm{J}$$

**Step 6: Check consistency with the work-energy theorem**
The work-energy theorem states that the work done on an object equals its change in kinetic energy ($W = \Delta K = K_f - K_i$).
* **Initial Kinetic Energy ($K_i$):** At $t=0$, velocity is $\vec{v}(0) = [1, -1]$. The speed squared is $v_i^2 = 1^2 + (-1)^2 = 2\ \mathrm{m^2/s^2}$.
    $$K_i = \frac{1}{2}m v_i^2 = \frac{1}{2}(2)(2) = 2\ \mathrm{J}$$
* **Final Kinetic Energy ($K_f$):** At $t=3$, the velocity is $\vec{v}(3) = [3(3) + 1, 3 - 1] = [10, 2]\ \mathrm{m/s}$. The speed squared is $v_f^2 = 10^2 + 2^2 = 100 + 4 = 104\ \mathrm{m^2/s^2}$.
    $$K_f = \frac{1}{2}m v_f^2 = \frac{1}{2}(2)(104) = 104\ \mathrm{J}$$
* **Change in Kinetic Energy:**
    $$\Delta K = K_f - K_i = 104\ \mathrm{J} - 2\ \mathrm{J} = 102\ \mathrm{J}$$
The calculated work ($102\ \mathrm{J}$) perfectly matches the change in kinetic energy ($102\ \mathrm{J}$). The results are consistent.