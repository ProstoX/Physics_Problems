## 8. Waves

Which of the following functions can describe a traveling wave? Hint: check if it satisfies the wave equation 

$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$

a) $y(x,t) = A \cos(kx^2 - \omega t)$

b) $y(x,t) = A(x-vt)^2$

c) $y(x,t) = A \log(x+vt)$

---


### Understanding the Variables

Before diving into the math, let's break down the variables used in these equations and their standard SI units:

* **$y$**: The displacement of the wave from its equilibrium position (Units: meters, m).
* **$x$**: The spatial position along the axis the wave is traveling (Units: meters, m).
* **$t$**: Time (Units: seconds, s).
* **$v$**: The velocity or speed of the wave (Units: meters per second, m/s).
* **$A$**: The amplitude or scaling constant of the wave (Units: typically meters, m, though it can vary based on the specific function's dimensions).
* **$k$**: The wave number, related to the spatial period (Units: radians per meter, rad/m).
* **$\omega$**: The angular frequency, related to the time period (Units: radians per second, rad/s).

**The Wave Equation**
The standard 1D wave equation is a partial differential equation given by:
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$
Any mathematically valid traveling wave must satisfy this equation. Additionally, according to d'Alembert's solution, any function of the form $f(x - vt)$ (traveling right) or $f(x + vt)$ (traveling left) will satisfy this equation.

---

### Step-by-Step Solutions

#### a) $y(x,t) = A \cos(kx^2 - \omega t)$

Let's find the second partial derivatives with respect to $x$ and $t$.

1.  **First derivative with respect to $x$:**
    $$\frac{\partial y}{\partial x} = -A \sin(kx^2 - \omega t) \cdot (2kx) = -2Akx \sin(kx^2 - \omega t)$$
2.  **Second derivative with respect to $x$:**
    Use the product rule:
    $$\frac{\partial^2 y}{\partial x^2} = -2Ak \sin(kx^2 - \omega t) - 4Ak^2x^2 \cos(kx^2 - \omega t)$$
3.  **First derivative with respect to $t$:**
    $$\frac{\partial y}{\partial t} = -A \sin(kx^2 - \omega t) \cdot (-\omega) = A\omega \sin(kx^2 - \omega t)$$
4.  **Second derivative with respect to $t$:**
    $$\frac{\partial^2 y}{\partial t^2} = A\omega \cos(kx^2 - \omega t) \cdot (-\omega) = -A\omega^2 \cos(kx^2 - \omega t)$$

**Conclusion for (a):**
If we plug these into the wave equation, $\frac{\partial^2 y}{\partial x^2}$ contains both a sine term and an $x^2$ cosine term, whereas $\frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$ only contains a constant multiple of a cosine term. Because the spatial derivative introduces extra $x$ variables that cannot be balanced out, they are not equal. 
**Result: Function (a) is NOT a traveling wave.**

---

#### b) $y(x,t) = A(x-vt)^2$

Let's test this function using the same method.

1.  **Derivatives with respect to $x$:**
    $$\frac{\partial y}{\partial x} = 2A(x-vt) \cdot (1) = 2A(x-vt)$$
    $$\frac{\partial^2 y}{\partial x^2} = 2A$$
2.  **Derivatives with respect to $t$:**
    $$\frac{\partial y}{\partial t} = 2A(x-vt) \cdot (-v) = -2Av(x-vt)$$
    $$\frac{\partial^2 y}{\partial t^2} = -2Av \cdot (-v) = 2Av^2$$

**Conclusion for (b):**
Plug the second derivatives into the wave equation:
$$2A = \frac{1}{v^2} (2Av^2)$$
$$2A = 2A$$
The equation holds true perfectly. Notice that this function is in the form $f(x-vt)$, which describes a parabolic shape moving in the positive $x$ direction at speed $v$.
**Result: Function (b) IS a valid traveling wave.**

---

#### c) $y(x,t) = A \log(x+vt)$

*Note: In mathematics and physics, $\log$ usually denotes the natural logarithm $\ln$.*

1.  **Derivatives with respect to $x$:**
    $$\frac{\partial y}{\partial x} = A \frac{1}{x+vt} \cdot (1) = \frac{A}{x+vt}$$
    $$\frac{\partial^2 y}{\partial x^2} = -A (x+vt)^{-2} = -\frac{A}{(x+vt)^2}$$
2.  **Derivatives with respect to $t$:**
    $$\frac{\partial y}{\partial t} = A \frac{1}{x+vt} \cdot (v) = \frac{Av}{x+vt}$$
    $$\frac{\partial^2 y}{\partial t^2} = -Av (x+vt)^{-2} \cdot (v) = -\frac{Av^2}{(x+vt)^2}$$

**Conclusion for (c):**
Plug these into the wave equation:
$$-\frac{A}{(x+vt)^2} = \frac{1}{v^2} \left( -\frac{Av^2}{(x+vt)^2} \right)$$
$$-\frac{A}{(x+vt)^2} = -\frac{A}{(x+vt)^2}$$
The equation holds perfectly. This function is in the form $f(x+vt)$, which means it describes a wave moving in the negative $x$ direction (to the left) at speed $v$. *(Note: While mathematically valid for the wave equation, physically it has an asymptote at $x = -vt$, meaning the amplitude goes to infinity at that point).*
**Result: Function (c) IS a valid traveling wave.**