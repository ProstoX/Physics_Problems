## 2. Ampere's Law

Two long, parallel wires are $10 \text{ cm}$ apart and carry currents of $5 \text{ A}$ in opposite directions. Calculate the magnitude and direction of the magnetic field at a point midway between the wires.

---

### **Variables and Units Explained**

*   **$B$ (Magnetic Field):** Represents the strength of the magnetic field at a specific point. Measured in Teslas (T).
*   **$\mu_0$ (Vacuum Permeability):** A fundamental physical constant representing the resistance of a vacuum to forming a magnetic field. It is exactly $4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$.
*   **$I$ (Current):** The rate of flow of electric charge through the wires. Measured in Amperes (A).
*   **$r$ (Distance):** The radial distance from the center of the wire to the point where the magnetic field is being measured. Measured in meters (m).

---

### **Solution: Calculating the Magnetic Field**

**Step 1: Identify given information and convert to SI units**
*   Total distance between wires ($d$) = 10 cm = 0.1 m
*   Distance from each wire to the midpoint ($r$) = 5 cm = 0.05 m
*   Current in wire 1 ($I_1$) = 5 A
*   Current in wire 2 ($I_2$) = 5 A
*   The currents flow in opposite directions.

**Step 2: Apply Ampere's Law for a long straight wire**
The magnitude of the magnetic field produced by a single, infinitely long, straight wire is given by the formula:
$$B = \frac{\mu_0 I}{2 \pi r}$$

**Step 3: Determine the direction of the magnetic field**
We use the **Right-Hand Rule**: Point your right thumb in the direction of the current, and your fingers will curl in the direction of the circular magnetic field lines.
*   Assume Wire 1 carries current "up". At the midpoint to its right, its magnetic field points "into the page".
*   Assume Wire 2 (located to the right of Wire 1) carries current "down". At the midpoint to its left, its magnetic field *also* points "into the page".
Because the currents are in opposite directions, their magnetic fields at the exact midpoint point in the **same direction** and reinforce each other.

**Step 4: Calculate the net magnetic field magnitude**
Since the magnetic fields point in the same direction, we simply add their magnitudes:
$$B_{\text{net}} = B_1 + B_2$$
$$B_{\text{net}} = \frac{\mu_0 I_1}{2 \pi r} + \frac{\mu_0 I_2}{2 \pi r}$$

Substitute the known values:
$$B_{\text{net}} = \frac{(4\pi \times 10^{-7}) \times 5}{2 \pi \times 0.05} + \frac{(4\pi \times 10^{-7}) \times 5}{2 \pi \times 0.05}$$

Simplify the expression (the $\pi$ cancels out):
$$B_{\text{net}} = \frac{2 \times 10^{-7} \times 5}{0.05} + \frac{2 \times 10^{-7} \times 5}{0.05}$$
$$B_{\text{net}} = \frac{10 \times 10^{-7}}{0.05} + \frac{10 \times 10^{-7}}{0.05}$$
$$B_{\text{net}} = (20 \times 10^{-7}) + (20 \times 10^{-7}) = 40 \times 10^{-7} \text{ T}$$

Expressed in scientific notation, the net magnetic field magnitude is **$4.0 \times 10^{-5} \text{ T}$** (or 40 $\mu\text{T}$). The direction is perpendicular to the plane containing the two wires (e.g., pointing straight into the page/screen).