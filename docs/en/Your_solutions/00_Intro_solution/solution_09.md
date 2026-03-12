### Transforming from Verbal to Mathematically Formal

When dealing with optimization problems (finding the "maximum" or "minimum" of something), the goal is to create a single mathematical function that models the quantity you want to optimize.

1. **The Geometry:** A rectangle in the first quadrant "under the curve" means its bottom edge lies on the x-axis, its left edge lies on the y-axis, and its top-right corner touches the curve.
2. **The Dimensions:** Let the width of the rectangle along the x-axis be $x$. Because the top-right corner touches the curve, the height of the rectangle at that specific $x$ is exactly the y-value of the curve: $y = 3 - x^2$.
3. **The Objective Function:** We want to maximize the area ($A$) of this rectangle. The area of a rectangle is $\text{width} \times \text{height}$.

$$A = x \cdot y$$


4. **The Formalization:** We substitute our expression for $y$ into the area equation so that Area is a function of a single variable, $x$.

$$A(x) = x(3 - x^2)$$


$$A(x) = 3x - x^3$$



Our formal mathematical goal is to find the value of $x$ (where $x > 0$) that yields the absolute maximum value for the function $A(x)$.

---

### Step 1: Find the First Derivative

To find the maximum area, we need to locate the critical points of our area function. We do this by taking the first derivative of $A(x)$ with respect to $x$ using the power rule.


$$A(x) = 3x - x^3$$

$$A'(x) = 3 - 3x^2$$

### Step 2: Find the Critical Points

Critical points occur where the first derivative is equal to zero. Set $A'(x)$ to zero and solve for $x$:


$$3 - 3x^2 = 0$$

$$3 = 3x^2$$

$$1 = x^2$$

$$x = \pm 1$$

Since the problem states the rectangle is in the **first quadrant**, we know $x$ must be positive. Therefore, our only valid critical point is $x = 1$.

### Step 3: Verify the Maximum

To confirm that $x = 1$ actually gives us a maximum area (and not a minimum), we can use the Second Derivative Test. Take the derivative of $A'(x)$:


$$A''(x) = -6x$$

Substitute our critical point $x = 1$ into the second derivative:


$$A''(1) = -6(1) = -6$$

Because the second derivative is negative ($-6 < 0$), the area function is concave down at $x = 1$. This proves that $x = 1$ is indeed a **local maximum**.

### Step 4: Calculate the Dimensions

Now that we know the optimal width ($x$), we can find the optimal height ($y$) by plugging $x$ back into the original curve's equation:


$$y = 3 - x^2$$

$$y = 3 - (1)^2$$

$$y = 3 - 1$$

$$y = 2$$

### Final Answer

The dimensions of the rectangle that yield the maximum area are a **width of $1$ unit** and a **height of $2$ units**. (The maximum area itself is $1 \times 2 = 2$ square units).

*Visualization is available at [solution_09.png](solution_09.png)*