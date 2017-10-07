#!/usr/bin/env python3.6

import bnn
from PIL import Image as PIL_Image
from PIL import ImageEnhance
from PIL import ImageOps
import numpy as np
import math
from array import *

print(bnn.available_params(bnn.NETWORK_LFC))

classifier = bnn.PynqBNN(network=bnn.NETWORK_LFC)

classifier.load_parameters("mnist")

img_path = "car2.jpg"

img = PIL_Image.open(img_path).convert("L")
'''
img = contr.enhance(3)
bright = ImageEnhance.Brightness(img)
img = bright.enhance(4.0)
'''

small_img = img.resize((28,28))
small_img = ImageOps.invert(small_img)

data_image = array('B')

pixel = small_img.load()
for x in range(0, 28):
    for y in range(0, 28):
        data_image.append(pixel[y,x])

hexval = "{0:#0{1}x}".format(1,6)
header = array('B')
header.extend([0,0,8,1,0,0])
header.append(int('0x'+hexval[2:][:2],16))
header.append(int('0x'+hexval[2:][2:],16))
header.extend([0,0,0,28,0,0,0,28])
header[3] = 3 # Changing MSB for image data (0x00000803)

data_image = header + data_image
output_file = open('/home/xilinx/image.images-idx3-ubyte', 'wb')
data_image.tofile(output_file)
output_file.close()

uh = classifier.inference("/home/xilinx/image.images-idx3-ubyte")
print(uh)
