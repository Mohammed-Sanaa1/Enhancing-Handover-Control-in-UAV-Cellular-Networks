#Probabilistic Movement
import numpy as np
import pandas as pd

# Define parameters
num_uavs = 10
num_time_steps = 1000
area_size = (1000, 1000, 500)  # Define the area size where UAVs move (X, Y, Z)

# Generate random initial positions for UAVs in 3D
initial_positions = np.random.rand(num_uavs, 3) * area_size

# Define a probabilistic movement model
def probabilistic_movement(current_position):
    # Implement your probabilistic movement logic here
    # This could involve analyzing real-world data to determine probabilities
    # for different actions (e.g., moving to specific locations, following paths, etc.)
    # For demonstration purposes, we'll use a simple example of movement towards the center
    
    center = np.array(area_size) / 2  # Center of the area
    direction = center - current_position
    distance = np.linalg.norm(direction)
    
    # Define probabilities of movement based on distance from the center
    probability_to_move = 1 / (distance + 1)  # Example: Higher probability to move when closer to the center
    
    # Determine whether to move based on probability
    if np.random.rand() < probability_to_move:
        # Move towards the center
        speed = min(distance, 10)  # Limit speed to avoid overshooting
        new_position = current_position + direction * (speed / distance)
    else:
        # Stay in the current position
        new_position = current_position
    
    # Ensure new position stays within area bounds
    new_position = np.maximum(0, np.minimum(new_position, area_size))
    
    return new_position

# Simulate UAV trajectories
uav_trajectories = {}
current_positions = initial_positions.copy()
for t in range(num_time_steps):
    for i in range(num_uavs):
        current_positions[i] = probabilistic_movement(current_positions[i])
        if i not in uav_trajectories:
            uav_trajectories[i] = []
        uav_trajectories[i].append((t, current_positions[i][0], current_positions[i][1], current_positions[i][2]))

trajectory_rows = []

# Simulate UAV trajectories
for t in range(num_time_steps):
    for i in range(num_uavs):
        current_positions[i] = probabilistic_movement(current_positions[i])
        trajectory_rows.append({'UAV_ID': i, 'Time_Step': t, 'X': current_positions[i][0], 'Y': current_positions[i][1], 'Z': current_positions[i][2]})

# Convert trajectory rows to DataFrame
trajectory_data = pd.DataFrame(trajectory_rows)

# Save trajectory data to CSV
trajectory_data.to_csv('uav_trajectory_data_probabilistic.csv', index=False)
