## 3. Conservation of Energy

A pendulum with a length of 1.0 meter is released from an initial angle of $15^\circ$. What is the speed of the pendulum bob at the bottom of its swing?

---

### Variable Definitions

Before solving the problem, here is a breakdown of the variables used in this conservation of energy scenario:

* **$L$**: The length of the pendulum string. Measured in meters (m).
* **$\theta$**: The initial angle from the vertical at which the pendulum is released. Measured in degrees (°).
* **$h$**: The initial height of the pendulum bob relative to its lowest point. Measured in meters (m).
* **$g$**: The acceleration due to gravity. On Earth, this is approximately 9.81 m/s².
* **$m$**: The mass of the pendulum bob. Measured in kilograms (kg). *(Note: As we will see, mass cancels out in this specific problem).*
* **$v$**: The velocity (speed) of the bob at the lowest point. Measured in meters per second (m/s).
* **$PE$**: Potential Energy, the stored energy based on height. Measured in Joules (J).
* **$KE$**: Kinetic Energy, the energy of motion. Measured in Joules (J).

---

### Step-by-Step Solution

**Goal:** Find the speed of the pendulum at the bottom of its swing given a length of 1.0 m and an initial release angle of 15°.

**Step 1: Understand the Conservation of Energy Principle.**
Because we are ignoring air resistance and friction, the total mechanical energy of the pendulum is conserved. This means the initial Potential Energy ($PE$) at the top of the swing is completely converted into Kinetic Energy ($KE$) at the very bottom of the swing.
$$PE_{initial} = KE_{final}$$

**Step 2: Define the energy equations.**
* The formula for gravitational potential energy is $PE = mgh$.
* The formula for kinetic energy is $KE = \frac{1}{2}mv^2$.

Setting them equal gives us:
$$mgh = \frac{1}{2}mv^2$$

Notice that mass ($m$) is on both sides of the equation. We can divide both sides by $m$ to cancel it out, showing that the final speed does not depend on the pendulum's mass:
$$gh = \frac{1}{2}v^2$$

**Step 3: Find the initial height ($h$).**
We aren't directly given $h$, but we can find it using trigonometry. When the pendulum is pulled back at an angle $\theta$, the string forms a right triangle with the vertical axis. The vertical distance from the pivot to the bob is $L \cos(\theta)$. 
Since the lowest point of the pendulum is at a distance $L$ from the pivot, the height $h$ the bob was raised is the difference between the full string length and that vertical component:
$$h = L - L\cos(\theta)$$
$$h = L(1 - \cos\theta)$$

**Step 4: Substitute the known values to calculate $h$.**
* $L$ = 1.0 m
* $\theta$ = 15°

$$h = 1.0 \cdot (1 - \cos(15^\circ))$$
$$h = 1.0 \cdot (1 - 0.9659)$$
$$h \approx 0.0341 \text{ m}$$

**Step 5: Rearrange the energy equation to solve for velocity ($v$).**
Going back to our simplified energy equation ($gh = \frac{1}{2}v^2$), multiply both sides by 2:
$$v^2 = 2gh$$
Take the square root of both sides:
$$v = \sqrt{2gh}$$

**Step 6: Calculate the final speed.**
Use standard gravity ($g = 9.81$ m/s²) and the height we just calculated:
$$v = \sqrt{2 \cdot 9.81 \cdot 0.0341}$$
$$v = \sqrt{0.669}$$
$$v \approx 0.818$$

**Answer:** The speed of the pendulum bob at the bottom of its swing is approximately **0.818 m/s**.