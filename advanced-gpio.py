from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

max = 15
try:
    while True:
        for value in range(0, max, 5):
            led.value = value / 100  # PWMLED value must be between 0 and 1
            print(value)
            sleep(0.1)
        for value in range(max, -1, -5):
            print(value)
            led.value = value / 100
            sleep(0.1)
except KeyboardInterrupt:
    pass
