from machine import Pin, I2C, ADC
import ssd1306
import time

# OLED setup
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Pulse sensor setup
pulse_pin = ADC(26)  # ADC pin for pulse sensor

# Variables for BPM calculation
baseline = sum([pulse_pin.read_u16() for _ in range(100)]) // 100
threshold = baseline + 1000 # Adjust based on your pulse sensor readings
last_peak_time = 0
bpm = 0
peak_detected = False

# Main loop
while True:
    pulse_value = pulse_pin.read_u16()  # Read analog value
    current_time = time.ticks_ms()  # Current time in milliseconds

    # Peak detection logic
    if pulse_value > threshold and not peak_detected:
        peak_detected = True
        if last_peak_time != 0:  # Skip first reading
            time_diff = time.ticks_diff(current_time, last_peak_time)  # Time between peaks
            bpm = 60000 // time_diff  # Convert to BPM (60000 ms in a minute)
        last_peak_time = current_time

    if pulse_value < threshold:
        peak_detected = False

    # Display data on OLED
    oled.fill(0)  # Clear the screen
    oled.text("Heartbeat Sensor", 0, 0)
    oled.text(f"Pulse: {pulse_value}", 0, 20)
    oled.text(f"BPM: {bpm}", 0, 40)
    oled.show()

    time.sleep(0.1)  # Small delay