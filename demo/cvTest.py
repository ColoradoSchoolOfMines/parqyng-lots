#!/usr/bin/python3.6

from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
import numpy as np
import cv2
import curses

base = BaseOverlay("base.bit")

stdscr = curses.initscr()
stdscr.nodelay(True)

frame_w = 640 
frame_h = 480

Mode = VideoMode(frame_w, frame_h, 24) 
hdmi_out = base.video.hdmi_out
hdmi_out.configure(Mode, PIXEL_BGR)
hdmi_out.start()

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Capture device is open?: " + str(cap.isOpened()))

run = True
while run:
    ret, frame = cap.read()
    check_exit = stdscr.getch()
    if check_exit == ord('q'):
        run = False

    if ret:
        outframe = hdmi_out.newframe()
        outframe[:] = frame
        hdmi_out.writeframe(outframe)
    else:
        raise RuntimeError("Error while reading from camera")

curses.endwin()
print("Exiting, cleaning up...")
print("Releasing capture...")
cap.release()
print("destroying all windows...")
cv2.destroyAllWindows()
print("Stopping HDMI...")
hdmi_out.stop()
print("Deleting HDMI out...")
del hdmi_out
