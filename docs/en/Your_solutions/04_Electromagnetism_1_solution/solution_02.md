## 2. Electric Potential

Point charges of +1C, -2C, +3C, and -4C are placed at the corners of a square with sides of 1.0 m (in order). Calculate the electric potential at the center of the square.

---

### Variables and Units Explained

Here is a quick breakdown of the letters used in the Electric Potential formula and the geometry of this problem:

*   **$V$ (Electric Potential):** Think of this as the "electrical pressure" at a specific point in space. Measured in **Volts (V)**, which is equivalent to Joules per Coulomb (J/C).
*   **$k$ (Coulomb's Constant):** A constant determining the strength of the electric field. It is approximately $8.99 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$.
*   **$q$ (Electric Charge):** The amount of charge creating the potential. Measured in **Coulombs (C)**.
*   **$r$ (Distance):** The straight-line distance from the charge to the point where we are measuring the potential (the center). Measured in **meters (m)**.
*   **$a$ (Side Length):** The length of the sides of the square. Measured in **meters (m)**.

---

### Step-by-Step Solution

**Step 1: Find the Distance ($r$) from the Corners to the Center**
Just like in the previous problem, the charges are at the corners of a square with a side length of 1.0 m. The distance from any corner to the exact center is half the length of the diagonal.
$$r = \frac{a\sqrt{2}}{2}$$
Given $a = 1.0$ m:
$$r = \frac{1.0 \times \sqrt{2}}{2} \approx 0.7071\text{ m}$$
Because the square is perfectly symmetrical, this distance $r$ is exactly the same for all four charges.

**Step 2: Understand the Formula for Electric Potential**
The electric potential created by a single point charge at a distance $r$ is:
$$V = k \frac{q}{r}$$
Unlike force, potential is a **scalar quantity**. This means we do not need to calculate vector directions. We just calculate the potential from each charge and add them together algebraically (keeping their positive or negative signs).

**Step 3: Apply the Principle of Superposition**
The total electric potential at the center ($V_{net}$) is simply the sum of the potentials from the four individual charges:
$$V_{net} = V_1 + V_2 + V_3 + V_4$$
$$V_{net} = k \frac{q_1}{r} + k \frac{q_2}{r} + k \frac{q_3}{r} + k \frac{q_4}{r}$$
Because $k$ and $r$ are the same for every term, we can factor them out to make the math incredibly easy:
$$V_{net} = \frac{k}{r} (q_1 + q_2 + q_3 + q_4)$$

**Step 4: Calculate the Final Value**
Let's plug in our specific charge values (+1 C, -2 C, +3 C, -4 C):
$$Sum\ of\ charges = 1 - 2 + 3 - 4 = -2\text{ C}$$
Now, plug the sum, $k$, and $r$ into our factored equation:
$$V_{net} = \frac{8.99 \times 10^9}{0.7071} \times (-2)$$
$$V_{net} = (12.71 \times 10^9) \times (-2)$$
$$V_{net} = -25.42 \times 10^9\text{ V}$$

*   **Final Answer:** The electric potential at the center of the square is **$-25.42 \times 10^9$ V** (or $-25.42$ Gigavolts).
