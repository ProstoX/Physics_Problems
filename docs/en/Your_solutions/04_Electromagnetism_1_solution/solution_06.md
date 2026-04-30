##  6. Field at a point from a system of charges

Two point charges are given:

* $+q\  \text{at point}\  (-a, 0)$
* $+2q\  \text{at point}\  (a, 0)$

1. Determine the field vector $\vec E(0, y)$, $\vec E(x, 0)$ and generally $\vec E(x, y)$.
2. Determine the condition for which the components $E_x = 0$, $E_y = 0$ and the zero field $\vec E = 0$.
3. Calculate the field for: $a = 0.2\,\mathrm{m}$, $y = 0.3\,\mathrm{m}$, $q = 2\,\mu\mathrm{C}$.
4. Investigate the limit $y \gg a$.

---

### Variables and Units Explained

Before solving the equations, here is a quick review of the variables:

*   **$\vec{E}$ (Electric Field):** A vector representing the force per unit charge at a specific point in space. Measured in **Newtons per Coulomb ($\text{N/C}$)** or Volts per meter ($\text{V/m}$). It has components $E_x$ and $E_y$.
*   **$k$ (Coulomb's Constant):** $8.99 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2$.
*   **$q$ (Base Charge):** The reference amount of charge. Measured in **Coulombs ($\text{C}$)**.
*   **$a$ (Distance parameter):** Defines the position of the charges on the x-axis. Measured in **meters ($\text{m}$)**.
*   **$x, y$ (Coordinates):** The observation point where we are calculating the field. Measured in **meters ($\text{m}$)**.

---

### Step-by-Step Solution

#### 1. Determine the field vectors $\vec{E}(x,y)$, $\vec{E}(0,y)$, and $\vec{E}(x,0)$
The total electric field at any point is the vector sum of the fields from the individual charges: $\vec{E} = \vec{E}_1 + \vec{E}_2$.
The general formula for an electric field vector from a point charge at origin $(x_0, y_0)$ is:
$$\vec{E} = k \frac{q}{r^3} \vec{r} = kq \frac{(x - x_0)\hat{i} + (y - y_0)\hat{j}}{((x - x_0)^2 + (y - y_0)^2)^{3/2}}$$

**General Field $\vec{E}(x,y)$:**
For $q_1 = +q$ at $(-a, 0)$ and $q_2 = +2q$ at $(a, 0)$, we add their contributions:
$$E_x(x,y) = kq \left[ \frac{x + a}{((x + a)^2 + y^2)^{3/2}} + \frac{2(x - a)}{((x - a)^2 + y^2)^{3/2}} \right]$$
$$E_y(x,y) = kq y \left[ \frac{1}{((x + a)^2 + y^2)^{3/2}} + \frac{2}{((x - a)^2 + y^2)^{3/2}} \right]$$
$$\vec{E}(x,y) = E_x(x,y)\hat{i} + E_y(x,y)\hat{j}$$

**Field along the y-axis $\vec{E}(0,y)$:**
Substitute $x = 0$ into the general equations:
$$E_x(0,y) = kq \left[ \frac{a}{(a^2 + y^2)^{3/2}} - \frac{2a}{(a^2 + y^2)^{3/2}} \right] = -\frac{kqa}{(a^2 + y^2)^{3/2}}$$
$$E_y(0,y) = kq y \left[ \frac{1}{(a^2 + y^2)^{3/2}} + \frac{2}{(a^2 + y^2)^{3/2}} \right] = \frac{3kqy}{(a^2 + y^2)^{3/2}}$$
$$\vec{E}(0,y) = \frac{kq}{(a^2 + y^2)^{3/2}} (-a\hat{i} + 3y\hat{j})$$

**Field along the x-axis $\vec{E}(x,0)$:**
Substitute $y = 0$. Here, $E_y = 0$ everywhere on the x-axis. The distance formulas simplify to absolute values:
$$\vec{E}(x,0) = kq \left[ \frac{x + a}{|x + a|^3} + \frac{2(x - a)}{|x - a|^3} \right] \hat{i}$$

#### 2. Determine the condition for zero field ($E_x = 0, E_y = 0, \vec{E} = 0$)
*   **Condition for $E_y = 0$:** Look at the numerator of the general $E_y$ equation. Because the bracketed term is a sum of strictly positive distances, the only way for $E_y = 0$ is if **$y = 0$**. (The zero field must lie on the x-axis).
*   **Condition for $E_x = 0$:** Since $y = 0$, we look at the x-axis. To have opposite vectors that can cancel out, the point must lie *between* the two positive charges ($-a < x < a$). In this region, $(x+a)$ is positive and $(x-a)$ is negative.
Set $E_x = 0$:
$$\frac{1}{(x + a)^2} - \frac{2}{(a - x)^2} = 0$$
$$\frac{1}{(x + a)^2} = \frac{2}{(a - x)^2}$$
Take the square root of both sides (knowing both denominators are positive distances in this region):
$$a - x = \sqrt{2}(x + a)$$
$$a - a\sqrt{2} = x + x\sqrt{2}$$
$$x = a \frac{1 - \sqrt{2}}{1 + \sqrt{2}}$$
Multiply top and bottom by $(1 - \sqrt{2})$ to rationalize:
$$x = a(2\sqrt{2} - 3) \approx -0.172a$$
*   **Condition for $\vec{E} = 0$:** Both components must be zero simultaneously. Therefore, the absolute zero field point is at **$(-0.172a, 0)$**.

#### 3. Calculate the field for specific values
Given: $a = 0.2\text{ m}$, $y = 0.3\text{ m}$, $x = 0$, $q = 2 \times 10^{-6}\text{ C}$. We use the $\vec{E}(0,y)$ equation from Step 1.
First, calculate the denominator:
$$(a^2 + y^2)^{3/2} = (0.2^2 + 0.3^2)^{3/2} = (0.04 + 0.09)^{3/2} = (0.13)^{3/2} \approx 0.04687\text{ m}^3$$
Next, calculate $kq$:
$$kq = (8.99 \times 10^9) \times (2 \times 10^{-6}) = 17980\text{ N}\cdot\text{m}^2/\text{C}$$
Now plug into the vector components:
$$E_x = -\frac{17980 \times 0.2}{0.04687} \approx -76,723\text{ N/C}$$
$$E_y = \frac{3 \times 17980 \times 0.3}{0.04687} = \frac{16182}{0.04687} \approx 345,253\text{ N/C}$$
$$\vec{E}(0, 0.3) \approx (-7.67 \times 10^4\hat{i} + 3.45 \times 10^5\hat{j})\text{ N/C}$$

#### 4. Investigate the limit $y \gg a$
If $y$ is much greater than $a$, we are looking at the system from extremely far away along the y-axis. 
In the denominator $(a^2 + y^2)^{3/2}$, $a^2$ becomes insignificantly small compared to $y^2$. Thus, $(a^2 + y^2)^{3/2} \approx (y^2)^{3/2} = y^3$.
Substitute this into our $\vec{E}(0,y)$ equation:
$$E_x \approx -\frac{kqa}{y^3}$$
$$E_y \approx \frac{kq(3y)}{y^3} = \frac{k(3q)}{y^2}$$
**Conclusion:** Because $y$ is so large, $E_x$ drops to zero very quickly (inversely proportional to the cube of the distance). However, $E_y$ dominates and acts exactly like the electric field of a single point charge with a magnitude of **$3q$**. This makes intuitive physical sense: from very far away, the two individual charges ($+q$ and $+2q$) blur together into one combined charge of $+3q$.
