from gpiozero import LED, PWMLED, LEDBoard
from signal import pause
import time


leds = LEDBoard(red=17, green=22, blue=24)
print(leds)

leds.on()
time.sleep(1)
leds.off()
time.sleep(1)
leds.red.on()
time.sleep(1)
leds.green.on()
time.sleep(1)
leds.blue.on()

pause()