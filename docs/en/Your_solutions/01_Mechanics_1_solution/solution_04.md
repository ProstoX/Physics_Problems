## 4. Vector Calculus

The position of an object is given by $\vec{r}(t) = (3t^2)\hat{i} + (5t - 8t^2)\hat{j}$. Find the object's velocity and acceleration vectors as a function of time.

### Variables and Units Glossary

Before solving the equations, here is a breakdown of the mathematical symbols used in this problem and their standard SI units:

* **$t$ (Time):** The independent variable representing elapsed time. Measured in seconds (s).
* **$\vec{r}(t)$ (Position Vector):** A vector that points from the origin to the object's location at any given time $t$. Measured in meters (m).
* **$\vec{v}(t)$ (Velocity Vector):** The rate of change of the position vector. It describes how fast and in what direction the object is moving. Measured in meters per second (m/s).
* **$\vec{a}(t)$ (Acceleration Vector):** The rate of change of the velocity vector. It describes how the object's speed and direction are changing. Measured in meters per second squared (m/s²).
* **$\hat{i}$ and $\hat{j}$ (Unit Vectors):** Directional indicators representing the standard horizontal (x-axis) and vertical (y-axis) directions, respectively. They have a magnitude of exactly 1 and are unitless.



---

### Step-by-Step Solution

**Initial Setup:**
We are given the object's position as a vector function of time:
$$\vec{r}(t) = (3t^2)\hat{i} + (5t - 8t^2)\hat{j}$$

#### 1. Determine the Velocity Vector, $\vec{v}(t)$
In kinematics, velocity is the first derivative of position with respect to time. To find the velocity vector, we take the derivative of the $x$ (or $\hat{i}$) component and the $y$ (or $\hat{j}$) component independently.

$$\vec{v}(t) = \frac{d}{dt}[\vec{r}(t)]$$
$$\vec{v}(t) = \frac{d}{dt}(3t^2)\hat{i} + \frac{d}{dt}(5t - 8t^2)\hat{j}$$

Using the standard power rule for derivatives ($\frac{d}{dt}(t^n) = nt^{n-1}$):
* Derivative of $3t^2$ is $6t$.
* Derivative of $5t - 8t^2$ is $5 - 16t$.

Putting these back into the vector equation:
$$\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$$

#### 2. Determine the Acceleration Vector, $\vec{a}(t)$
Acceleration is the first derivative of velocity with respect to time (or the second derivative of position). We take the derivative of our new velocity vector components.

$$\vec{a}(t) = \frac{d}{dt}[\vec{v}(t)]$$
$$\vec{a}(t) = \frac{d}{dt}(6t)\hat{i} + \frac{d}{dt}(5 - 16t)\hat{j}$$

Again, applying the power rule:
* Derivative of $6t$ is $6$.
* Derivative of $5 - 16t$ is $-16$.

Putting these back into the vector equation:
$$\vec{a}(t) = 6\hat{i} - 16\hat{j}$$

**Conclusion:** The velocity vector is **$\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$**, meaning the velocity changes over time in both directions. 
The acceleration vector is **$\vec{a}(t) = 6\hat{i} - 16\hat{j}$**, which is a constant vector, meaning the acceleration does not change as time progresses.

*Visualization is available at [solution_04.html](solution_04.html)*