## 1. Coulomb's Law

Four point charges of +1.0 C each are placed at the corners of a square with sides of 1.0 m. Calculate the magnitude and direction of the electric force on a charge of -2.0 C placed at the center of the square.

---

### Variables and Units Explained

Before jumping into the math, here is a quick breakdown of the letters used in Coulomb's Law and the geometry of this problem:

*   **$F$ (Electric Force):** The pull or push between charges. Measured in **Newtons ($\text{N}$)**.
*   **$k$ (Coulomb's Constant):** A physical constant that dictates the strength of the electric force. It is approximately $8.99 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$.
*   **$q$ and $Q$ (Electric Charge):** The amount of charge on the objects. Measured in **Coulombs ($\text{C}$)**.
*   **$r$ (Distance):** The straight-line distance between the centers of two charges. Measured in **meters ($\text{m}$)**.
*   **$a$ (Side Length):** The length of the sides of the square. Measured in **meters ($\text{m}$)**.

---

### Step-by-Step Solution

**Step 1: Understand the Geometry and Find the Distance ($r$)**
To use Coulomb's Law, we need the distance from the corner charges to the center charge. The diagonal of a square with side length $a$ is $a\sqrt{2}$. The center is exactly halfway along this diagonal.
$$r = \frac{a\sqrt{2}}{2}$$
Given $a = 1.0\text{ m}$:
$$r = \frac{1.0 \times \sqrt{2}}{2} \approx 0.707\text{ m}$$
Notice that $r^2 = (\frac{\sqrt{2}}{2})^2 = \frac{2}{4} = 0.5\text{ m}^2$. This will make our calculation easier.

**Step 2: Calculate the Magnitude of the Force from One Corner**
Coulomb's Law states that the magnitude of the electrostatic force between two point charges is:
$$F = k \frac{|q Q|}{r^2}$$
Let's calculate the force ($F_1$) exerted by just *one* of the $+1.0\text{ C}$ corner charges on the $-2.0\text{ C}$ central charge:
$$F_1 = (8.99 \times 10^9) \frac{|(1.0) \times (-2.0)|}{0.5}$$
$$F_1 = (8.99 \times 10^9) \frac{2.0}{0.5}$$
$$F_1 = 35.96 \times 10^9\text{ N}$$
This force is **attractive** because the charges have opposite signs (positive corner, negative center). Therefore, the force pulls the center charge directly toward that specific corner.

**Step 3: Apply the Principle of Superposition (Symmetry)**
We have four identical $+1.0\text{ C}$ charges at the corners, meaning there are four forces acting on the central charge, all pulling outward toward their respective corners with the exact same magnitude ($35.96 \times 10^9\text{ N}$).

Now, look at the vectors:
*   The force pulling toward the top-right corner is perfectly opposed by the force pulling toward the bottom-left corner. They cancel each other out entirely.
*   The force pulling toward the top-left corner is perfectly opposed by the force pulling toward the bottom-right corner. They also cancel each other out.

**Step 4: Final Conclusion**
Because of the perfectly symmetrical arrangement of identical charges, all force vectors cancel out. 

*   **Net Force Magnitude:** $0\text{ N}$
*   **Direction:** None (the net force is zero, so direction is undefined).