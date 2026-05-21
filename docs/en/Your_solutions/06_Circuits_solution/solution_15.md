## 15. Resistor Cube*

A cube is constructed from 12 identical resistors on its edges, each with resistance R. What is the equivalent resistance between two opposite corners of the cube?

---

## Solution: Equivalent Resistance of a Resistor Cube

### Given

A cube has:

* 12 identical resistors.
* Each resistor has a resistance $R$.

**Goal:** Find the equivalent resistance ($R_{\text{eq}}$) between two opposite corners of the cube.

---

### Step 1 — Understand the Symmetry

Connect the battery between two opposite corners of the cube:

* **Corner A:** Input
* **Corner B:** Output

Because the cube is perfectly symmetric:

* The three vertices adjacent to **A** are at the same electric potential.
* The three vertices adjacent to **B** are also at the same electric potential.

---

### Step 2 — Group the Vertices

The cube can be viewed as four distinct layers:

1. **Corner A**
2. **Three equivalent vertices** near A
3. **Three equivalent vertices** near B
4. **Corner B**

---

### Step 3 — Simplify the Resistors

We can now calculate the equivalent resistance for each section:

* **First Set (near A):** There are 3 resistors of resistance $R$ in parallel.

$$R_1 = \frac{R}{3}$$


* **Middle Section:** Between the two groups of middle vertices, there are 6 resistors of resistance $R$ in parallel.

$$R_2 = \frac{R}{6}$$


* **Last Set (near B):** There are 3 resistors of resistance $R$ in parallel.

$$R_3 = \frac{R}{3}$$



---

### Step 4 — Calculate Total Equivalent Resistance

These three sections are connected in series. Therefore:


$$R_{\text{eq}} = R_1 + R_2 + R_3$$

Substitute the values:


$$R_{\text{eq}} = \frac{R}{3} + \frac{R}{6} + \frac{R}{3}$$

Find a common denominator:


$$R_{\text{eq}} = \frac{2R}{6} + \frac{R}{6} + \frac{2R}{6} = \frac{5R}{6}$$

---

### Final Answer

$$\boxed{R_{\text{eq}} = \frac{5R}{6}}$$