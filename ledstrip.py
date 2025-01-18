from gpiozero import LED, PWMLED
from signal import pause
import time


leds = LEDBoard(red=17, green=22, blue=24)
print(leds)

leds.on()
time.sleep(1)
leds.off()
time.sleep(1)
leds.color(255, 0, 0)
time.sleep(1)
leds.color(0, 255, 0)
time.sleep(1)
leds.color(0, 0, 255)
time.sleep(1)
leds.color(255, 255, 0)
time.sleep(1)
leds.color(115, 79, 150)
time.sleep(3)

pause()