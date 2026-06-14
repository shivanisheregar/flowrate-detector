
from src.flow_calculator import calculate_flow_rate

volume = 1000
time_taken = 5

flow_rate = calculate_flow_rate(volume, time_taken)

print("Volume:", volume, "mL")
print("Time:", time_taken, "s")
print("Flow Rate:", flow_rate, "mL/s")
