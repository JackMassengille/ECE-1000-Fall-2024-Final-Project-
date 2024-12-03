# Heartbeat Sensor
This GitHub contains all relevant files used during development of our heartbeat sensor project for ECE 1000.
## Project Summary
The heartbeat sensor is designed to measure a persons heartbeat through them placing their finger on the sensor.  It incorporates a Raspberry Pi Pico microcontroller, an OLED display, and an infered light heartbeat sensor.

The primary goal of this project was to get a decently accurate read on a persons beats per minute and display the the reading and BPM on the OLED screen.  The heatbeat sensor we have however does not give super accurate readings and heavily depends on the pressure of your finger, lighting, and many other small factors.  This made it very hard to make the Sensor detect when a finger is on it which was slightly dissapointing but nonetheless it does print a bpm somewhat accurate if you apply the right pressure to the sensor.

## Project Capabilities 
The Heartbeat sensor a couple of key capabilities including:

* Translating the raw data from the sensor to BPM.
* Printing the BPM and the raw data to the OLED display.

## Who Are We?

* Dr. Indranil Bhattacharya - Professor and Department Chair
* John Caleb (JC) Williams - Graduate Assistant
* Storm Johnson - Graduate Assistant
* Jack Massengille - Freshman Electrical Engineer Undergrad
* Anthony Pfaff - Freshman Computer Engineer Undergrad

* Project Stakeholders - This project was developed for anyone who wants to get a decently accurate heartbeat from the touch of a finger.
