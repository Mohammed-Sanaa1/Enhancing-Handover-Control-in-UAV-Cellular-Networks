#Random Walk
import numpy as np
import pandas as pd

# Define parameters
num_uavs = 10
num_time_steps = 1000
area_size = (1000, 1000, 500)  # Define the area size where UAVs move in (X, Y, Z)

# Generate random initial positions for UAVs in 3D space
initial_positions = np.random.rand(num_uavs, 3) * area_size

# Define a simple mobility model for 3D space
def mobility_model_3d(current_position):
    # Generate random direction and distance for X, Y, and Z dimensions
    direction = np.random.rand(3) * 2 * np.pi
    distance = np.random.rand() * 50  # Maximum distance UAV can move in one timestep
    
    # Calculate new position based on direction and distance for each dimension
    new_position = current_position + distance * np.array([np.cos(direction[0]), np.sin(direction[0]), np.random.rand()-0.5])
    
    # Ensure new position stays within area bounds for each dimension
    for i in range(3):
        new_position[i] = max(0, min(new_position[i], area_size[i]))
    
    return new_position

# Simulate UAV trajectories in 3D space
uav_trajectories = {}
current_positions = initial_positions.copy()
for t in range(num_time_steps):
    for i in range(num_uavs):
        current_positions[i] = mobility_model_3d(current_positions[i])
        if i not in uav_trajectories:
            uav_trajectories[i] = []
        uav_trajectories[i].append((t, current_positions[i][0], current_positions[i][1], current_positions[i][2]))

# Convert trajectories to DataFrame
trajectory_rows = []

# Simulate UAV trajectories in 3D space
for t in range(num_time_steps):
    for i in range(num_uavs):
        current_positions[i] = mobility_model_3d(current_positions[i])
        trajectory_rows.append({'UAV_ID': i, 'Time_Step': t, 'X': current_positions[i][0], 'Y': current_positions[i][1], 'Z': current_positions[i][2]})

# Convert trajectory rows to DataFrame
trajectory_data = pd.DataFrame(trajectory_rows)

# Save trajectory data to CSV
trajectory_data.to_csv('uav_trajectory_data_random_walk.csv', index=False)