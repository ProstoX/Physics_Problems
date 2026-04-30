##  7. Cyclotron Motion

An electron is accelerated from rest through a potential difference of 5000 V. It then enters a region of uniform magnetic field B = 0.1 T, perpendicular to its velocity. What is the radius of the circular path it will follow?

---

### **Variable & Unit Breakdown**

*   **$q$ (Charge):** The electric charge of the particle (for an electron, this is the elementary charge). Measured in **Coulombs (C)**.
*   **$V$ (Voltage/Potential Difference):** The difference in electric potential that accelerates the electron. Measured in **Volts (V)**.
*   **$m$ (Mass):** The resting mass of the particle. Measured in **kilograms (kg)**.
*   **$v$ (Velocity):** The speed of the particle in a specific direction after acceleration. Measured in **meters per second (m/s)**.
*   **$B$ (Magnetic Field):** The strength of the uniform magnetic field the particle enters. Measured in **Teslas (T)**.
*   **$r$ (Radius):** The radius of the circular path the particle takes inside the magnetic field. Measured in **meters (m)**.
*   **$F_B$ (Magnetic Force):** The force exerted on a moving charge by a magnetic field. Measured in **Newtons (N)**.
*   **$F_c$ (Centripetal Force):** The net force causing an object to move in a circular path. Measured in **Newtons (N)**.

---

### **Step-by-Step Solution**

**Step 1: Calculate the velocity of the electron after acceleration**
When the electron is accelerated from rest through a potential difference, its electrical potential energy is converted entirely into kinetic energy. 
The equation for this conservation of energy is:
$$qV = \frac{1}{2}mv^2$$

We need to solve for the velocity ($v$):
$$v^2 = \frac{2qV}{m}$$
$$v = \sqrt{\frac{2qV}{m}}$$

**Step 2: Relate the magnetic force to centripetal force**
Once the electron enters the uniform magnetic field, the magnetic force acts perpendicular to its velocity, causing it to move in a circular path. This magnetic force provides the necessary centripetal force.
The equation setting magnetic force equal to centripetal force is:
$$qvB = \frac{mv^2}{r}$$

We can simplify this by dividing both sides by $v$:
$$qB = \frac{mv}{r}$$

Now, solve for the radius ($r$):
$$r = \frac{mv}{qB}$$

**Step 3: Combine equations and calculate the radius**
Substitute the expression for velocity ($v$) from Step 1 into the radius equation from Step 2:
$$r = \frac{m}{qB} \sqrt{\frac{2qV}{m}}$$

Simplify the expression:
$$r = \frac{1}{B} \sqrt{\frac{2mV}{q}}$$

Now, plug in the known physical constants and the given values:
*   Mass of an electron ($m$) $\approx 9.109 \times 10^{-31}$ kg
*   Elementary charge ($q$) $\approx 1.602 \times 10^{-19}$ C
*   Potential difference ($V$) = $5000$ V
*   Magnetic field ($B$) = $0.1$ T

$$r = \frac{1}{0.1} \sqrt{\frac{2 \cdot (9.109 \times 10^{-31}) \cdot 5000}{1.602 \times 10^{-19}}}$$
$$r = 10 \cdot \sqrt{\frac{9.109 \times 10^{-27}}{1.602 \times 10^{-19}}}$$
$$r = 10 \cdot \sqrt{5.686 \times 10^{-8}}$$
$$r = 10 \cdot (2.38 \times 10^{-4})$$
$$r \approx 2.38 \times 10^{-3} \text{ m}$$

**Answer:** The radius of the circular path is approximately **$2.38$ millimeters**.