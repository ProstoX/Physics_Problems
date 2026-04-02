## 7. Elimination of time and interpretation of acceleration

The path equation is given in parametric form:

$$
x(t)=2t^2, \qquad y(t)=3t^3
$$

* Eliminate the parameter $t$.
* Draw the trajectory.
* Calculate $\vec v(t)$, $|\vec v(t)|$, $\vec a(t)$ and $|\vec a(t)|$.
* Is the acceleration constant?

### Variables and Units Glossary

Here is a quick breakdown of the symbols used in this problem and their standard SI units:

* **$t$ (Time):** The independent variable representing elapsed time. Measured in seconds ($\text{s}$).
* **$x(t), y(t)$ (Position Coordinates):** The horizontal and vertical positions of the object at a given time. Measured in meters ($\text{m}$).
* **$\vec{v}(t)$ (Velocity Vector):** The rate of change of the position vector, describing the object's directional speed. Measured in meters per second ($\text{m/s}$).
* **$|\vec{v}(t)|$ (Speed):** The magnitude (scalar length) of the velocity vector. Measured in meters per second ($\text{m/s}$).
* **$\vec{a}(t)$ (Acceleration Vector):** The rate of change of the velocity vector. Measured in meters per second squared ($\text{m/s}^2$).
* **$|\vec{a}(t)|$ (Magnitude of Acceleration):** The scalar length of the acceleration vector. Measured in meters per second squared ($\text{m/s}^2$).
* **$\hat{i}, \hat{j}$ (Unit Vectors):** Directional indicators for the x-axis and y-axis, respectively. They are unitless.

---

### Step-by-Step Solution

**Initial Setup:**
We are given the parametric equations of motion:
$$x(t) = 2t^2$$
$$y(t) = 3t^3$$

#### 1. Eliminate the parameter $t$
To find the direct relationship between $x$ and $y$ (the path equation), we need to eliminate $t$ from the equations. 

First, let's manipulate both equations so they share a common power of $t$. We can raise the $x$ equation to the power of $3$, and the $y$ equation to the power of $2$:
* From $x = 2t^2$, we isolate $t^2$:
  $$t^2 = \frac{x}{2}$$
  Cube both sides:
  $$(t^2)^3 = \left(\frac{x}{2}\right)^3 \implies t^6 = \frac{x^3}{8}$$

* From $y = 3t^3$, we isolate $t^3$:
  $$t^3 = \frac{y}{3}$$
  Square both sides:
  $$(t^3)^2 = \left(\frac{y}{3}\right)^2 \implies t^6 = \frac{y^2}{9}$$

Since both expressions now equal $t^6$, we can set them equal to each other:
$$\frac{y^2}{9} = \frac{x^3}{8}$$

Multiply by $9$ to isolate $y^2$:
$$y^2 = \frac{9}{8}x^3$$

If we solve for $y$, we get the explicit path equation:
$$y(x) = \pm \sqrt{\frac{9}{8}x^3}$$

#### 2. Draw the trajectory
The equation $y^2 = \frac{9}{8}x^3$ describes a mathematical curve known as a **semicubical parabola**. 
* Because $x^3$ must be positive for $y$ to have real solutions, the curve only exists for $x \ge 0$.
* The $\pm$ indicates that the curve is symmetric across the x-axis. As $t$ goes from negative to positive, the particle travels along the bottom branch (where $y < 0$), hits a sharp point or "cusp" at the origin $(0,0)$ at $t=0$, and then travels outward along the top branch (where $y > 0$).

#### 3. Calculate $\vec{v}(t)$, $|\vec{v}(t)|$, $\vec{a}(t)$, and $|\vec{a}(t)|$

**Velocity Vector $\vec{v}(t)$:**
Take the first derivative of the position components with respect to time ($t$).
$$v_x(t) = \frac{dx}{dt}(2t^2) = 4t$$
$$v_y(t) = \frac{dy}{dt}(3t^3) = 9t^2$$
$$\vec{v}(t) = 4t\hat{i} + 9t^2\hat{j}$$

**Speed $|\vec{v}(t)|$:**
Use the Pythagorean theorem to find the magnitude of the velocity vector.
$$|\vec{v}(t)| = \sqrt{(v_x)^2 + (v_y)^2}$$
$$|\vec{v}(t)| = \sqrt{(4t)^2 + (9t^2)^2}$$
$$|\vec{v}(t)| = \sqrt{16t^2 + 81t^4}$$
*(You can factor out a $t^2$ to simplify this to $|t|\sqrt{16 + 81t^2}$)*

**Acceleration Vector $\vec{a}(t)$:**
Take the derivative of the velocity components with respect to time.
$$a_x(t) = \frac{d}{dt}(4t) = 4$$
$$a_y(t) = \frac{d}{dt}(9t^2) = 18t$$
$$\vec{a}(t) = 4\hat{i} + 18t\hat{j}$$

**Magnitude of Acceleration $|\vec{a}(t)|$:**
Use the Pythagorean theorem on the acceleration vector components.
$$|\vec{a}(t)| = \sqrt{(a_x)^2 + (a_y)^2}$$
$$|\vec{a}(t)| = \sqrt{(4)^2 + (18t)^2}$$
$$|\vec{a}(t)| = \sqrt{16 + 324t^2}$$

#### 4. Is the acceleration constant?
**No.** While the horizontal acceleration ($4 \text{ m/s}^2$) is constant, the vertical acceleration ($18t \text{ m/s}^2$) explicitly depends on time $t$. Because at least one component of the vector changes as time progresses, the overall acceleration vector is not constant.


*Visualization is available at [solution_07.html](solution_07.html)*