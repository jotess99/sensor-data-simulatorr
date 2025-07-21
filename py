import random
import time

print("Starting motor sensor data simulation...\n")

for i in range(5):
    voltage = random.randint(210, 240)
    temperature = random.randint(40, 80)
    vibration = random.uniform(0.5, 3.5)

    print(f"Voltage: {voltage}V | Temperature: {temperature}°C | Vibration: {vibration:.2f} m/s²")
    time.sleep(1)
