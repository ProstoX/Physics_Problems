## 3. Biot-Savart Law

A small segment of a line wire of length $0.1 \text{ m}$ carries a current of $3 \text{ A}$. The segment is located at a distance of $0.2 \text{ m}$ from a point $P$. Calculate the magnetic field at point $P$ due to this current segment (assume the segment is perpendicular to the line connecting it to point $P$).

---

### **Variables and Units Explained**

*   **$dB$ (Magnetic Field):** The infinitesimal magnetic field produced by the small current segment. Measured in Teslas (T).
*   **$\mu_0$ (Vacuum Permeability):** A physical constant describing how well a magnetic field can penetrate a vacuum. Its exact value is $4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$.
*   **$I$ (Current):** The electric current flowing through the wire segment. Measured in Amperes (A).
*   **$dl$ (Length of Segment):** The tiny physical length of the wire segment carrying the current. Measured in meters (m).
*   **$r$ (Distance):** The straight-line distance from the center of the current segment to the observation point $P$. Measured in meters (m).
*   **$\theta$ (Angle):** The angle between the direction of the current segment ($d\mathbf{l}$) and the position vector pointing from the segment to point $P$ ($\mathbf{r}$). Measured in degrees ($^\circ$) or radians.

---

### **Solution: Calculating the Magnetic Field**

**Step 1: Identify the given values and constants**
*   Length of segment ($dl$) = $0.1 \text{ m}$
*   Current ($I$) = $3 \text{ A}$
*   Distance to point P ($r$) = $0.2 \text{ m}$
*   Angle ($\theta$) = $90^\circ$ (since the problem states the segment is perpendicular to the line connecting it to point P)
*   The constant factor $\frac{\mu_0}{4\pi}$ is exactly $10^{-7} \text{ T}\cdot\text{m/A}$.

**Step 2: State the Biot-Savart Law equation**
The magnitude of the magnetic field $dB$ produced by a small current element is given by the Biot-Savart Law:
$$dB = \frac{\mu_0}{4\pi} \frac{I \cdot dl \cdot \sin(\theta)}{r^2}$$

**Step 3: Substitute the values into the equation**
Because the angle $\theta$ is $90^\circ$, $\sin(90^\circ) = 1$. This means the field at this specific point is at its maximum for this distance.
$$dB = (10^{-7}) \frac{3 \cdot 0.1 \cdot \sin(90^\circ)}{(0.2)^2}$$

**Step 4: Perform the calculation**
$$dB = (10^{-7}) \frac{0.3 \cdot 1}{0.04}$$
$$dB = (10^{-7}) \cdot 7.5$$

The magnitude of the magnetic field at point $P$ is **$7.5 \times 10^{-7} \text{ T}$** (or $0.75 \text{ \mu T}$). 

*(Note: The direction of the magnetic field would be determined by the Right-Hand Rule, pointing perpendicular to both the wire segment and the line connecting it to point $P$.)*