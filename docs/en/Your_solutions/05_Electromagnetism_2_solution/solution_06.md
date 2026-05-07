## 6. EM Wave Analysis

An electromagnetic wave has its electric field component described by $E_y(x,t) = 100 \sin(10^7 x - \omega t) \text{ V/m}$. What is the direction of propagation? What is the wavelength $\lambda$? What is the angular frequency $\omega$? What is the equation for the magnetic field component?

---

### Variables and Units

Before diving into the solution, here is a quick breakdown of the symbols used in this problem and their standard SI units:

*   **$E_y$**: The electric field component along the y-axis, measured in **Volts per meter (V/m)**.
*   **$x$**: Spatial position along the axis of propagation, measured in **meters (m)**.
*   **$t$**: Time, measured in **seconds (s)**.
*   **$\omega$** (omega): Angular frequency, representing the rate of oscillation, measured in **radians per second (rad/s)**.
*   **$k$**: Angular wave number, representing the spatial frequency of the wave, measured in **radians per meter (rad/m)**.
*   **$\lambda$** (lambda): Wavelength, the physical distance over which the wave's shape repeats, measured in **meters (m)**.
*   **$c$**: The speed of light in a vacuum, approximately **$3 \times 10^8$ m/s**.
*   **$B_z$**: The magnetic field component along the z-axis, measured in **Tesla (T)**.

---

### Step-by-Step Solution

The general equation for a plane electromagnetic wave traveling in a vacuum is given by:
$$E(x,t) = E_0 \sin(kx \pm \omega t)$$

Comparing this to your specific equation, $E_y(x,t) = 100 \sin(10^7 x - \omega t)$, we can extract the following given values:
*   Amplitude ($E_0$) = **100 V/m**
*   Wave number ($k$) = **$10^7$ rad/m**

#### 1. Direction of Propagation
The phase term of the sine function is $(10^7 x - \omega t)$. 
*   **Rule:** When the spatial term ($kx$) and the temporal term ($\omega t$) have opposite signs (one positive, one negative), the wave propagates in the positive direction of the spatial axis. 
*   **Answer:** The wave is propagating in the **positive x-direction ($+x$)**.

#### 2. Wavelength ($\lambda$)
The wave number $k$ is related to the wavelength by the formula $k = \frac{2\pi}{\lambda}$.
*   Rearranging for wavelength: $\lambda = \frac{2\pi}{k}$
*   Substitute $k = 10^7$: 
    $$\lambda = \frac{2\pi}{10^7} \approx 6.28 \times 10^{-7} \text{ m}$$
*   **Answer:** The wavelength is approximately **628 nm** (which falls in the visible red light spectrum).

#### 3. Angular Frequency ($\omega$)
For electromagnetic waves in a vacuum, the angular frequency and wave number are related by the speed of light: $c = \frac{\omega}{k}$.
*   Rearranging for angular frequency: $\omega = c \cdot k$
*   Substitute $c = 3 \times 10^8 \text{ m/s}$ and $k = 10^7 \text{ rad/m}$:
    $$\omega = (3 \times 10^8) \times 10^7 = 3 \times 10^{15} \text{ rad/s}$$
*   **Answer:** The angular frequency is **$3 \times 10^{15}$ rad/s**.

#### 4. Equation for the Magnetic Field Component
In an electromagnetic wave, the electric field ($\vec{E}$), magnetic field ($\vec{B}$), and direction of propagation ($\vec{v}$) are all mutually perpendicular.
*   **Amplitude:** The magnitude of the magnetic field relates to the electric field by $B_0 = \frac{E_0}{c}$.
    $$B_0 = \frac{100}{3 \times 10^8} \approx 3.33 \times 10^{-7} \text{ T}$$
*   **Direction:** We use the right-hand rule, where $\vec{E} \times \vec{B}$ points in the direction of propagation. 
    *   $\vec{E}$ is in the $+y$ direction ($\hat{j}$).
    *   The wave travels in the $+x$ direction ($\hat{i}$).
    *   Since $\hat{j} \times \hat{k} = \hat{i}$, the magnetic field must be in the $+z$ direction ($\hat{k}$).
*   **Answer:** The magnetic field is perfectly in phase with the electric field. Its equation is:
    $$B_z(x,t) = 3.33 \times 10^{-7} \sin(10^7 x - 3 \times 10^{15} t) \text{ T}$$