
# coding: utf-8

# In[1]:


from pynq.overlays.base import BaseOverlay
base = BaseOverlay('base.bit')


# In[2]:


from pynq.lib.pmod import *


# In[4]:


sensors = [Grove_PIR(base.PMODA, port) for port in (PMOD_GROVE_G1, PMOD_GROVE_G2)]
bar = Grove_LEDbar(base.PMODB, PMOD_GROVE_G4)


# In[ ]:


while True:
    display = 0
    for i, s in enumerate(sensors):
        display |= s.read() << i
    bar.write_binary(display)

