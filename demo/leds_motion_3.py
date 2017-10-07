
# coding: utf-8

# In[19]:


from pynq.overlays.base import BaseOverlay
import time
base = BaseOverlay('base.bit')
spacing = 1.8


# In[20]:


from pynq.lib.pmod import *


# In[21]:


sensors = [Grove_PIR(base.PMODA, port) for port in (PMOD_GROVE_G1, PMOD_GROVE_G2)]
bar = Grove_LEDbar(base.PMODB, PMOD_GROVE_G4)


# In[ ]:


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
                print("in" if i else "out", "| count", ct, "|", spacing/(clock - detect[not i]), "m/s")
                detect[not i] = 0
            elif r:
                detect[i] = clock
    detect = [0 if clock - 10 > v else v for v in detect]
    bar.write_binary(display)

