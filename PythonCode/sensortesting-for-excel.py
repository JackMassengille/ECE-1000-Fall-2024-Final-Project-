
# Author: Jack Massengille
# Date: 11-30-24
# Source:  blog: https://peppe8o.com

from machine import ADC

# setup the Pulse Sensor reading pin
pulse=ADC(28)
file = open("EmptyTest.txt", "w")
x=0

# main program
while x<10000:
    x=x+1
    try:
        value=pulse.read_u16()
        file.write(str(value)+"\n")
        
    except OSError as e:
        machine.reset()
