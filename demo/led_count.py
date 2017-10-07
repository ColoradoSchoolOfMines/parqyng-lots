#!/usr/bin/env python3.6

from time import sleep
from pynq.overlays.base import BaseOverlay

base = BaseOverlay("base.bit")

for led in base.leds:
    led.off()
    
for i in range(16):
    for led in base.leds:
        if i & 1:
            led.on()
        else:
            led.off()
        i >>= 1
    sleep(0.25)
