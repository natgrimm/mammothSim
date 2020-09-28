# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:06:40 2019

@author: richardg71
"""

import cv2
import numpy as np
import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5065

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

#fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

#out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
aim = False;
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if (cv2.contourArea(contour) < 900 and cv2.contourArea(contour) > 200):
            continue
   #     cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        if ((aim == False) and ((y) < (frame_height * 1.0/ 6.0)) and ((x) < (frame_width * 2.0/6.0))):
            cv2.putText(frame1, "Status: {}".format('AIM Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
            sock.sendto( ("Aim").encode(), (UDP_IP, UDP_PORT) )
            aim = True;
        if (aim and ((y) < (frame_height * 1.0/ 6.0)) and ((x) > (frame_width * 4.0/6.0))):
            cv2.putText(frame1, "Status: {}".format('Shoot Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
            sock.sendto( ("040").encode(), (UDP_IP, UDP_PORT) )
            aim = False
            time.sleep(.5)
    image = cv2.resize(frame1, (1280,720))
#    out.write(image)
    cv2.imshow("feed", frame1)
    cv2.imshow("diff", diff)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
#out.release()