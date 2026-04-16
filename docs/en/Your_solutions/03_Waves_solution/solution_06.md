## 6. Wave Equation

A wave is described by the equation $y(x,t) = 0.05 \sin(2\pi x - 50\pi t)$, where x and y are in meters and t is in seconds. Determine the waves':

a) Amplitude $A$.

b) Wavelength $\lambda$.

c) Frequency $f$.

d) Wave speed $v$.

---


### **Variables & Units**

Before diving into the steps, let's define the standard variables used in the 1D traveling wave equation $y(x,t) = A \sin(kx - \omega t)$:

* **$y(x,t)$**: Displacement of the wave at a specific position $x$ and time $t$. Measured in meters (**m**).
* **$A$**: Amplitude, the maximum displacement from the equilibrium (middle) position. Measured in meters (**m**).
* **$k$**: Angular wavenumber, which relates to the spatial frequency of the wave. Measured in radians per meter (**rad/m**).
* **$\omega$**: Angular frequency, which relates to the time frequency of the wave. Measured in radians per second (**rad/s**).
* **$x$**: Position along the wave's path. Measured in meters (**m**).
* **$t$**: Time. Measured in seconds (**s**).
* **$\lambda$**: Wavelength, the distance over which the wave's shape repeats. Measured in meters (**m**).
* **$f$**: Frequency, the number of cycles per second. Measured in Hertz (**Hz** or $\text{s}^{-1}$).
* **$v$**: Wave speed, how fast the wave propagates through space. Measured in meters per second (**m/s**).

---

### **Step-by-Step Solution**

**1. Compare the given equation to the standard wave equation**
The standard equation for a wave traveling in the positive x-direction is:
$$y(x,t) = A \sin(kx - \omega t)$$

The problem gives us:
$$y(x,t) = 0.05 \sin(2\pi x - 50\pi t)$$

By matching the terms, we can extract our core constants:
* $A = 0.05$ m
* $k = 2\pi$ rad/m
* $\omega = 50\pi$ rad/s

**2. Determine the Amplitude (a)**
The amplitude is simply the coefficient in front of the sine function.
* **Answer:** $A = 0.05\text{ m}$

**3. Determine the Wavelength (b)**
The wavenumber $k$ is defined as $k = \frac{2\pi}{\lambda}$. We can rearrange this formula to solve for wavelength:
$$\lambda = \frac{2\pi}{k}$$
Substitute our known value for $k$:
$$\lambda = \frac{2\pi}{2\pi}$$
* **Answer:** $\lambda = 1\text{ m}$

**4. Determine the Frequency (c)**
The angular frequency $\omega$ is defined as $\omega = 2\pi f$. Rearrange to solve for regular frequency:
$$f = \frac{\omega}{2\pi}$$
Substitute our known value for $\omega$:
$$f = \frac{50\pi}{2\pi}$$
* **Answer:** $f = 25\text{ Hz}$

**5. Determine the Wave Speed (d)**
Wave speed can be found by multiplying the frequency by the wavelength ($v = f \cdot \lambda$), or by dividing the angular frequency by the wavenumber ($v = \frac{\omega}{k}$). Let's use $f \cdot \lambda$:
$$v = 25 \cdot 1$$
* **Answer:** $v = 25\text{ m/s}$
