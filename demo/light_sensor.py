#! /usr/bin/env python3.6

from time import sleep

from pynq.lib.arduino import ARDUINO_GROVE_I2C, Grove_Light
from pynq.overlays.base import BaseOverlay

base = BaseOverlay("base.bit")

# Note that you need an ADC to I2C board
light_sensor = Grove_Light(base.ARDUINO, ARDUINO_GROVE_I2C)

while True:
    print(light_sensor.read())
    sleep(1)
