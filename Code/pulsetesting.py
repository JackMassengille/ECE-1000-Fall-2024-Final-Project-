from machine import ADC
import time

# Pulse sensor setup
pulse_pin = ADC(26)  # ADC pin for pulse sensor

# Step 1: Calculate baseline
print("Calculating baseline...")
baseline = sum([pulse_pin.read_u16() for _ in range(1000)]) // 1000  # Average of 100 readings
print(f"Baseline Value: {baseline}")

# Step 2: Set threshold
offset = 1000  # Adjust this based on your sensor's behavior
threshold = baseline + offset
print(f"Threshold Value: {threshold}")

# Step 3: Monitor pulse and debug
print("Monitoring pulse...")
while True:
    pulse_value = pulse_pin.read_u16()  # Read analog value
    if pulse_value > threshold:
        print(f"Pulse detected! Value: {pulse_value}")
    else:
        print(f"Below threshold. Value: {pulse_value}")
    
    time.sleep(0.1)  # Small delay