# Author: Jack Massengille
# Date: 12-1-24
# Source:  chat GPT and blog: https://peppe8o.com

from machine import Pin, I2C, ADC
import ssd1306
import time

# OLED setup
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Pulse sensor setup
pulse_pin = ADC(26)  # ADC pin for pulse sensor

# Calibration for baseline and threshold
print("Calibrating... Please remove your finger from the sensor.")
time.sleep(2)
baseline = sum([pulse_pin.read_u16() for _ in range(100)]) // 100
threshold = baseline + 800  # Adjust offset as needed
print(f"Calibration complete. Baseline: {baseline}, Threshold: {threshold}")

# Variables for BPM calculation
last_peak_time = 0
bpm = 0
peak_detected = False
readings = []  # For moving average
max_readings = 10  # Adjust for smoothing

# Main loop
while True:
    pulse_value = pulse_pin.read_u16()  # Read analog value
    readings.append(pulse_value)
    if len(readings) > max_readings:
        readings.pop(0)
    smoothed_pulse_value = sum(readings) // len(readings)

    current_time = time.ticks_ms()  # Current time in milliseconds

    # Peak detection logic with minimum time gap
    if smoothed_pulse_value > threshold and not peak_detected:
        peak_detected = True
        if last_peak_time != 0:  # Skip first reading
            time_diff = time.ticks_diff(current_time, last_peak_time)
            if time_diff > 300:  # Minimum 300ms (~200 BPM max)
                bpm = 60000 // time_diff  # Convert to BPM
        last_peak_time = current_time

    if smoothed_pulse_value < threshold:
        peak_detected = False

    # Filter unrealistic BPM values
    if not (40 <= bpm <= 200):
        bpm = 0  # Ignore invalid values

    # Display data on OLED
    oled.fill(0)  # Clear the screen
    oled.text("Heartbeat Sensor", 0, 0)
    oled.text(f"Pulse: {smoothed_pulse_value}", 0, 20)
    oled.text(f"BPM: {bpm}", 0, 40)
    oled.show()

    time.sleep(0.1)  # Small delay