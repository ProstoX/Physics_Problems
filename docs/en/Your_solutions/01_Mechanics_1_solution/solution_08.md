### Variables and Units Glossary

Before we calculate the solution, here is a breakdown of the mathematical symbols used in this problem and their standard SI units:

* **$a_c$ (Centripetal Acceleration):** The acceleration directed toward the center of a circular path that keeps an object moving in a circle. Measured in meters per second squared ($\text{m/s}^2$).
* **$R$ (Radius):** The distance from the center of the Earth to the equator. Measured in meters ($\text{m}$).
* **$T$ (Period):** The time it takes for the Earth to complete one full rotation on its axis. Measured in seconds ($\text{s}$).
* **$v$ (Tangential Velocity):** The linear speed of a person standing on the equator as the Earth spins. Measured in meters per second ($\text{m/s}$).
* **$\pi$ (Pi):** A mathematical constant representing the ratio of a circle's circumference to its diameter, approximately 3.14159.

---

### Step-by-Step Solution

#### 1. Convert Given Values to Standard SI Units
To use standard physics equations, we must convert our distance into meters and our time into seconds. 

* **Radius ($R$):** The problem gives $R = 6378 \text{ km}$.
  $$R = 6378 \times 1000 = 6,378,000 \text{ m}$$

* **Period ($T$):** The problem implicitly assumes standard Earth rotation. The Earth completes one full rotation every 24 hours.
  $$T = 24 \text{ hours} \times 60 \text{ minutes/hour} \times 60 \text{ seconds/minute}$$
  $$T = 86,400 \text{ s}$$

#### 2. Calculate Tangential Velocity ($v$)
Before we can find the acceleration, we need to know how fast a person on the equator is actually moving through space. The distance traveled in one full rotation is the circumference of the Earth ($C = 2\pi R$).

Velocity is distance divided by time:
$$v = \frac{2\pi R}{T}$$

Plugging in our values:
$$v = \frac{2 \pi (6,378,000)}{86,400}$$
$$v = \frac{40,074,155.89}{86,400} \approx 463.82 \text{ m/s}$$
*(A person at the equator is moving at roughly 464 m/s, or over 1000 mph!)*

#### 3. Calculate Centripetal Acceleration ($a_c$)
Centripetal acceleration is the square of the tangential velocity divided by the radius of the circular path.

$$a_c = \frac{v^2}{R}$$

Plugging in our calculated velocity and the Earth's radius:
$$a_c = \frac{(463.82)^2}{6,378,000}$$
$$a_c = \frac{215,129.59}{6,378,000} \approx 0.0337 \text{ m/s}^2$$

**Conclusion:** The centripetal acceleration of a person standing on the Earth's equator is approximately **$0.0337 \text{ m/s}^2$** directed toward the center of the Earth.


*Visualization is available at [solution_08.html](solution_08.html)*