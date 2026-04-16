## 3. Superposition Principle

Two waves are described by the equations $y_1(x, t) = A \sin(kx - \omega t)$ and $y_2(x, t) = A \sin(kx + \omega t)$. What is the equation of the resulting standing wave? Identify the positions of the nodes.

---

### **Variables and Units**

Before doing the math, here is a breakdown of the symbols used in these wave equations:

* **$y$ (Displacement):** The vertical position of a particle in the medium at a specific location and time. Measured in **meters (m)**.
* **$x$ (Position):** The horizontal location along the wave. Measured in **meters (m)**.
* **$t$ (Time):** The time at which the wave is being observed. Measured in **seconds (s)**.
* **$A$ (Amplitude):** The maximum displacement of the original traveling waves. Measured in **meters (m)**.
* **$k$ (Angular Wavenumber):** Relates to the spatial frequency of the wave ($k = 2\pi/\lambda$). Measured in **radians per meter (rad/m)**.
* **$\omega$ (Angular Frequency):** Relates to the temporal frequency of the wave ($\omega = 2\pi f$). Measured in **radians per second (rad/s)**.
* **$\lambda$ (Wavelength):** The distance over which the wave's shape repeats. Measured in **meters (m)**.
* **$n$ (Integer):** A whole number used to denote the sequence of nodes ($0, 1, 2, 3...$). Dimensionless.

---

### **Step-by-Step Solution**

**Step 1: Understand the starting equations**
We are given two waves traveling through the same medium:
* $y_1(x, t) = A \sin(kx - \omega t)$  *(A wave traveling in the positive $x$-direction)*
* $y_2(x, t) = A \sin(kx + \omega t)$  *(A wave traveling in the negative $x$-direction)*

**Step 2: Apply the Superposition Principle**
The superposition principle states that when two or more waves overlap in space, the resultant disturbance ($y$) is equal to the algebraic sum of the individual disturbances:
$$y(x, t) = y_1(x, t) + y_2(x, t)$$
$$y(x, t) = A \sin(kx - \omega t) + A \sin(kx + \omega t)$$

**Step 3: Use trigonometric identities to simplify**
To combine these terms, we use the sum-to-product trigonometric identity:
$$\sin(\alpha) + \sin(\beta) = 2 \sin\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)$$

Let $\alpha = kx - \omega t$ and $\beta = kx + \omega t$.
Calculate the sum and difference components:
* **Sum:** $\frac{\alpha + \beta}{2} = \frac{(kx - \omega t) + (kx + \omega t)}{2} = \frac{2kx}{2} = kx$
* **Difference:** $\frac{\alpha - \beta}{2} = \frac{(kx - \omega t) - (kx + \omega t)}{2} = \frac{-2\omega t}{2} = -\omega t$

**Step 4: Write the final equation for the standing wave**
Substitute these back into the identity:
$$y(x, t) = 2A \sin(kx) \cos(-\omega t)$$

Because cosine is an even function, $\cos(-\theta) = \cos(\theta)$, we can drop the negative sign to get the final equation of the standing wave:
$$y(x, t) = 2A \sin(kx) \cos(\omega t)$$

**Step 5: Identify the positions of the nodes**
Nodes are points on the standing wave that *never* move. This happens when the resulting displacement $y(x, t)$ is always zero, regardless of time ($t$). Looking at our standing wave equation, this occurs when the spatial part of the amplitude is zero:
$$\sin(kx) = 0$$

The sine function is zero at integer multiples of $\pi$:
$$kx = n\pi \quad \text{for} \quad n = 0, 1, 2, \dots$$

Since we know that $k = \frac{2\pi}{\lambda}$, we can substitute $k$ to solve for $x$:
$$\left(\frac{2\pi}{\lambda}\right) x = n\pi$$
$$x = \frac{n\pi \lambda}{2\pi}$$
$$x = \frac{n\lambda}{2} \quad \text{for} \quad n = 0, 1, 2, \dots$$

The nodes are located at $x = 0, \frac{\lambda}{2}, \lambda, \frac{3\lambda}{2}$, and so on.