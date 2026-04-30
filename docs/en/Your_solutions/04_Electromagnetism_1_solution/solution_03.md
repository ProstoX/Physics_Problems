## 3. Electrostatic Equilibrium

Find the equilibrium position for a charge $q_3 = +1\text{C}$ placed on the line between a charge $q_1 = +4\text{C}$ and a charge $q_2 = +9\text{C}$, which are separated by a distance of 2 m.

---

### Variables and Units Explained

Before diving into the math, here is a quick review of the variables used to solve this problem:

*   **$F$ (Electric Force):** The electrostatic push or pull between charges. Measured in **Newtons ($\text{N}$)**.
*   **$k$ (Coulomb's Constant):** Determines the strength of the electric force, approximately $8.99 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$.
*   **$q$ (Electric Charge):** The amount of charge. We have $q_1$, $q_2$, and the test charge $q_3$. Measured in **Coulombs ($\text{C}$)**.
*   **$d$ (Total Distance):** The total separation between the two outer charges ($2\text{ m}$). Measured in **meters ($\text{m}$)**.
*   **$x$ (Unknown Distance):** The distance from $q_1$ to our equilibrium point. Measured in **meters ($\text{m}$)**.

---

### Step-by-Step Solution

**Step 1: Set Up the Scenario and the Condition for Equilibrium**
We have three positive charges. Positive charges repel each other. 
*   $q_1 (+4\text{ C})$ is pushing $q_3$ to the right.
*   $q_2 (+9\text{ C})$ is pushing $q_3$ to the left.

For $q_3$ to be in **equilibrium**, the net force acting on it must be zero. This means the magnitude of the force from $q_1$ must exactly equal the magnitude of the force from $q_2$:
$$F_{1\text{ on }3} = F_{2\text{ on }3}$$

**Step 2: Define the Distances**
Let's place $q_1$ at position $0$ and $q_2$ at position $2\text{ m}$.
Let $x$ be the distance from $q_1$ to the test charge $q_3$.
Because the total distance is $2\text{ m}$, the distance from $q_3$ to $q_2$ must be $(2 - x)$.

**Step 3: Apply Coulomb's Law**
Using the formula $F = k \frac{|q_a q_b|}{r^2}$, we can write out the forces:
$$k \frac{|q_1 q_3|}{x^2} = k \frac{|q_2 q_3|}{(2 - x)^2}$$

**Step 4: Simplify the Equation**
Notice that Coulomb's constant ($k$) and the test charge ($q_3$) appear on both sides of the equation. We can divide both sides by $k$ and $q_3$ to cancel them out. *(Note: This proves that the equilibrium position does not depend on the magnitude or sign of the test charge $q_3$!)*
$$\frac{q_1}{x^2} = \frac{q_2}{(2 - x)^2}$$

**Step 5: Plug in the Values and Solve**
Substitute our known values for $q_1$ ($4\text{ C}$) and $q_2$ ($9\text{ C}$):
$$\frac{4}{x^2} = \frac{9}{(2 - x)^2}$$

To solve this easily without using the quadratic formula, take the square root of both sides:
$$\frac{\sqrt{4}}{\sqrt{x^2}} = \frac{\sqrt{9}}{\sqrt{(2 - x)^2}}$$
$$\frac{2}{x} = \frac{3}{2 - x}$$

Now, cross-multiply to solve for $x$:
$$2(2 - x) = 3x$$
$$4 - 2x = 3x$$
$$4 = 5x$$
$$x = \frac{4}{5} = 0.8\text{ m}$$

*   **Final Answer:** The $+1\text{ C}$ charge should be placed exactly **$0.8\text{ m}$ away from the $+4\text{ C}$ charge** (which puts it $1.2\text{ m}$ away from the $+9\text{ C}$ charge).

