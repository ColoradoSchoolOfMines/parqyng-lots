
from pynq.overlays.base import BaseOverlay
import time
base = BaseOverlay('base.bit')
spacing = 1.8

from requests_futures.sessions import FuturesSession
server = "http://192.168.112.82:8080"
session = FuturesSession()
f_params = session.post(server + '/register?lot=1')
def log_to_server(n):
    params = f_params.result().json()
    if n > 0:
        params["enter"] = n
    else:
        params["exit"] = -n
    session.post(server + "/report", json=params)

from pynq.lib.pmod import *
from pynq.lib.arduino import Grove_Buzzer as A_Grove_Buzzer, ARDUINO_GROVE_G1

sensors = [Grove_PIR(base.PMODA, port) for port in (PMOD_GROVE_G1, PMOD_GROVE_G2)]
bar = Grove_LEDbar(base.PMODB, PMOD_GROVE_G4)
buzz = A_Grove_Buzzer(base.ARDUINO, ARDUINO_GROVE_G1)

def tone_asc():
    buzz.play_tone(494, 428)
    buzz.play_tone(659, 428)
    
def tone_desc():
    buzz.play_tone(659, 428)
    buzz.play_tone(494, 428)

ct = 0
detect = [0 for s in sensors]
last = [s.read() for s in sensors]
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
                ct += [-1, 1][i]
                [tone_desc, tone_asc][i]()
                log_to_server([-1, 1][i])
                print("in" if i else "out", "| count", ct, "|", spacing/(clock - detect[not i]), "m/s")
                detect[not i] = 0
            elif r:
                detect[i] = clock
    detect = [0 if clock - 10 > v else v for v in detect]
    bar.write_binary(display)
