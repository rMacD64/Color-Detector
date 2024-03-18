import numpy as np
import cv2 as cv

def colour_limits(colour):
    # converts bgr values to hsv colour space
    # commonly used for object tracking
    c = np.unint8([[colour]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    # not sure what this does...
    lowLimit = hsvC[0][0][0] - 10, 100, 100
    upLimit = hsvC[0][0][0] + 10, 255, 255

    lowLimit = np.array(lowLimit, dtype=np.uint8)
    upLimit = np.array(upLimit, dtype=np.uint8)

    return lowLimit, upLimit

