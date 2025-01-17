#Random Waypoint Model

import numpy as np
import pandas as pd

# Define parameters
num_uavs = 10
num_time_steps = 1000
area_size = (1000, 1000, 500)  # Define the area size where UAVs move (X, Y, Z)
max_speed = 10  # Maximum speed of UAVs
max_acceleration = 2  # Maximum acceleration of UAVs
max_altitude = 500  # Maximum altitude of UAVs

# Generate random initial positions, speeds, accelerations, and altitudes for UAVs in 3D
initial_positions = np.random.rand(num_uavs, 3) * area_size
initial_speeds = np.random.rand(num_uavs) * max_speed
initial_accelerations = np.random.rand(num_uavs) * max_acceleration
initial_altitudes = np.random.rand(num_uavs) * max_altitude

# Define a more realistic mobility model: Random Waypoint with Speed and Acceleration
def random_waypoint(current_position, current_speed, current_acceleration, area_size, max_speed, max_acceleration):
    target = np.random.rand(3) * area_size  # Random waypoint within the area
    direction = target - current_position
    distance = np.linalg.norm(direction)
    speed = min(current_speed + current_acceleration, max_speed)
    if distance == 0:
        return current_position, 0  # No movement, speed becomes 0
    else:
        return current_position + direction * (speed / distance), speed

# Simulate UAV trajectories
uav_trajectories = {}
current_positions = initial_positions.copy()
current_speeds = initial_speeds.copy()
current_accelerations = initial_accelerations.copy()
current_altitudes = initial_altitudes.copy()

for t in range(num_time_steps):
    for i in range(num_uavs):
        current_positions[i], current_speeds[i] = random_waypoint(current_positions[i], current_speeds[i], current_accelerations[i], area_size, max_speed, max_acceleration)
        if i not in uav_trajectories:
            uav_trajectories[i] = []
        uav_trajectories[i].append((t, current_positions[i][0], current_positions[i][1], current_positions[i][2], current_speeds[i], current_accelerations[i], current_altitudes[i]))

# Convert trajectories to DataFrame
trajectory_rows = []
for uav_id, trajectory in uav_trajectories.items():
    for time_step, x, y, z, speed, acceleration, altitude in trajectory:
        trajectory_rows.append({'UAV_ID': uav_id, 'Time_Step': time_step, 'X': x, 'Y': y, 'Z': z, 'Speed': speed, 'Acceleration': acceleration, 'Altitude': altitude})

trajectory_data = pd.DataFrame(trajectory_rows)
# Save trajectory data to CSV
trajectory_data.to_csv('uav_trajectory_data_random_waypoint.csv', index=False)
