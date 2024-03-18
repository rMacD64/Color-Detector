import numpy as np
import cv2 as cv
from PIL import Image

from util import colour_limits

# VideoCapture() opens camera
# 0 is default camera, but may take string or other index
# to change camera settings
RED = [255, 0, 0]
BB_COLOUR = (0, 255, 0)
BB_THICKNESS = 5
ID = 0
cap = cv.VideoCapture(ID)

if not cap.isOpened():
    print("Error: Cannot open camera.")
    exit()

while True:
    # captures frame by frame and ret is false
    # if frame cannot be detected
    ret, frame = cap.read()

    # convert to hsv colour space
    hsvImg = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # get bounds from util function
    lowLimit, upLimit = colour_limits(colour=RED)

    mask = cv.inRange(hsvImg, lowLimit, upLimit)

    # creates pillow image of array
    maskImg = Image.fromarray(mask)

    # returns None if colour not detected or coordinates
    # if it is
    colourBB = maskImg.getbbox()

    if colourBB is not None:
        x1, y1, x2, y2 = colourBB

        frame = cv.rectangle(frame, (x1, y1), (x2, y2), BB_COLOUR, BB_THICKNESS)

    # showing the image
    # string parameter is title of video feed
    cv.imshow('frame', frame)

    # waitKey(0) produces still images until
    # a key is pressed. Parameter of 1 produces
    # constant images.
    # the following essentially means we will
    # stop recording frames when any key is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

