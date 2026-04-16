## 11. Animation: Two-Slit Interference

Write an HTML animation simulating Young's experiment, in which two slits act as point sources of coherent waves. The displacement of the resultant wave is the sum of partial waves described by the formula:

$$
u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_1}|} \sin(k |\vec{r} - \vec{r_1}| - \omega t) + \frac{A}{|\vec{r}-\vec{r_2}|} \sin(k |\vec{r} - \vec{r_2}| - \omega t)
$$

where $\vec{r_1}$ and $\vec{r_2}$ are the position vectors of the slits. The user should be able to change the distance between the slits $d = |\vec{r_1} - \vec{r_2}|$ and the wavelength $\lambda$. The animation should visualize the resulting interference pattern in real time.

---


### Variables and Units

Before solving or simulating, let's define the variables in the equation and their standard SI units:

* **$u(\vec{r},t)$**: The net displacement of the wave at a specific observation point $\vec{r}$ and at time $t$. (Units: meters, m)
* **$\vec{r}$**: The position vector $(x, y)$ of the point where we are measuring the wave. (Units: meters, m)
* **$\vec{r_1}, \vec{r_2}$**: The position vectors of Slit 1 and Slit 2. These act as our two coherent point sources. (Units: meters, m)
* **$|\vec{r} - \vec{r_1}|$**: The absolute distance from Slit 1 to the observation point. Let's call this $R_1$. (Units: meters, m)
* **$|\vec{r} - \vec{r_2}|$**: The absolute distance from Slit 2 to the observation point. Let's call this $R_2$. (Units: meters, m)
* **$A$**: The amplitude constant of the wave at the source. (Units: strictly $m^2$ in this specific formula to ensure $u$ results in meters, though often treated generically).
* **$k$**: The angular wavenumber, which tells us how many radians the wave cycles through per meter. It is inversely proportional to wavelength: $k = \frac{2\pi}{\lambda}$. (Units: radians per meter, rad/m)
* **$\lambda$**: The wavelength of the wave. (Units: meters, m)
* **$\omega$**: The angular frequency, telling us how many radians the wave cycles through per second. (Units: radians per second, rad/s)
* **$d$**: The distance between the two slits, $d = |\vec{r_1} - \vec{r_2}|$. (Units: meters, m)
* **$t$**: Time. (Units: seconds, s)

---

### Step-by-Step Explanation

**Step 1: Understand the single point source**
If we only had one slit (say, $\vec{r_1}$), the wave expanding from it in two dimensions would be described by $u_1 = \frac{A}{R_1} \sin(k R_1 - \omega t)$. The $1/R_1$ term dictates that the wave's amplitude decreases as it spreads out (energy conservation), and the sine term dictates the alternating peaks and troughs propagating outward over time.

**Step 2: Apply the Principle of Superposition**
When a single plane wave hits a barrier with two slits, Huygens' Principle states that each slit becomes a new point source. Because they originate from the same initial wave, they are *coherent* (they have the same frequency $\omega$ and a constant phase relationship). The Principle of Superposition states that the total wave displacement at any point $\vec{r}$ is simply the algebraic sum of the displacements from the individual waves:
$$u_{total} = u_1 + u_2$$

**Step 3: The Role of Wavelength and Wavenumber**
The user controls the wavelength $\lambda$. Because $k = \frac{2\pi}{\lambda}$, changing $\lambda$ changes $k$. A smaller wavelength increases $k$, which packs the ripples closer together. 

**Step 4: Interference Patterns (Path Difference)**
The most critical factor in this equation is the *path difference*, $\Delta R = R_2 - R_1$. 
* **Constructive Interference:** When $\Delta R$ is an integer multiple of the wavelength ($n\lambda$), the sine waves arrive "in phase" (peak meets peak). They add together to create a bright spot (maximum amplitude).
* **Destructive Interference:** When $\Delta R$ is a half-integer multiple of the wavelength ($(n + 0.5)\lambda$), the waves arrive "out of phase" (peak meets trough). They cancel each other out, creating a dark spot (zero amplitude).
Changing the slit distance $d$ alters the geometry of $R_1$ and $R_2$, directly altering where these constructive and destructive bands appear.
