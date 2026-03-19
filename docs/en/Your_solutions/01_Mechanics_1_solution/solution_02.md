### Variables and Units Glossary

Here is a quick breakdown of the symbols used in this specific equation and their standard SI units:

* **$R(\theta)$ (Range):** The total horizontal distance traveled by the projectile before hitting the ground, as a function of the launch angle. Measured in meters (m).
* **$v_0$ (Initial Velocity):** The speed at which the projectile is launched. Measured in meters per second (m/s).
* **$\theta$ (Launch Angle):** The angle above the horizontal at which the projectile is fired. Measured in degrees ($^\circ$) or radians (rad).
* **$g$ (Acceleration due to gravity):** The constant downward acceleration caused by Earth's gravity. Measured in meters per second squared (m/s²).

---

### Step-by-Step Analytical Solution

**Objective:** Prove that the maximum value of $R(\theta) = \frac{v_0^2 \sin(2\theta)}{g}$ occurs when $\theta = 45^\circ$.



#### Step 1: Isolate the Variable Component
In the given range equation, for a specific launch, the initial velocity ($v_0$) and the acceleration due to gravity ($g$) are constants. 

This means that the fraction $\frac{v_0^2}{g}$ is a fixed positive number. Therefore, the value of the range $R(\theta)$ depends entirely on the trigonometric component of the equation: $\sin(2\theta)$.

#### Step 2: Determine the Maximum Value of the Sine Function
To maximize the entire range equation, we must maximize the variable component, $\sin(2\theta)$. 

By definition of the trigonometric sine function, the value of sine for any real angle always fluctuates between $-1$ and $1$. Therefore, the absolute maximum mathematical value that $\sin(2\theta)$ can output is $1$.

#### Step 3: Solve for the Angle
Set the sine component equal to its maximum value:
$$\sin(2\theta) = 1$$

To find the angle that satisfies this equation, we take the inverse sine (arcsin) of $1$. The angle whose sine is $1$ is $90^\circ$ (or $\frac{\pi}{2}$ radians).
$$2\theta = 90^\circ$$

Now, simply divide by $2$ to isolate $\theta$:
$$\theta = \frac{90^\circ}{2}$$
$$\theta = 45^\circ$$

*(Note: While a calculus approach—taking the derivative $R'(\theta)$, setting it to $0$, and confirming a negative second derivative—also arrives at this answer, this trigonometric optimization is the most direct and mathematically elegant proof.)*

*Visualization is available at [solution_02.html](solution_02.html)*