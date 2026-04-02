## 11. Dynamics with a time-dependent force

A particle of mass $m=3$ kg moves in a force field $F$ dependent on time in the following way:

$$
F = (15t, 3t-12, -6t^2) \, \text{N}
$$

Assuming initial conditions $r_0=(5,2,-3)$ m, $v_0=(2,0,1)$ m/s, find the dependence of the particle's position and velocity on time.

---

### Variable Definitions and Units

* **$m$**: Mass of the particle, measured in kilograms (kg).
* **$t$**: Time, measured in seconds (s).
* **$F$** or **$\vec{F}(t)$**: Force vector acting on the particle, measured in Newtons (N).
* **$\vec{a}(t)$**: Acceleration vector, measured in meters per second squared (m/s$^2$).
* **$\vec{v}(t)$**: Velocity vector, measured in meters per second (m/s).
* **$\vec{r}(t)$**: Position vector, measured in meters (m).
* **$\vec{r}_0$**: Initial position vector at $t=0$, measured in meters (m).
* **$\vec{v}_0$**: Initial velocity vector at $t=0$, measured in meters per second (m/s).

---

### Step-by-Step Solution

**Step 1: Determine the acceleration of the particle**
According to Newton's Second Law of Motion, the force acting on an object is equal to its mass times its acceleration ($\vec{F}=m\vec{a}$). We can rearrange this to solve for acceleration by dividing the force vector by the mass.
$$\vec{a}(t)=\frac{\vec{F}(t)}{m}$$

Given $m=3$ kg and $\vec{F}=(15t,3t-12,-6t^2)$, we divide each component of the force by 3:
$$\vec{a}(t)=\left(\frac{15t}{3},\frac{3t-12}{3},\frac{-6t^2}{3}\right)$$
$$\vec{a}(t)=(5t,t-4,-2t^2)$$

**Step 2: Determine the velocity vector as a function of time**
Acceleration is the derivative of velocity with respect to time ($\vec{a}=\frac{d\vec{v}}{dt}$). Therefore, velocity is the integral of acceleration. We integrate each component of the acceleration vector and use the initial velocity $\vec{v}_0=(2,0,1)$ to solve for the constants of integration ($C$).
$$\vec{v}(t)=\int\vec{a}(t)dt$$

* **X-component:**
    $$v_x(t)=\int5tdt=\frac{5}{2}t^2+C_x$$
    Using $v_{x0}=2$: $\frac{5}{2}(0)^2+C_x=2 \implies C_x=2$
    $$v_x(t)=\frac{5}{2}t^2+2$$

* **Y-component:**
    $$v_y(t)=\int(t-4)dt=\frac{1}{2}t^2-4t+C_y$$
    Using $v_{y0}=0$: $\frac{1}{2}(0)^2-4(0)+C_y=0 \implies C_y=0$
    $$v_y(t)=\frac{1}{2}t^2-4t$$

* **Z-component:**
    $$v_z(t)=\int-2t^2dt=-\frac{2}{3}t^3+C_z$$
    Using $v_{z0}=1$: $-\frac{2}{3}(0)^3+C_z=1 \implies C_z=1$
    $$v_z(t)=-\frac{2}{3}t^3+1$$

**Final Velocity Equation:**
$$\vec{v}(t)=\left(\frac{5}{2}t^2+2,\frac{1}{2}t^2-4t,-\frac{2}{3}t^3+1\right)\text{ m/s}$$

**Step 3: Determine the position vector as a function of time**
Velocity is the derivative of position with respect to time ($\vec{v}=\frac{d\vec{r}}{dt}$). Therefore, position is the integral of velocity. We integrate each component of the velocity vector and use the initial position $\vec{r}_0=(5,2,-3)$ to solve for the new constants of integration.
$$\vec{r}(t)=\int\vec{v}(t)dt$$

* **X-component:**
    $$x(t)=\int\left(\frac{5}{2}t^2+2\right)dt=\frac{5}{6}t^3+2t+C_x$$
    Using $x_0=5$: $C_x=5$
    $$x(t)=\frac{5}{6}t^3+2t+5$$

* **Y-component:**
    $$y(t)=\int\left(\frac{1}{2}t^2-4t\right)dt=\frac{1}{6}t^3-2t^2+C_y$$
    Using $y_0=2$: $C_y=2$
    $$y(t)=\frac{1}{6}t^3-2t^2+2$$

* **Z-component:**
    $$z(t)=\int\left(-\frac{2}{3}t^3+1\right)dt=-\frac{2}{12}t^4+t+C_z=-\frac{1}{6}t^4+t+C_z$$
    Using $z_0=-3$: $C_z=-3$
    $$z(t)=-\frac{1}{6}t^4+t-3$$

**Final Position Equation:**
$$\vec{r}(t)=\left(\frac{5}{6}t^3+2t+5,\frac{1}{6}t^3-2t^2+2,-\frac{1}{6}t^4+t-3\right)\text{ m}$$
