
# coding: utf-8

# In[1]:


from pynq.overlays.base import BaseOverlay
base = BaseOverlay('base.bit')


# In[2]:


from pynq.lib.pmod import *


# In[3]:


sensors = [Grove_PIR(base.PMODA, port) for port in (PMOD_GROVE_G1, PMOD_GROVE_G2)]
bar = Grove_LEDbar(base.PMODB, PMOD_GROVE_G4)


# In[ ]:


while True:
    display = 0
    for m, s in zip([0b1111100000, 0b0000011111], sensors):
        display |= s.read() and m
    bar.write_binary(display)

