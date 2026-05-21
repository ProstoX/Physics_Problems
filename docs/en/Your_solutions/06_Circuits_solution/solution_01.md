## 1. Series and Parallel Circuit

You have three resistors, $R_1=15\,\Omega$, $R_2=30\,\Omega$, and $R_3=50\,\Omega$ and a 12 V battery. Consider case when they are all connected in series and when all of them connected in parallel. Calculate the total equivalent resistance in each case. Calculate the current flowing from the battery in each case.

---


## Variables and Units


| Symbol | Stands For | Unit of Measurement | Description |
| --- | --- | --- | --- |
| **$V$** | Voltage | Volts ($\text{V}$) | The electrical potential or "push" provided by the battery. |
| **$I$** | Current | Amperes or Amps ($\text{A}$) | The rate at which electrical charge flows through the circuit. |
| **$R$** | Resistance | Ohms ($\Omega$) | How much a component restricts the flow of electrical current. |
| **$R_{eq}$** | Equivalent Resistance | Ohms ($\Omega$) | The total combined resistance of all resistors in the circuit. |

---

## Part 1: Series Circuit

In a series circuit, the components are connected end-to-end in a single path. The current has only one route to flow through.

### Step 1: Calculate Total Equivalent Resistance ($R_{eq}$)

For resistors in series, you simply add their individual resistances together.

$$ R_{eq} = R_1 + R_2 + R_3 $$

Plug in the given values:

$$ R_{eq} = 15 + 30 + 50 $$

$$ R_{eq} = 95\,\Omega $$

### Step 2: Calculate Total Current ($I$)

To find the current flowing from the battery, we use Ohm's Law ($V = I \times R$), rearranged to solve for $I$:

$$ I = \frac{V}{R_{eq}} $$

Plug in the battery's voltage ($12\,\text{V}$) and our calculated total resistance:

$$ I = \frac{12}{95} $$

$$ I \approx 0.126\,\text{A} $$

---

## Part 2: Parallel Circuit

In a parallel circuit, the components are connected across multiple branches. The current splits, taking different paths through each resistor before combining again.

### Step 3: Calculate Total Equivalent Resistance ($R_{eq}$)

For resistors in parallel, the reciprocal of the total resistance is equal to the sum of the reciprocals of each individual resistor.

$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} $$

Plug in the values:

$$ \frac{1}{R_{eq}} = \frac{1}{15} + \frac{1}{30} + \frac{1}{50} $$

To add these fractions, find a common denominator, which is $150$:

$$ \frac{1}{R_{eq}} = \frac{10}{150} + \frac{5}{150} + \frac{3}{150} $$

$$ \frac{1}{R_{eq}} = \frac{18}{150} $$

Now, flip the fraction to solve for $R_{eq}$ rather than $\frac{1}{R_{eq}}$:

$$ R_{eq} = \frac{150}{18} $$

$$ R_{eq} \approx 8.33\,\Omega $$

### Step 4: Calculate Total Current ($I$)

We use Ohm's Law again, using the new equivalent resistance. To avoid rounding errors, it is best to use the exact fraction ($\frac{150}{18}$) from the previous step.

$$ I = \frac{V}{R_{eq}} $$

$$ I = \frac{12}{150 / 18} $$

$$ I = \frac{12 \times 18}{150} $$

$$ I = 1.44\,\text{A} $$
