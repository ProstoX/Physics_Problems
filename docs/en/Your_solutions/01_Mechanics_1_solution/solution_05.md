Here is the step-by-step mathematical solution to the relative velocity problem, along with the variable glossary and a prompt to generate an interactive HTML visualization.

### Variables and Units Glossary

Here is a breakdown of the symbols used in this vector problem and their standard units:

* **$\vec{v}_r$ (Velocity of the river):** The speed and direction of the water's current relative to the riverbank. Measured in meters per second (m/s). Given as **2 m/s** East.
* **$\vec{v}_{bw}$ (Velocity of the boat relative to water):** The speed the boat's motor propels it through still water. Measured in m/s. Given as **5 m/s**.
* **$\vec{v}_{bg}$ (Velocity of the boat relative to ground):** The actual, resultant speed and direction the boat travels as observed by someone standing on the shore. Measured in m/s.
* **$\theta$ (Heading Angle):** The angle at which the boat must point itself to counteract the river's current. Measured in degrees (°).
* **$d$ (Distance/Width):** The total width of the river. Measured in meters (m). Given as **200 m**.
* **$t$ (Time):** The total time it takes to cross the river. Measured in seconds (s).

---

### Step-by-Step Solution



#### 1. Set Up the Vector Relationship
To cross the river directly North, the boat must steer into the current (upstream, towards the West) so that the river pushes it perfectly back onto a straight North path. 

This creates a right-angled vector triangle where:
* The actual path across the river ($\vec{v}_{bg}$) is the "straight up" adjacent leg (North).
* The river's current ($\vec{v}_r$) is the horizontal opposite leg (East).
* The boat's heading ($\vec{v}_{bw}$) is the hypotenuse pointing West of North.

The vector equation is: 
$$\vec{v}_{bg} = \vec{v}_{bw} + \vec{v}_r$$

#### 2. Determine the Heading Direction ($\theta$)
To find the angle $\theta$ (measured West of North) that the boat needs to steer, we look at the horizontal (East-West) components. The boat's westward velocity component must perfectly cancel out the river's eastward velocity.

Using trigonometry (SOH CAH TOA), we know the opposite side ($\vec{v}_r$) and the hypotenuse ($\vec{v}_{bw}$):
$$\sin(\theta) = \frac{v_r}{v_{bw}}$$

Plug in the given values:
$$\sin(\theta) = \frac{2}{5} = 0.4$$

Take the inverse sine (arcsin) to find the angle:
$$\theta = \arcsin(0.4) \approx 23.58^\circ$$

The boat must head **23.58° West of North**.

#### 3. Calculate the Resultant Velocity ($\vec{v}_{bg}$)
Now we need to find how fast the boat is actually moving directly North relative to the shore. We can use the Pythagorean theorem ($a^2 + b^2 = c^2$) on our velocity triangle:
$$v_{bg}^2 + v_r^2 = v_{bw}^2$$

Rearrange to solve for $v_{bg}$:
$$v_{bg} = \sqrt{v_{bw}^2 - v_r^2}$$

Plug in the values:
$$v_{bg} = \sqrt{5^2 - 2^2} = \sqrt{25 - 4} = \sqrt{21}$$
$$v_{bg} \approx 4.58 \text{ m/s}$$

Because the boat spends some of its effort fighting the current, its effective speed straight across the river drops to about **4.58 m/s**.

#### 4. Determine the Time to Cross ($t$)
Since we know the straight-line distance across the river ($d$) and the straight-line velocity relative to the ground ($v_{bg}$), we can use the basic kinematic formula ($v = \frac{d}{t}$):
$$t = \frac{d}{v_{bg}}$$

Plug in our exact values:
$$t = \frac{200}{\sqrt{21}} \approx \frac{200}{4.583}$$
$$t \approx 43.64 \text{ s}$$

It will take the boat approximately **43.64 seconds** to reach the opposite shore.


*Visualization is available at [solution_05.html](solution_05.html)*