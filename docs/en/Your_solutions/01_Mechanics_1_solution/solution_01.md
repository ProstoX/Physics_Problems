## 1. Projectile Motion

A projectile is fired from the ground with an initial velocity of $100  \text{ m/s}$ at an angle of $37^\circ$ above the horizontal. Assume no air resistance.

* Derive the differential equations of motion in the horizontal and vertical directions.

* Determine the time of flight.

* Determine the maximum height.

* Determine the range.

### Variables and Units Glossary

Before we dive into the math, here is a quick breakdown of the symbols used in the solution, what they represent, and their standard standard SI units:

* **$t$ (Time):** The time elapsed since the projectile was fired. Measured in seconds ($\text{s}$).
* **$x(t)$ (Horizontal Position):** The distance traveled along the ground at time $t$. Measured in meters ($\text{m}$).
* **$y(t)$ (Vertical Position):** The height of the projectile above the ground at time $t$. Measured in meters ($\text{m}$).
* **$v_0$ (Initial Velocity):** The speed at which the projectile is launched. Measured in meters per second ($\text{m/s}$). Given as $100 \text{ m/s}$.
* **$\theta$ (Launch Angle):** The angle above the horizontal at which the projectile is fired. Measured in degrees ($^\circ$). Given as $37^\circ$.
* **$g$ (Acceleration due to gravity):** The constant downward acceleration caused by Earth's gravity. Measured in meters per second squared ($\text{m/s}^2$). Standard value is approximately $9.8 \text{ m/s}^2$.
* **$T$ (Time of Flight):** The total time the projectile spends in the air before hitting the ground. Measured in seconds ($\text{s}$).
* **$H$ (Maximum Height):** The peak vertical position the projectile reaches. Measured in meters ($\text{m}$).
* **$R$ (Range):** The total horizontal distance traveled when the projectile returns to its initial height. Measured in meters ($\text{m}$).

---

### Step-by-Step Solution

**Initial Setup & Components:**
First, we break the initial velocity ($v_0$) into its horizontal ($x$) and vertical ($y$) components using basic trigonometry. 
* Initial horizontal velocity: $v_{0x} = v_0 \cos(\theta) = 100 \cos(37^\circ) \approx 79.86 \text{ m/s}$
* Initial vertical velocity: $v_{0y} = v_0 \sin(\theta) = 100 \sin(37^\circ) \approx 60.18 \text{ m/s}$

#### 1. Differential Equations of Motion
According to Newton's Second Law ($F = ma$), acceleration is the second derivative of position with respect to time ($a = \frac{d^2x}{dt^2}$). Since there is no air resistance, the only force acting on the projectile after launch is gravity, which acts purely in the downward vertical direction.

* **Horizontal Direction:** There are no forces acting horizontally, so acceleration is zero.
    $$m \frac{d^2x}{dt^2} = 0 \implies \frac{d^2x}{dt^2} = 0$$

* **Vertical Direction:** Gravity is the only force, acting downwards.
    $$m \frac{d^2y}{dt^2} = -mg \implies \frac{d^2y}{dt^2} = -g$$

*(Integrating these equations twice with respect to time gives us our standard kinematic equations: $x(t) = v_{0x}t$ and $y(t) = v_{0y}t - \frac{1}{2}gt^2$.)*

#### 2. Determine the Time of Flight ($T$)
The projectile hits the ground when its vertical position $y(t)$ returns to $0$. We set the vertical position equation to $0$ and solve for $t$:

$$y(t) = v_{0y}t - \frac{1}{2}gt^2 = 0$$
$$t \left(v_{0y} - \frac{1}{2}gt\right) = 0$$

This gives two solutions: $t = 0$ (the launch) and $t = T$ (the landing).
$$T = \frac{2v_{0y}}{g}$$

Plugging in our values:
$$T = \frac{2(60.18)}{9.8} \approx \frac{120.36}{9.8} \approx 12.28 \text{ s}$$

#### 3. Determine the Maximum Height ($H$)
The projectile reaches its maximum height at the exact middle of its flight (since the trajectory is a symmetrical parabola), which occurs at $t = \frac{T}{2}$, or when vertical velocity ($v_y$) is exactly $0$. Let's use the kinematic formula that doesn't rely on time: $v_y^2 = v_{0y}^2 - 2g(y - y_0)$. Setting $v_y = 0$ and solving for $y$ (which is $H$):

$$0 = v_{0y}^2 - 2gH$$
$$H = \frac{v_{0y}^2}{2g}$$

Plugging in our values:
$$H = \frac{(60.18)^2}{2(9.8)} = \frac{3621.63}{19.6} \approx 184.78 \text{ m}$$

#### 4. Determine the Range ($R$)
The range is the horizontal distance traveled during the total time of flight ($T$). Since horizontal velocity is constant, we simply multiply $v_{0x}$ by $T$:

$$R = v_{0x}T = v_{0x} \left( \frac{2v_{0y}}{g} \right)$$
*(Note: Using the trigonometric identity $2 \sin(\theta)\cos(\theta) = \sin(2\theta)$, this simplifies to the classic range equation: $R = \frac{v_0^2 \sin(2\theta)}{g}$)*

Plugging in our values to the exact formula:
$$R = \frac{(100)^2 \sin(2 \times 37^\circ)}{9.8} = \frac{10000 \sin(74^\circ)}{9.8}$$
$$R = \frac{10000(0.9613)}{9.8} \approx \frac{9612.6}{9.8} \approx 980.88 \text{ m}$$

*Visualization is available at [solution_01.html](solution_01.html)*