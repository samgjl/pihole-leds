import RPi.GPIO as GPIO
from gpiozero import LED, PWMLED
from signal import pause
import time

RED = PWMLED(17)
GREEN = PWMLED(22)
BLUE = PWMLED(24)
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
 
def color(r: float, g: float, b: float):
    RED.value = r
    GREEN.value = g
    BLUE.value = b

def on():
    RED.on()
    GREEN.on()
    BLUE.on()

def off():
    RED.off()
    GREEN.off()
    BLUE.off()

if __name__ == "__main__":
    on()
    time.sleep(3)
    off()
    time.sleep(3)
    color(1, 0, 0)
    time.sleep(3)
    color(0, 1, 0)
    time.sleep(3)
    color(0, 0, 1)
    time.sleep(3)
    color(1, 1, 1)
    time.sleep(3)