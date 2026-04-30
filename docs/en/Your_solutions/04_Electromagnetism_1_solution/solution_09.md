## 9. Vector Lorentz Force

A proton moves with a velocity $\vec{v} = (2\hat{i} - 4\hat{j} + \hat{k}) \text{ m/s}$ in a region where the magnetic field is $\vec{B} = (\hat{i} + 2\hat{j} - \hat{k}) \text{ T}$. What is the magnitude of the magnetic force this charge experiences?

---

### **Variables and Units**
Before calculating, here is what each letter in the relevant physics formula represents:
*   **$\vec{F}$**: Magnetic Lorentz force vector. The force exerted on the particle, measured in **Newtons (N)**.
*   **$q$**: Electric charge. For a proton, this is the elementary charge, approximately **1.60 × 10⁻¹⁹ Coulombs (C)**.
*   **$\vec{v}$**: Velocity vector. The speed and direction of the particle in 3D space, measured in **meters per second (m/s)**.
*   **$\vec{B}$**: Magnetic field vector. The strength and direction of the magnetic field in 3D space, measured in **Teslas (T)**.
*   **$\hat{i}, \hat{j}, \hat{k}$**: Unit vectors representing the x, y, and z axes, respectively. 

---

### **Step-by-Step Solution**

**Step 1: Identify the correct formula.**
When velocity and magnetic field are given as 3D vectors, we use the vector form of the Lorentz force equation (ignoring any electric field, which is zero here):
$$ \vec{F} = q(\vec{v} \times \vec{B}) $$
This requires calculating the cross product of the velocity and magnetic field vectors.

**Step 2: Calculate the cross product ($\vec{v} \times \vec{B}$).**
Set up the determinant with the given vectors $\vec{v} = (2\hat{i} - 4\hat{j} + \hat{k})$ and $\vec{B} = (\hat{i} + 2\hat{j} - \hat{k})$:
$$ \vec{v} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -4 & 1 \\ 1 & 2 & -1 \end{vmatrix} $$

Expand the determinant:
$$ = \hat{i}[(-4)(-1) - (1)(2)] - \hat{j}[(2)(-1) - (1)(1)] + \hat{k}[(2)(2) - (-4)(1)] $$
$$ = \hat{i}[4 - 2] - \hat{j}[-2 - 1] + \hat{k}[4 + 4] $$
$$ \vec{v} \times \vec{B} = 2\hat{i} + 3\hat{j} + 8\hat{k} $$

**Step 3: Find the magnitude of the cross product.**
The magnitude of a vector $\vec{A} = x\hat{i} + y\hat{j} + z\hat{k}$ is $|\vec{A}| = \sqrt{x^2 + y^2 + z^2}$.
$$ |\vec{v} \times \vec{B}| = \sqrt{2^2 + 3^2 + 8^2} $$
$$ |\vec{v} \times \vec{B}| = \sqrt{4 + 9 + 64} = \sqrt{77} \approx 8.775 $$

**Step 4: Calculate the final force magnitude.**
Multiply the magnitude of the cross product by the charge of the proton ($q = 1.6 \times 10^{-19}$ C).
$$ |\vec{F}| = q|\vec{v} \times \vec{B}| $$
$$ |\vec{F}| = (1.6 \times 10^{-19}) \times \sqrt{77} $$
$$ |\vec{F}| \approx 1.40 \times 10^{-18} \text{ N} $$

**Answer:** The magnitude of the magnetic force this charge experiences is approximately **1.40 × 10⁻¹⁸ N**.

---

### **Prompt for HTML Visualization Generation**


> **System Prompt for Visualization:**
> Create an interactive, single-file HTML visualization using HTML, CSS, and Three.js (via CDN) to demonstrate the vector Lorentz force using the cross product $\vec{F} = q(\vec{v} \times \vec{B})$.
> 
> **Visual Elements:**
> 1. Set up a 3D scene with a grid helper and clear Cartesian axes (x, y, z).
> 2. Render three distinct, labeled 3D vector arrows originating from the center (0,0,0):
>    * Velocity vector ($\vec{v}$)
>    * Magnetic Field vector ($\vec{B}$)
>    * Force vector ($\vec{F}$), which represents the cross product. Note: Scale the visual length of $\vec{F}$ appropriately so it fits on screen alongside the others.
> 3. Draw a transparent plane spanned by $\vec{v}$ and $\vec{B}$ to visually prove that the resulting force vector $\vec{F}$ is perfectly perpendicular to both.
> 4. Include orbital controls so the user can click and drag to rotate the 3D scene and view the vectors from any angle.
> 
> **Interactivity (UI Controls):**
> Include an overlaid control panel (using simple HTML/CSS over the canvas) with number inputs or sliders for the components of $\vec{v}$ (x, y, z) and $\vec{B}$ (x, y, z). 
> * Initialize the values to: $\vec{v} = (2, -4, 1)$ and $\vec{B} = (1, 2, -1)$. 
> * When the user changes any component, dynamically update the 3D vectors and the plane in real-time.
> * Display the calculated numerical resulting vector for $\vec{v} \times \vec{B}$ in the UI panel.
> 
> Ensure all CSS and JS is contained within the single HTML file, making it instantly runnable in a browser.