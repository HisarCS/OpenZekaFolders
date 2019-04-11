import sys
sys.path.append("..") ## Must be added to include the OpenZeka Class
from OpenZekaMasterClass import ZedCam
from time import sleep
import cv2


camera = ZedCam()

camera.startLooking()

while True:
    frame = camera.getImage()

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break