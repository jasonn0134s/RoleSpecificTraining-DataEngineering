import pandas as pd
import numpy as np

# load csv file
df = pd.read_csv("energy_usage.csv")

# convert timestamp column
df['timestamp'] = pd.to_datetime(df['timestamp'])

# convert energy values to float
df['energy_kwh'] = df['energy_kwh'].astype(float)

# total energy usage
total_energy = np.sum(df['energy_kwh'])

# average energy usage
average_energy = np.mean(df['energy_kwh'])

print("Total Energy Usage:", total_energy)

print("Average Energy Usage:", average_energy)

# room wise summary
room_summary = df.groupby('room_id')['energy_kwh'].sum()

print("\nRoom Wise Energy Summary")

print(room_summary)

# device wise summary
device_summary = df.groupby('device_id')['energy_kwh'].sum()

print("\nDevice Wise Energy Summary")

print(device_summary)