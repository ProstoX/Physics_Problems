import numpy as np
import matplotlib.pyplot as plt

# --- Physical Constants & Initial Conditions ---
m = 1.0       # Mass (kg)
g = 9.81      # Gravity (m/s^2)
k = 0.5       # Drag coefficient (kg/s)
v0 = 25.0     # Initial upward velocity (m/s)
x0 = 10.0     # Initial height (m)

dt = 0.01     # Time step for numerical integration (s)
t_end = 4.0   # Total simulation time (s)

# --- Arrays for Numerical Simulation ---
t = np.arange(0, t_end, dt)
v_num = np.zeros(len(t))
x_num = np.zeros(len(t))
v_num[0] = v0
x_num[0] = x0

# --- Euler Method Integration ---
for i in range(1, len(t)):
    # Calculate acceleration (dv/dt) at current step
    dv_dt = -g - (k/m) * v_num[i-1]
    
    # Update velocity and position
    v_num[i] = v_num[i-1] + dv_dt * dt
    x_num[i] = x_num[i-1] + v_num[i-1] * dt

# --- Ideal Case (No Drag) for Comparison ---
v_ideal = v0 - g * t
x_ideal = x0 + v0 * t - 0.5 * g * t**2

# --- Plotting the Results ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Position Plot
ax1.plot(t, x_num, label='With Drag (Numeric)', color='red', linewidth=2)
ax1.plot(t, x_ideal, label='No Drag (Analytical)', color='blue', linestyle='--')
ax1.set_title('Vertical Position over Time')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Height (m)')
ax1.grid(True)
ax1.legend()

# Velocity Plot
ax2.plot(t, v_num, label='With Drag (Numeric)', color='red', linewidth=2)
ax2.plot(t, v_ideal, label='No Drag (Analytical)', color='blue', linestyle='--')
ax2.axhline(0, color='black', linewidth=1) # Zero velocity line
ax2.set_title('Vertical Velocity over Time')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Velocity (m/s)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()