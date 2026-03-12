To solve the system of linear equations using Cramer's Rule, we first write the system in standard form:

1. $2x + 3y = 12$
2. $x - y = 1$

This can be represented as a matrix equation $AX = B$:


$$\begin{bmatrix} 2 & 3 \\ 1 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 12 \\ 1 \end{bmatrix}$$

Cramer's Rule states that $x = \frac{D_x}{D}$ and $y = \frac{D_y}{D}$, where $D$ is the determinant of the coefficient matrix, and $D_x$ and $D_y$ are the determinants of the matrices formed by replacing the respective columns with the constant terms.

### Step 1: Find the determinant of the coefficient matrix ($D$)

$$D = \begin{vmatrix} 2 & 3 \\ 1 & -1 \end{vmatrix}$$

$$D = (2)(-1) - (3)(1)$$

$$D = -2 - 3$$

$$D = -5$$

### Step 2: Find the determinant for $x$ ($D_x$)

Replace the first column (x-coefficients) with the constant terms ($12$ and $1$).


$$D_x = \begin{vmatrix} 12 & 3 \\ 1 & -1 \end{vmatrix}$$

$$D_x = (12)(-1) - (3)(1)$$

$$D_x = -12 - 3$$

$$D_x = -15$$

### Step 3: Find the determinant for $y$ ($D_y$)

Replace the second column (y-coefficients) with the constant terms ($12$ and $1$).


$$D_y = \begin{vmatrix} 2 & 12 \\ 1 & 1 \end{vmatrix}$$

$$D_y = (2)(1) - (12)(1)$$

$$D_y = 2 - 12$$

$$D_y = -10$$

### Step 4: Solve for $x$ and $y$

Now, apply Cramer's Rule to find the values of $x$ and $y$:


$$x = \frac{D_x}{D} = \frac{-15}{-5} = 3$$

$$y = \frac{D_y}{D} = \frac{-10}{-5} = 2$$

### Check:

1. $2 * 3 + 3 * 2 = 12$
2. $3 - 2 = 1$

### Final Answer:

The solution to the system of equations is **$x = 3$** and **$y = 2$**.