### Variables and Units Glossary

Before we dive into the math, let's break down the symbols used in the equation and their standard SI units. Note that in this specific textbook problem, the constant $b$ is doing double-duty with mixed dimensions, which is common in abstract math problems but worth noting!

* **$t$ (Time):** The independent variable representing elapsed time. Measured in seconds (s).
* **$t_0$ (Final Time):** A specific point in time marking the end of the interval. Measured in seconds (s).
* **$\vec{r}(t)$ (Position Vector):** A 3D vector pointing from the origin to the particle's location at time $t$. Measured in meters (m).
* **$x(t), y(t), z(t)$ (Spatial Coordinates):** The individual horizontal, vertical, and depth positions. Measured in meters (m).
* **$a$ (X-Amplitude):** A positive constant representing the maximum stretch of the trajectory along the x-axis. Measured in meters (m).
* **$b$ (Y-Amplitude / Z-Velocity):** A positive constant. In the y-component ($b \sin(\omega t)$), it acts as a length measured in meters (m). In the z-component ($bt$), it acts as a constant vertical velocity measured in meters per second (m/s).
* **$\omega$ (Angular Frequency):** The rate at which the point rotates around the z-axis. Measured in radians per second (rad/s).
* **$\vec{v}(t)$ (Velocity Vector):** The rate of change of the position vector. Measured in meters per second (m/s).
* **$S$ (Path Length):** The total distance traveled along the curve. Measured in meters (m).



---

### Step-by-Step Solution

#### a) Find the equation of the point's trajectory

The position vector gives us the parametric equations for the three spatial coordinates:
1.  $x = a \cos(\omega t)$
2.  $y = b \sin(\omega t)$
3.  $z = bt$

To find the physical trajectory (the curve in 3D space independent of time), we need to eliminate the parameter $t$. First, let's look at the $x$ and $y$ coordinates. We can isolate the trigonometric functions by dividing by the amplitudes:
$$\frac{x}{a} = \cos(\omega t)$$
$$\frac{y}{b} = \sin(\omega t)$$

Squaring both equations and adding them together allows us to use the Pythagorean identity ($\sin^2(\theta) + \cos^2(\theta) = 1$):
$$\left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = \cos^2(\omega t) + \sin^2(\omega t)$$
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

This tells us that the entire trajectory is constrained to the surface of an **elliptical cylinder** extending along the z-axis. 

To define the exact curve on this cylinder, we isolate $t$ from the z-equation ($t = z/b$) and substitute it back into the x and y equations:
$$x(z) = a \cos\left(\frac{\omega z}{b}\right)$$
$$y(z) = b \sin\left(\frac{\omega z}{b}\right)$$

This pair of equations completely defines the trajectory as an **elliptical helix** spiraling upward along the z-axis.

#### b) Compute the path length of the point from time $t=0$ to $t=t_0$

Path length (or arc length) is the integral of the particle's speed over time.
$$S = \int_{0}^{t_0} |\vec{v}(t)| \, dt$$

First, we find the velocity vector by taking the derivative of the position vector $\vec{r}(t)$ with respect to time:
$$v_x(t) = \frac{d}{dt}(a \cos(\omega t)) = -a\omega \sin(\omega t)$$
$$v_y(t) = \frac{d}{dt}(b \sin(\omega t)) = b\omega \cos(\omega t)$$
$$v_z(t) = \frac{d}{dt}(bt) = b$$
$$\vec{v}(t) = (-a\omega \sin(\omega t), b\omega \cos(\omega t), b)$$

Next, calculate the speed $|\vec{v}(t)|$ (the magnitude of the velocity vector):
$$|\vec{v}(t)| = \sqrt{v_x^2 + v_y^2 + v_z^2}$$
$$|\vec{v}(t)| = \sqrt{a^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2}$$

Now, plug this into the integral:
$$S = \int_{0}^{t_0} \sqrt{a^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2} \, dt$$

**Note on this integral:** Because $a$ and $b$ are different constants, the $\sin^2$ and $\cos^2$ terms do not simply combine. This results in an *incomplete elliptic integral of the second kind*. It cannot be solved to yield a simple, closed-form equation using standard elementary functions, so leaving it in this exact integral form is the mathematically correct answer for the general case.

#### c) Discuss special cases

The general trajectory is an elliptical helix, but interesting things happen when we tweak the constants:

* **Special Case 1: $a = b$**
    If the amplitudes are equal, the elliptical cylinder becomes a perfect circular cylinder ($x^2 + y^2 = a^2$). The trajectory becomes a standard **circular helix**. 
    This beautifully simplifies our path length integral from part (b). If $a = b$, the terms under the square root become:
    $$b^2\omega^2 \sin^2(\omega t) + b^2\omega^2 \cos^2(\omega t) + b^2$$
    We factor out $b^2\omega^2$:
    $$b^2\omega^2 (\sin^2(\omega t) + \cos^2(\omega t)) + b^2 = b^2\omega^2(1) + b^2$$
    The speed is now entirely constant! The path length simply becomes speed multiplied by time:
    $$S = \int_{0}^{t_0} \sqrt{b^2\omega^2 + b^2} \, dt = t_0 \sqrt{b^2\omega^2 + b^2}$$

* **Special Case 2: $\omega \to 0$**
    If the angular frequency approaches 0, the particle stops oscillating. $\cos(0) = 1$ and $\sin(0) = 0$, so the position becomes $\vec{r}(t) = (a, 0, bt)$. The trajectory flattens out into a **straight vertical line** moving parallel to the z-axis at a constant distance $a$ from the origin.


*Visualization is available at [solution_10.html](solution_10.html)*