## 2. Harmonic Motion

A 10 kg mass is attached to a spring and oscillates according to the equation $x(t) = 0.2 \cos(10\pi t)$ (in meters). What is the spring constant $k$? What is the total mechanical energy of the system?

---

### Variable Definitions

Before proceeding with the calculations, here is a breakdown of the variables used in simple harmonic motion (SHM) equations:

* **$x(t)$**: The position or displacement of the mass at a specific time $t$. Measured in meters (m).
* **$A$**: The amplitude, which is the maximum displacement from the equilibrium (resting) position. Measured in meters (m).
* **$\omega$**: The angular frequency, representing how fast the oscillation occurs. Measured in radians per second (rad/s).
* **$t$**: The time elapsed. Measured in seconds (s).
* **$k$**: The spring constant, representing the stiffness of the spring. Measured in Newtons per meter (N/m).
* **$m$**: The mass of the object attached to the spring. Measured in kilograms (kg).
* **$E$**: The total mechanical energy of the system. Measured in Joules (J).

---

### Part 1: Finding the Spring Constant ($k$)

**Goal:** Determine the spring constant $k$ given a mass of **10 kg** and the position equation $x(t) = 0.2 \cos(10\pi t)$.

**Step 1: Identify known values from the standard SHM equation.**
The standard equation for the position of an object in simple harmonic motion is:
$$x(t) = A \cos(\omega t)$$

By comparing the standard equation to the given equation $x(t) = 0.2 \cos(10\pi t)$, we can extract the following parameters:
* Amplitude ($A$) = **0.2 m**
* Angular frequency ($\omega$) = **$10\pi$ rad/s**
* Mass ($m$) = **10 kg**

**Step 2: State the formula relating angular frequency to the spring constant.**
The angular frequency $\omega$ of a mass-spring system is defined by the formula:
$$\omega = \sqrt{\frac{k}{m}}$$

**Step 3: Rearrange the formula to solve for $k$.**
Square both sides of the equation to remove the square root:
$$\omega^2 = \frac{k}{m}$$

Multiply both sides by $m$ to isolate $k$:
$$k = m \cdot \omega^2$$

**Step 4: Substitute the known values and calculate.**
$$k = 10 \cdot (10\pi)^2$$
$$k = 10 \cdot 100\pi^2$$
$$k = 1000\pi^2$$

**Answer:** The exact spring constant is **$1000\pi^2$ N/m**. If you calculate the numerical approximation ($\pi \approx 3.14159$), the spring constant is approximately **9869.6 N/m**.

---

### Part 2: Finding the Total Mechanical Energy ($E$)

**Goal:** Calculate the total mechanical energy of the oscillating mass-spring system. 

**Step 1: State the formula for total mechanical energy.**
In an ideal simple harmonic oscillator (ignoring friction and air resistance), the total mechanical energy is conserved and is equal to the maximum potential energy stored in the spring at its peak amplitude.
$$E = \frac{1}{2}kA^2$$

**Step 2: Substitute the known values into the formula.**
We know $k = 1000\pi^2$ and $A = 0.2$.
$$E = \frac{1}{2} \cdot (1000\pi^2) \cdot (0.2)^2$$

**Step 3: Calculate the final energy.**
First, square the amplitude: $(0.2)^2 = 0.04$
$$E = \frac{1}{2} \cdot 1000\pi^2 \cdot 0.04$$
$$E = 500\pi^2 \cdot 0.04$$
$$E = 20\pi^2$$

**Answer:** The exact total mechanical energy of the system is **$20\pi^2$ Joules**. Numerically, this is approximately **197.4 Joules**.