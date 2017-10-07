#!/usr/bin/env python3.6

import numpy as np
import cv2
import sys

def check_obj(haar_file):
    frame_w = 640 
    frame_h = 480

    cap = cv2.VideoCapture(0)

    classifier = cv2.CascadeClassifier(haar_file)
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    objs = classifier.detectMultiScale(gray, 1.3, 5)

    cap.release()
    
    return len(objs)

if __name__ == "__main__":
   print(len(sys.argv))
   for arg in sys.argv:
       print(arg)
   if len(sys.argv) != 2:
       print("./check_car.py <haar_file>")
       exit(-1)
   is_obj = check_obj(sys.argv[-1])
   print("There are %s specified objs on screen" % is_obj)
