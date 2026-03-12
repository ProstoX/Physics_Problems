### Transforming from Verbal to Mathematically Formal

When reading this problem, the immediate instinct is often to calculate the distance of the fly's first trip to the wall, then calculate where the bicycle is, then calculate the distance of the return trip, and so on. This creates an infinite geometric series.

However, the mathematically formal (and much simpler) way to approach this is to change the perspective from **distance** to **time**.

1. **The constraint:** The fly moves continuously until the bicycle reaches the wall. Therefore, the total time the fly is flying is exactly equal to the total time it takes for the bicycle to reach the wall.
2. **The formalization:** Instead of summing distances ($d_1 + d_2 + d_3 + \dots$), we use the fundamental kinematic equation $d = v \cdot t$. We can find the total time ($t$) using the bicycle's parameters, and then apply that same time ($t$) to the fly's speed to find the fly's total distance.

---

### Formula Variables and Constants

Here is what each letter in our equations will represent:

* **$D_{bike}$ (Initial distance of the bicycle):** The starting distance between the bicycle and the wall.
* **Type:** Constant for this specific problem
* **Value:** 10 m


* **$v_{bike}$ (Speed of the bicycle):** The constant velocity at which the bicycle approaches the wall.
* **Type:** Constant
* **Value:** 1 m/s


* **$v_{fly}$ (Speed of the fly):** The constant speed of the fly as it zips back and forth.
* **Type:** Constant
* **Value:** 2 m/s


* **$t$ (Total time):** The duration of the event from the start until the bicycle hits the wall.
* **Type:** Variable (to be calculated)
* **Unit:** Seconds (s)


* **$D_{fly}$ (Total distance of the fly):** The final accumulated distance the fly travels.
* **Type:** Variable (to be calculated)
* **Unit:** Meters (m)


---

### Step 1: Calculate the Total Time

First, we determine how long the bicycle travels before it hits the wall. We use the standard distance formula, rearranged to solve for time:


$$t = \frac{D_{bike}}{v_{bike}}$$

Substitute the known values for the bicycle:


$$t = \frac{10}{1}$$

$$t = 10$$

The total time the bicycle is in motion (and therefore the total time the fly is flying) is **10 seconds**.

### Step 2: Calculate the Fly's Total Distance

Now that we have the total time constraint, we can figure out how far the fly traveled during those 10 seconds. The fly's constant changes of direction do not matter because its speed remains constant and we are looking for the total path distance (a scalar quantity), not displacement.

We use the distance formula again, this time for the fly:


$$D_{fly} = v_{fly} \cdot t$$

Substitute the fly's speed and the time we just calculated:


$$D_{fly} = 2 \cdot 10$$

$$D_{fly} = 20$$

### Final Answer

The total distance the fly travels before being crushed is **20 meters**.