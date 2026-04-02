## 7. Dynamics with Friction

A 5 kg block is placed on a 10 kg block. A horizontal force of 45 N is applied to the 10 kg block, and the 5 kg block is tied to the wall. The coefficient of kinetic friction between all moving surfaces is 0.2. Find the acceleration of the 10 kg block.

---

### Variable Definitions

Before solving the problem, here is a breakdown of the variables used in this system:

* **$m_1$**: The mass of the top block (5 kg). Measured in kilograms (kg).
* **$m_2$**: The mass of the bottom block (10 kg). Measured in kilograms (kg).
* **$F_{app}$**: The horizontal pulling force applied to the bottom block (45 N). Measured in Newtons (N).
* **$\mu_k$**: The coefficient of kinetic friction (0.2). This is a dimensionless ratio representing the roughness between the surfaces.
* **$g$**: The acceleration due to gravity (approximately 9.81 m/s²). Measured in meters per second squared (m/s²).
* **$N$**: Normal force, which is the perpendicular contact force exerted by a surface. Measured in Newtons (N).
* **$f_k$**: Kinetic friction force, which opposes the sliding motion of surfaces. Measured in Newtons (N).
* **$a$**: The acceleration of the bottom block. Measured in meters per second squared (m/s²).

---

### Step-by-Step Solution



**Goal:** Find the acceleration ($a$) of the 10 kg block.

**Step 1: Analyze the forces acting on the 10 kg block ($m_2$).**
The 10 kg block is being pulled forward by the applied force ($F_{app}$). However, it is experiencing friction from **two** different surfaces that oppose its motion:
1.  Friction from the ground below it ($f_{k2}$).
2.  Friction from the 5 kg block above it ($f_{k1}$), because the 5 kg block is tied to the wall and scrapes against the top of the 10 kg block as it slides away.

**Step 2: Calculate the normal forces.**
To find friction, we first need the normal force at each surface.
* **Surface 1 (between the two blocks):** The normal force ($N_1$) is simply the weight of the top block pressing down.
    $$N_1 = m_1g$$
    $$N_1 = 5 \cdot 9.81 = 49.05 \text{ N}$$
* **Surface 2 (between the bottom block and the ground):** The ground must support the weight of *both* blocks.
    $$N_2 = (m_1 + m_2)g$$
    $$N_2 = (5 + 10) \cdot 9.81 = 15 \cdot 9.81 = 147.15 \text{ N}$$

**Step 3: Calculate the kinetic friction forces.**
The formula for kinetic friction is $f_k = \mu_k \cdot N$. We are given that $\mu_k = 0.2$ for all moving surfaces.
* **Friction from the top block:**
    $$f_{k1} = \mu_k \cdot N_1$$
    $$f_{k1} = 0.2 \cdot 49.05 = 9.81 \text{ N}$$
* **Friction from the ground:**
    $$f_{k2} = \mu_k \cdot N_2$$
    $$f_{k2} = 0.2 \cdot 147.15 = 29.43 \text{ N}$$

**Step 4: Calculate the net force on the 10 kg block.**
The net horizontal force ($F_{net}$) is the applied pulling force minus the total friction opposing the movement. 
$$F_{net} = F_{app} - f_{k1} - f_{k2}$$
$$F_{net} = 45 - 9.81 - 29.43$$
$$F_{net} = 45 - 39.24$$
$$F_{net} = 5.76 \text{ N}$$

**Step 5: Calculate the acceleration.**
Using Newton's Second Law ($F = ma$), we can find the acceleration of the 10 kg block.
$$F_{net} = m_2a$$
$$a = \frac{F_{net}}{m_2}$$
$$a = \frac{5.76}{10}$$
$$a = 0.576$$

**Answer:** The acceleration of the 10 kg block is **0.576 m/s²**. *(Note: If using $g = 9.8$ m/s², the acceleration calculates exactly to 0.58 m/s²)*.