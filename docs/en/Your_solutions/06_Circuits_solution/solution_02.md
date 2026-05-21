## 2. Resistors

You have a supply of exactly three $1\,\Omega$ resistors. What are all the possible equivalent resistances you can create by combining them? List all unique values.

---

## Variables and Units

| Symbol | Stands For | Unit of Measurement | Description |
| --- | --- | --- | --- |
| **$R$** | Resistance | Ohms ($\Omega$) | The resistance of a single, individual resistor (in this case, $1\,\Omega$). |
| **$R_{eq}$** | Equivalent Resistance | Ohms ($\Omega$) | The total combined resistance of the resistor network when viewed as a single unit. |

---

## Step-by-Step Solution

When you have exactly three identical resistors and must use all of them, there are exactly four unique topological ways to connect them in a standard two-terminal circuit. We will calculate the equivalent resistance for each configuration.

### Configuration 1: All Three in Series

In this configuration, all three resistors are connected end-to-end in a single line.

To find the equivalent resistance of resistors in series, you simply add them together:


$$ R_{eq} = R_1 + R_2 + R_3 $$

$$ R_{eq} = 1 + 1 + 1 $$

$$ R_{eq} = 3\,\Omega $$

### Configuration 2: All Three in Parallel

In this configuration, all three resistors are connected side-by-side across the same two points.

To find the equivalent resistance of resistors in parallel, you sum their reciprocals and then take the reciprocal of that total:


$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} $$

$$ \frac{1}{R_{eq}} = \frac{1}{1} + \frac{1}{1} + \frac{1}{1} $$

$$ \frac{1}{R_{eq}} = 3 $$

Flipping both sides to solve for $R_{eq}$:


$$ R_{eq} = \frac{1}{3}\,\Omega \approx 0.333\,\Omega $$

### Configuration 3: Two in Parallel, One in Series

In this setup, two resistors are connected in parallel with each other, and that entire parallel pair is connected in series with the third resistor.

First, calculate the resistance of the parallel pair ($R_{p}$):


$$ \frac{1}{R_p} = \frac{1}{1} + \frac{1}{1} = 2 \implies R_p = \frac{1}{2}\,\Omega = 0.5\,\Omega $$

Next, add the third resistor in series:


$$ R_{eq} = R_p + R_3 $$

$$ R_{eq} = 0.5 + 1 $$

$$ R_{eq} = 1.5\,\Omega \text{ (or } \frac{3}{2}\,\Omega \text{)} $$

### Configuration 4: Two in Series, One in Parallel

In this final setup, two resistors are connected in series with each other, and that entire series branch is placed in parallel with the third resistor.

First, calculate the resistance of the series branch ($R_{s}$):


$$ R_s = 1 + 1 = 2\,\Omega $$

Next, calculate the equivalent resistance of this $2\,\Omega$ branch in parallel with the remaining $1\,\Omega$ resistor:


$$ \frac{1}{R_{eq}} = \frac{1}{R_s} + \frac{1}{R_3} $$

$$ \frac{1}{R_{eq}} = \frac{1}{2} + \frac{1}{1} $$

$$ \frac{1}{R_{eq}} = 1.5 \text{ (or } \frac{3}{2} \text{)} $$

Flipping the fraction to solve for $R_{eq}$:


$$ R_{eq} = \frac{2}{3}\,\Omega \approx 0.667\,\Omega $$

---

## Final Answer

By combining exactly three $1\,\Omega$ resistors, you can create the following four unique equivalent resistances:

* **$3\,\Omega$**
* **$1.5\,\Omega$** (or $\frac{3}{2}\,\Omega$)
* **$0.667\,\Omega$** (or $\frac{2}{3}\,\Omega$)
* **$0.333\,\Omega$** (or $\frac{1}{3}\,\Omega$)
