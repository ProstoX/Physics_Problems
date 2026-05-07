## 5. Energy Stored by charge in a capacitor

We have parallel-plate capacitor with the following parameters:

* $S = 0.02\,\mathrm{m^2}$
* $d = 5\,\mathrm{mm}$
* $U = 500\,\mathrm{V}$

1. Calculate the capacitance $C$ of the capacitor.
2. Calculate the energy $U$ stored in the capacitor.
3. Calculate the electric field intensity $E$ between the plates.
4. Calculate the force of attraction $F$ between the plates.

---

### **Variables and Units**

Before diving into the calculations, here is a quick breakdown of what each letter stands for, its standard physical meaning, and the SI units used to measure it:

*   **$S$ (Area):** The surface area of one of the capacitor plates. Measured in square meters (m²).
*   **$d$ (Distance):** The separation gap between the two plates. Measured in meters (m).
*   **$U$ or $V$ (Voltage/Potential Difference):** The electric potential difference applied across the plates. Measured in volts (V). *(Note: To avoid confusion between voltage and energy—which are both sometimes represented by $U$—I will use $V$ for voltage and $U$ for stored energy in the formulas below).*
*   **$C$ (Capacitance):** The ability of the capacitor to store an electric charge. Measured in farads (F).
*   **$U$ or $W$ (Energy):** The total electrical potential energy stored in the electric field. Measured in joules (J). 
*   **$E$ (Electric Field Intensity):** The strength of the electric field between the plates. Measured in volts per meter (V/m).
*   **$F$ (Force):** The electrostatic force of attraction between the positively and negatively charged plates. Measured in newtons (N).
*   **$\varepsilon_0$ (Vacuum Permittivity):** A physical constant representing the capability of a vacuum to permit electric fields. It is approximately $8.854 \times 10^{-12}$ F/m.

---

### **Calculations**

**Given Parameters:**
*   Area ($S$) = 0.02 m²
*   Distance ($d$) = 5 mm = 0.005 m
*   Voltage ($V$) = 500 V

#### **1. Calculate the capacitance $C$**
The capacitance of a parallel-plate capacitor in a vacuum (or air) is determined by its geometry.

$$C = \frac{\varepsilon_0 \cdot S}{d}$$

*   **Step-by-step:**
    $$C = \frac{(8.854 \times 10^{-12} \text{ F/m}) \cdot 0.02 \text{ m}^2}{0.005 \text{ m}}$$
    $$C = 8.854 \times 10^{-12} \cdot 4$$
    $$C = 3.5416 \times 10^{-11} \text{ F}$$
*   **Result:** **35.4 pF** (picofarads)

#### **2. Calculate the energy $U$ stored in the capacitor**
The energy stored in a capacitor is half the product of its capacitance and the square of the voltage.

$$U = \frac{1}{2} C V^2$$

*   **Step-by-step:**
    $$U = 0.5 \cdot (3.5416 \times 10^{-11} \text{ F}) \cdot (500 \text{ V})^2$$
    $$U = 0.5 \cdot (3.5416 \times 10^{-11}) \cdot 250,000$$
    $$U = 4.427 \times 10^{-6} \text{ J}$$
*   **Result:** **4.43 µJ** (microjoules)

#### **3. Calculate the electric field intensity $E$**
For a parallel-plate capacitor, the electric field is uniform and depends directly on the voltage and inversely on the distance.

$$E = \frac{V}{d}$$

*   **Step-by-step:**
    $$E = \frac{500 \text{ V}}{0.005 \text{ m}}$$
    $$E = 100,000 \text{ V/m}$$
*   **Result:** **100 kV/m** (kilovolts per meter)

#### **4. Calculate the force of attraction $F$ between the plates**
The plates have opposite charges, so they attract each other. A simple way to calculate this is using the relationship between energy and force ($F = \frac{U}{d}$). Alternatively, you can use the electrostatic pressure formula $F = \frac{1}{2} \varepsilon_0 E^2 S$.

$$F = \frac{U}{d}$$

*   **Step-by-step:**
    $$F = \frac{4.427 \times 10^{-6} \text{ J}}{0.005 \text{ m}}$$
    $$F = 8.854 \times 10^{-4} \text{ N}$$
*   **Result:** **8.85 \times 10⁻⁴ N** (or 0.885 mN)
