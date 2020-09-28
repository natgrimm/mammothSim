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
aim = False

shoot_count = 0
shoot_again_count = 0
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if (aim):
        shoot_count += 1
    if (shoot_again_count < 101):
        shoot_again_count += 1
    else:
        cv2.putText(frame1, "Status: {}".format('Ready'), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if (cv2.contourArea(contour) < 900 and cv2.contourArea(contour) > 200):
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
   
        if ((aim == False) and ((y < (frame_height * 3.0/ 8.0) and (y > (frame_height * 1.0 / 8.0)))) and (shoot_again_count > 100)):
            cv2.putText(frame1, "Status: {}".format('AIM Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
            sock.sendto( ("Aim").encode(), (UDP_IP, UDP_PORT) )
            aim = True
            shoot_count = 0
            
        if (aim and ((y) < (frame_height * 1.0/ 8.0)) and (shoot_again_count > 100)):
            cv2.putText(frame1, "Status: {}".format('Shoot Movement'), (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
            if (shoot_count < 100):
                sock.sendto( ("030").encode(), (UDP_IP, UDP_PORT) )
            else:
                sock.sendto( ("015").encode(), (UDP_IP, UDP_PORT) )
            aim = False
            print("Shoot count: " + str(shoot_count))

#            shoot_count = 0
            shoot_again_count = 0
  #          time.sleep(.5)
  #  image = cv2.resize(frame1, (1280,))
#    out.write(image)
    cv2.imshow("feed", frame1)
 #   cv2.imshow("diff", diff)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
#out.release()