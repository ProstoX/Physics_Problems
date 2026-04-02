## 1. Gravitational Dependence

A simple pendulum has a period of 4 seconds on Earth. What would its period be on the Moon, where the gravitational acceleration is about 1/6th of Earth's?

What is the required length of a simple pendulum to have a period of exactly 1 second on Earth?

---

### Variable Definitions

Before diving into the calculations, here is a quick breakdown of the variables used in the simple pendulum formula:

* **$T$**: The period of the pendulum. This represents the time it takes for the pendulum to complete one full swing (back and forth). It is measured in seconds (s).
* **$L$**: The length of the pendulum. This is the distance from the pivot point to the center of mass of the pendulum bob. It is measured in meters (m).
* **$g$**: The acceleration due to gravity. This represents the strength of the gravitational pull acting on the pendulum. It is measured in meters per second squared (m/s²). On Earth, this is approximately 9.81 m/s².

---

### Part 1: Period on the Moon

**Goal:** Find the period of a pendulum on the Moon given that its period on Earth is 4 seconds, and the Moon's gravity is 1/6th of Earth's gravity.

**Step 1: State the governing formula.**
The formula for the period of a simple pendulum is:
$$T = 2\pi\sqrt{\frac{L}{g}}$$

**Step 2: Set up the equations for Earth and the Moon.**
For Earth, the period is $T_{Earth} = 4$ seconds. 
$$T_{Earth} = 2\pi\sqrt{\frac{L}{g_{Earth}}} = 4$$

For the Moon, the gravity is $g_{Moon} = \frac{g_{Earth}}{6}$. We want to find $T_{Moon}$:
$$T_{Moon} = 2\pi\sqrt{\frac{L}{g_{Moon}}}$$

**Step 3: Substitute the Moon's gravity into the equation.**
Replace $g_{Moon}$ with $\frac{g_{Earth}}{6}$:
$$T_{Moon} = 2\pi\sqrt{\frac{L}{\frac{g_{Earth}}{6}}}$$

**Step 4: Simplify the expression.**
When dividing by a fraction, you multiply by its reciprocal. Move the 6 to the numerator:
$$T_{Moon} = 2\pi\sqrt{\frac{6L}{g_{Earth}}}$$

**Step 5: Factor out the square root of 6.**
$$T_{Moon} = \sqrt{6} \cdot \left( 2\pi\sqrt{\frac{L}{g_{Earth}}} \right)$$

**Step 6: Substitute the Earth period back in and solve.**
Notice that the expression inside the parentheses is exactly equal to $T_{Earth}$ (which is 4 seconds).
$$T_{Moon} = \sqrt{6} \cdot 4$$
$$T_{Moon} \approx 2.449 \cdot 4 \approx 9.80$$

**Answer:** The period of the pendulum on the Moon would be approximately **9.80 seconds**.

---

### Part 2: Required Length for a 1-Second Period

**Goal:** Find the length $L$ required for a simple pendulum to have a period of exactly $T = 1$ second on Earth.

**Step 1: State the formula and the known values.**
* Formula: $T = 2\pi\sqrt{\frac{L}{g}}$
* $T = 1$ s
* $g \approx 9.81$ m/s² (Standard Earth gravity)

**Step 2: Rearrange the formula to solve for $L$.**
First, divide both sides by $2\pi$:
$$\frac{T}{2\pi} = \sqrt{\frac{L}{g}}$$

Next, square both sides to remove the square root:
$$\frac{T^2}{4\pi^2} = \frac{L}{g}$$

Finally, multiply both sides by $g$ to isolate $L$:
$$L = \frac{g \cdot T^2}{4\pi^2}$$

**Step 3: Substitute the known values into the rearranged formula.**
$$L = \frac{9.81 \cdot 1^2}{4\pi^2}$$
$$L = \frac{9.81}{4 \cdot 9.8696}$$
$$L = \frac{9.81}{39.478}$$

**Step 4: Calculate the final length.**
$$L \approx 0.248$$

**Answer:** The required length of the pendulum is approximately **0.248 meters** (or 24.8 centimeters).