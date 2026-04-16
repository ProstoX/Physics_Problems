## 10. Force field and power

In a certain force field, the equations of motion of a particle with mass $m=0.5$ kg are as follows:

$$
x = 5t^2 - t, \quad y = 2t^3, \quad z = -3t + 2
$$

$$
\vec{r}(t) = [5t^2 - t, 2t^3, -3t + 2]
$$

Find the time dependence of: the particle's velocity, the particle's momentum, the particle's acceleration, the force acting on the particle, and the power transferred by the field to the particle.

---

### Step-by-Step Solution

**Step 1: Find the particle's velocity**
Velocity is the first derivative of the position with respect to time. We need to differentiate each coordinate function $x(t)$, $y(t)$, and $z(t)$ with respect to $t$.
* $v_x = \frac{dx}{dt} = \frac{d}{dt}(5t^2 - t) = 10t - 1$
* $v_y = \frac{dy}{dt} = \frac{d}{dt}(2t^3) = 6t^2$
* $v_z = \frac{dz}{dt} = \frac{d}{dt}(-3t + 2) = -3$

The time dependence of the velocity vector is:
$$
\vec{v}(t) = [10t - 1, 6t^2, -3]
$$

**Step 2: Find the particle's momentum**
Momentum is the product of the particle's mass and its velocity vector ($\vec{p} = m\vec{v}$). We multiply each component of the velocity vector by the mass $m = 0.5$.
* $p_x = 0.5 \cdot (10t - 1) = 5t - 0.5$
* $p_y = 0.5 \cdot (6t^2) = 3t^2$
* $p_z = 0.5 \cdot (-3) = -1.5$

The time dependence of the momentum vector is:
$$
\vec{p}(t) = [5t - 0.5, 3t^2, -1.5]
$$

**Step 3: Find the particle's acceleration**
Acceleration is the first derivative of velocity with respect to time (or the second derivative of position). We differentiate the velocity components.
* $a_x = \frac{dv_x}{dt} = \frac{d}{dt}(10t - 1) = 10$
* $a_y = \frac{dv_y}{dt} = \frac{d}{dt}(6t^2) = 12t$
* $a_z = \frac{dv_z}{dt} = \frac{d}{dt}(-3) = 0$

The time dependence of the acceleration vector is:
$$
\vec{a}(t) = [10, 12t, 0]
$$

**Step 4: Find the force acting on the particle**
According to Newton's Second Law, force is the product of mass and acceleration ($\vec{F} = m\vec{a}$).
* $F_x = 0.5 \cdot 10 = 5$
* $F_y = 0.5 \cdot 12t = 6t$
* $F_z = 0.5 \cdot 0 = 0$

The time dependence of the force vector is:
$$
\vec{F}(t) = [5, 6t, 0]
$$

**Step 5: Find the power transferred by the field**
Power is the dot product of the force vector and the velocity vector ($P = \vec{F} \cdot \vec{v}$).
* $P(t) = F_x \cdot v_x + F_y \cdot v_y + F_z \cdot v_z$
* $P(t) = 5(10t - 1) + 6t(6t^2) + 0(-3)$
* $P(t) = 50t - 5 + 36t^3$

Rearranging the terms, the time dependence of the power is:
$$
P(t) = 36t^3 + 50t - 5
$$