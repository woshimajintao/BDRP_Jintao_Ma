import mujoco
from mujoco import MjModel, MjData
import pickle
import os

# Define the model path
MODEL_PATH = os.path.expanduser("~/Downloads/arm26.xml")  # Replace with the actual model path

# Define the output path
OUTPUT_PATH = os.path.expanduser("~/Downloads/simulation_data.pkl")

# Load the model and data
model = MjModel.from_xml_path(MODEL_PATH)
data = MjData(model)

# Dictionary to store simulation data
simulation_data = {
    "time": [],
    "qpos": [],  # Joint positions
    "qvel": [],  # Joint velocities
    "ctrl": []   # Control inputs (if control inputs are present)
}

# Run the simulation
print("Starting simulation...")
for step in range(1000):  # Run the simulation for 1000 steps
    mujoco.mj_step(model, data)
    
    # Save the simulation data
    simulation_data["time"].append(data.time)
    simulation_data["qpos"].append(data.qpos.copy())
    simulation_data["qvel"].append(data.qvel.copy())
    simulation_data["ctrl"].append(data.ctrl.copy() if data.ctrl is not None else None)

print("Simulation complete. Saving data...")

# Save the data as a .pkl file
with open(OUTPUT_PATH, "wb") as f:
    pickle.dump(simulation_data, f)

print(f"Simulation data has been saved to {OUTPUT_PATH}")
