### Transforming from Verbal to Mathematically Formal

When a problem asks for the "area under the curve" of a continuous, non-negative function between two points along the x-axis, it is asking for the **definite integral** of that function over that specific interval.

1. **The Function:** The "curve" is our function, $f(x) = \sin(x)$. This will be the integrand (the expression being integrated).
2. **The Interval:** The phrase "from $x=0$ to $x=\pi$" gives us our lower and upper limits of integration, respectively.
3. **The Formalization:** We combine these elements using the integral symbol ($\int$). The mathematical translation of the verbal problem is:

$$\text{Area} = \int_{0}^{\pi} \sin(x) \, dx$$



---

### Step 1: Set Up the Definite Integral

Based on our formalization, we start with the definite integral:


$$\int_{0}^{\pi} \sin(x) \, dx$$

### Step 2: Find the Antiderivative

To evaluate the definite integral, we first need to find the antiderivative (indefinite integral) of $\sin(x)$. The derivative of $\cos(x)$ is $-\sin(x)$, which means the antiderivative of $\sin(x)$ is $-\cos(x)$.
We write this using bracket notation to indicate that we still need to evaluate it at the limits:


$$[-\cos(x)]_{0}^{\pi}$$

### Step 3: Apply the Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus states that we evaluate the antiderivative at the upper limit and subtract the antiderivative evaluated at the lower limit: $F(b) - F(a)$.


$$(-\cos(\pi)) - (-\cos(0))$$

### Step 4: Evaluate the Trigonometric Values

Substitute the known values for the cosine function at these angles. We know that $\cos(\pi) = -1$ and $\cos(0) = 1$.


$$(-(-1)) - (-1)$$

Simplify the signs:


$$1 + 1$$

$$2$$

### Final Answer

The exact area under the curve $f(x) = \sin(x)$ from $x=0$ to $x=\pi$ is **2** square units.