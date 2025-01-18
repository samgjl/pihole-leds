import RPi.GPIO as GPIO
from gpiozero import LED, PWMLED
from signal import pause
import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(17, GPIO.OUT)
# GPIO.setup(22, GPIO.OUT)
# GPIO.setup(24, GPIO.OUT)

RED = PWMLED(17, frequency=1000)
GREEN = PWMLED(22, frequency=1000)
BLUE = PWMLED(24, frequency=1000)
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
    RED.value = r/255
    GREEN.value = g/255
    BLUE.value = b/255

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
    time.sleep(1)
    off()
    time.sleep(1)
    color(255, 0, 0)
    time.sleep(1)
    color(0, 255, 0)
    time.sleep(1)
    color(0, 0, 255)
    time.sleep(1)
    color(255, 255, 0)
    time.sleep(1)
    off()
    time.sleep(1)
    color(115, 79, 150)
    time.sleep(3)