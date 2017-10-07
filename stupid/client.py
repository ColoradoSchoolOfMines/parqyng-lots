from pynq import PL
from pynq.overlays.base import BaseOverlay
from pynq.lib.pmod import *
from pynq.lib.arduino import Grove_Buzzer as A_Grove_Buzzer, ARDUINO_GROVE_G1
import time
import psutil
import threading
from concurrent.futures import ThreadPoolExecutor

import node

base = BaseOverlay('base.bit')

sensors = [Grove_PIR(base.PMODA, port) for port in (PMOD_GROVE_G1, PMOD_GROVE_G2)]
bar = Grove_LEDbar(base.PMODB, PMOD_GROVE_G4)
buzz = A_Grove_Buzzer(base.ARDUINO, ARDUINO_GROVE_G1)

def tone_asc():
    buzz.play_tone(494, 428)
    buzz.play_tone(659, 428)
    
def tone_desc():
    buzz.play_tone(659, 428)
    buzz.play_tone(494, 428)

def node_client(data, sync):
    n = node.connect()
    while True:
        # Do updates every t
        time.sleep(n.cfg['period'] or 2.0)

        # Update with data
        sync.acquire()
        n.enter += data['enter']
        n.exit += data['exit']
        data['enter'] = 0
        data['exit'] = 0
        data['spacing'] = n.cfg['spacing']
        data['delay'] = n.cfg['delay']
        sync.release()

        # Send report and get car count back
        res = n.send_report()
        cars = res.get('cars_in_lot')
        if cars is not None:
            sync.acquire()
            data['cars'] = cars
            sync.release()

        print('update finished')

def node_sensors(data, executor, sync):
    detect = [0 for s in sensors]
    last = [s.read() for s in sensors]
    delay = 0

    while True:
        display = 0
        for m, i, s in zip([0b1111100000, 0b0000011111], [0, 1], sensors):
            r = s.read()
            clock = time.process_time()
            display |= r and m
            if r != last[i]:
                # change in sensor output
                last[i] = r
                if r and detect[not i]:
                    sync.acquire()
                    executor.submit([tone_desc, tone_asc][i])
                    data['enter' if i else 'exit'] += 1
                    spacing = data['spacing'] or 1.8
                    delay = data['delay']
                    sync.release()

                    print('in' if i else 'out', spacing/(clock - detect[not i]), 'm/s')
                    detect[not i] = 0
                elif r:
                    detect[i] = clock

            if delay:
                time.sleep(delay)

        detect = [0 if clock - 10 > v else v for v in detect]
        bar.write_binary(display)

data = {
    'spacing': 1.8,
    'enter': 0,
    'exit': 0,
    'cars': None,
}
sync = threading.Lock()

executor = ThreadPoolExecutor(max_workers=4)
executor.submit(node_client, data, sync)
executor.submit(node_sensors, data, executor, sync)
