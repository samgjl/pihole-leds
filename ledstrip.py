from gpiozero import LED, PWMLED, LEDBoard
from signal import pause
import time


leds = LEDBoard(red=17, green=22, blue=24)
print(leds)

# while True:
#     leds.value = (1, 0, 0)
leds.value = (0.01, 0.01, 0.01)

pause()