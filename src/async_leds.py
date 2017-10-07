#!/usr/bin/env python3.6

from pynq import PL
from pynq.overlays.base import BaseOverlay
import asyncio
import psutil

base = BaseOverlay("base.bit")

@asyncio.coroutine
def flash_led(num):
    while True:
        yield from base.buttons[num].wait_for_value_async(1)
        while base.buttons[num].read():
            base.leds[num].toggle()
            yield from asyncio.sleep(0.1)
        base.leds[num].off()

tasks = [asyncio.ensure_future(flash_led(i)) for i in range(4)]

@asyncio.coroutine
def print_cpu_usage():
    # Calculate the CPU utilisation by the amount of idle time
    # each CPU has had in three second intervals
    last_idle = [c.idle for c in psutil.cpu_times(percpu=True)]
    while True:
        yield from asyncio.sleep(3)
        next_idle = [c.idle for c in psutil.cpu_times(percpu=True)]
        usage = [(1-(c2-c1)/3) * 100 for c1,c2 in zip(last_idle, next_idle)]
        print("CPU Usage: {0:3.2f}%, {1:3.2f}%".format(*usage))
        last_idle = next_idle


tasks.append(asyncio.ensure_future(print_cpu_usage()))

if base.switches[0].read():
    print("Please set switch 0 low before running")
else:
    base.switches[0].wait_for_value(1)

[t.cancel() for t in tasks]
base.switches[0].wait_for_value(0)
