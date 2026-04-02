## 8. Work of a variable force

Given a one-dimensional force:

$$
F(x)=-kx
$$

* Write down the equation of motion and solve it.
* Calculate the work done during the displacement from $0$ to $x_0$.
* Interpret the result as potential energy.
* Verify the relationship $F = -\frac{dU}{dx}$.
* Draw the graph of $F(x)$ and $U(x)$.

---

### Variable Definitions

Before we dive into the steps, here is a breakdown of the letters used in these equations and their standard units:

* **$F(x)$**: Force acting on the object at position $x$. Measured in Newtons (N).
* **$x$**: Displacement or position of the object from the equilibrium point. Measured in meters (m).
* **$x_0$**: A specific final displacement or position. Measured in meters (m).
* **$k$**: A positive proportionality constant (e.g., the spring constant). Measured in Newtons per meter (N/m).
* **$m$**: Mass of the object. Measured in kilograms (kg).
* **$t$**: Time. Measured in seconds (s).
* **$a$**: Acceleration of the object. Measured in meters per second squared (m/s²).
* **$W$**: Work done by the force. Measured in Joules (J).
* **$U(x)$**: Potential energy of the system at position $x$. Measured in Joules (J).
* **$\omega$**: Angular frequency of the resulting oscillation. Measured in radians per second (rad/s).
* **$A$**: Amplitude (maximum displacement) of the oscillation. Measured in meters (m).
* **$\phi$**: Phase constant, determined by initial conditions. Measured in radians (rad).

---

### Step-by-Step Solution



#### 1. Equation of Motion and its Solution

**Step 1: Apply Newton's Second Law.**
Newton's second law states that $F = ma$. In calculus terms, acceleration $a$ is the second derivative of position with respect to time ($a = \frac{d^2x}{dt^2}$).
$$m\frac{d^2x}{dt^2} = -kx$$

**Step 2: Rearrange into a standard differential equation.**
Divide both sides by mass $m$ and move all terms to one side:
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = 0$$

Let $\omega^2 = \frac{k}{m}$, where $\omega$ is the angular frequency. The equation becomes:
$$\frac{d^2x}{dt^2} + \omega^2x = 0$$

**Step 3: Solve the differential equation.**
This is a standard second-order linear ordinary differential equation describing Simple Harmonic Motion. The general solution is a sinusoidal function:
$$x(t) = A \cos(\omega t + \phi)$$
*(Note: $A$ and $\phi$ are constants determined by the system's initial position and velocity at $t=0$.)*

#### 2. Work Done During Displacement

**Step 1: Set up the work integral.**
The work $W$ done by a variable one-dimensional force $F(x)$ as an object moves from an initial position $x_i$ to a final position $x_f$ is defined by the integral:
$$W = \int_{x_i}^{x_f} F(x) dx$$

**Step 2: Substitute the force equation and limits.**
Our limits are from $0$ to $x_0$, and $F(x) = -kx$:
$$W = \int_{0}^{x_0} (-kx) dx$$

**Step 3: Integrate and evaluate.**
The antiderivative of $x$ is $\frac{1}{2}x^2$.
$$W = \left[ -\frac{1}{2}kx^2 \right]_{0}^{x_0}$$
$$W = -\frac{1}{2}kx_0^2 - \left( -\frac{1}{2}k(0)^2 \right)$$
$$W = -\frac{1}{2}kx_0^2$$
The negative sign indicates that the restoring force acts in the opposite direction to the displacement.

#### 3. Interpret as Potential Energy

**Step 1: Relate work to potential energy.**
For a conservative force, the work done by the force is equal to the negative change in potential energy ($\Delta U$):
$$W = -\Delta U = -(U(x_f) - U(x_i))$$

**Step 2: Apply the calculated work.**
Assuming the potential energy at the equilibrium position ($x = 0$) is zero, we set $U(0) = 0$.
$$W = -(U(x_0) - U(0)) = -U(x_0)$$

Substitute the work we found in the previous section:
$$-\frac{1}{2}kx_0^2 = -U(x_0)$$
$$U(x_0) = \frac{1}{2}kx_0^2$$

This means the general function for the potential energy of this system is:
$$U(x) = \frac{1}{2}kx^2$$

#### 4. Verify the Relationship $F = -\frac{dU}{dx}$

**Step 1: Differentiate the potential energy function.**
We want to show that the negative derivative of $U(x)$ gives us our original force $F(x)$.
$$-\frac{dU}{dx} = -\frac{d}{dx} \left( \frac{1}{2}kx^2 \right)$$

**Step 2: Apply the power rule.**
The derivative of $x^2$ is $2x$.
$$-\frac{dU}{dx} = -\frac{1}{2}k(2x)$$
$$-\frac{dU}{dx} = -kx$$

This exactly matches our initial given force $F(x) = -kx$, successfully verifying the relationship.

#### 5. Graphs of $F(x)$ and $U(x)$

While I cannot directly output an image file here, here is exactly how the graphs look:

* **Graph of $F(x) = -kx$:** This is a straight line passing through the origin $(0,0)$. Because of the negative sign, it has a negative slope ($-k$). It passes through the second quadrant (negative $x$, positive $F$) and the fourth quadrant (positive $x$, negative $F$).
* **Graph of $U(x) = \frac{1}{2}kx^2$:** This is a parabola that opens upwards. Its vertex (the lowest point) is at the origin $(0,0)$, representing the minimum potential energy at the equilibrium state.
