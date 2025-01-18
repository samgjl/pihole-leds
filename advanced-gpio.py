from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

try:
    while True:
        for value in range(0, 101, 5):
            led.value = value / 100  # PWMLED value must be between 0 and 1
            sleep(0.1)
        for value in range(100, -1, -5):
            led.value = value / 100
            sleep(0.1)
except KeyboardInterrupt:
    pass
