import RPi.GPIO as GPIO
from gpiozero import LED
from signal import pause
import time

RED = LED(17)
GREEN = LED(22)
BLUE = LED(24)
"""
We're using a 3-pin LED strip, so we can control each color individually.
the pins are as follows:
GPIO Control:
    Red     GPIO 17
    Green   GPIO 22
    Blue    GPIO 24
"""

print([RED, GREEN, BLUE])
# print([RED.pin, GREEN.pin, BLUE.pin])
# print([RED.on(), GREEN.on(), BLUE.on()])
RED.on()
time.sleep(1)
RED.off()
GREEN.on()
time.sleep(1)
GREEN.off()
BLUE.on()
time.sleep(1)
BLUE.off()
pause()
