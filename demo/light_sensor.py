#! /usr/bin/env python3.6

from time import sleep

from pynq.lib.arduino import ARDUINO_GROVE_I2C, Grove_Light
from pynq.overlays.base import BaseOverlay

base = BaseOverlay("base.bit")
print('base done')

light_sensor = Grove_Light(base.ARDUINO, ARDUINO_GROVE_I2C)

print('INIT COMPLETE')

while True:
    print(light_sensor.read())
    sleep(1)
