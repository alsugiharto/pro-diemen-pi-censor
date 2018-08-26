
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

# Gain = 2/3 for reading voltages from 0 to 6.144V.
# See table 3 in ADS1115 datasheet
GAIN = 2/3

# Main loop.
while 1:
    value = [0]
    # Read ADC channel 0
    value[0] = adc.read_adc(0, gain=GAIN)
    # Ratio of 15 bit value to max volts determines volts
    volts = value[0] / 32767.0 * 6.144
    # Tests shows linear relationship between psi & voltage:
    psi = 50.0 * volts - 25.0
    # Bar conversion
    bar = psi * 0.0689475729

    print("\n{0:0.0f} psi".format(psi))

    sleep(1)
~
