## 10. Animation: Wave Sources

Write an HTML animation in which it is possible to place dots that will serve as sources of waves described by the equation:

$$
u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_0}|^\alpha} \sin(k |\vec{r} - \vec{r_0}| - \omega t)
$$

where $\vec{r_0}$ is the position of the dot, and $\alpha$ is a parameter that can be set within the range $[0, 2]$. The animation should show the superposition of waves from all dots.

---

### Step-by-Step Solution

**1. Variable Definitions and Units**

Let's begin by defining each term in the provided equation and the standard SI units typically used:

* **$u(\vec{r}, t)$**: Displacement of the wave at position $\vec{r}$ and time $t$. Units: Depends on the physical type of wave (e.g., meters for a displacement wave, Pascals for a pressure wave, Volts per meter for an electric field). Let's define this as displacement in **meters (m)**.
* **$\vec{r}$**: Position vector, representing the coordinates where the wave is being measured (e.g., $(x, y)$ on a plane or $(x, y, z)$ in space). Units: **meters (m)**.
* **$\vec{r_0}$**: Position vector of the wave source (the "dot"). Units: **meters (m)**.
* **$|\vec{r}-\vec{r_0}|$**: The magnitude of the displacement vector, which is the direct distance from the source to the measuring point. Units: **meters (m)**.
* **$A$**: The source amplitude. Units: **meters (m)** (must match $u$).
* **$\alpha$**: Attenuation parameter, controlling how quickly the wave's intensity drops with distance. Units: **Dimensionless**. Range $[0, 2]$.
* **$k$**: Angular wavenumber. It is related to wavelength ($\lambda$) by $k = \frac{2\pi}{\lambda}$. Units: **radians per meter (rad/m)**.
* **$\omega$**: Angular frequency. It is related to frequency ($f$) by $\omega = 2\pi f$. Units: **radians per second (rad/s)**.
* **$t$**: Time. Units: **seconds (s)**.
* **$\sin(...)$**: The oscillating phase function that creates the wave shape. Units: **Dimensionless**.

**2. Physical Interpretation and the Parameter $\alpha$**

The equation describes an expanding wavefront originating from a point source at $\vec{r_0}$.

The amplitude term is $\frac{A}{|\vec{r}-\vec{r_0}|^\alpha}$. This shows that the amplitude decreases as the distance from the source increases. The specific physical reality depends on the parameter $\alpha$:

* **$\alpha = 0$**: $\frac{A}{1} = A$. The amplitude is constant everywhere, regardless of distance. This is a non-physical simplification, a standard uniform plane wave.
* **$\alpha = 1$**: The amplitude drops off as $\frac{1}{\text{distance}}$. This is the standard behavior of a **circular wave expanding in a 2D plane**. (Energy is spread over a circumference which grows with distance).
* **$\alpha = 2$**: The amplitude drops off as $\frac{1}{\text{distance}^2}$. This is the behavior of a **spherical wave expanding in 3D space**. (Energy is spread over the surface of a sphere, which grows with the square of the distance).

The range $[0, 2]$ allows you to simulate anything from perfect transmission (no attenuation) up to standard spatial expansion.

**3. Superposition Principle and Numerical Implementation**

The key to visualizing the interference is the principle of superposition. It states that the total wave disturbance at any point is the vector sum of the disturbances from each individual source.

In 2D, the total displacement $u_{total}(x, y, t)$ is the sum of the wave functions for all $N$ placed sources:

$$
u_{total}(x, y, t) = \sum_{i=1}^{N} u_i(x, y, t) = \sum_{i=1}^{N} \frac{A_i}{d_i^\alpha} \sin(k_i d_i - \omega_i t)
$$

where $d_i = \sqrt{(x-x_{0,i})^2 + (y-y_{0,i})^2}$ is the distance from measuring pixel $(x, y)$ to source $(x_{0,i}, y_{0,i})$.

To create the visualization, a program must:
1. Define a 2D grid (canvas).
2. Maintain a list of placed sources with their $(\vec{r_0}, A, k, \omega)$ properties.
3. Use sliders to control the global $\alpha$ (and potentially other properties).
4. For every frame in the animation and for *every pixel* on the grid:
    a. Reset the total value to 0.
    b. Loop through *all* placed sources.
    c. Calculate that source's specific contribution using the equation.
    d. Add it to the total.
5. Convert the resulting $u_{total}$ value for that pixel into a corresponding color intensity (bright for high values, dark for low) to display the "ripple tank" effect.