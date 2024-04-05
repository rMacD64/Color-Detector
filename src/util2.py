import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure
from skimage.exposure import match_histograms
import cv2

def colour_limits(c, h_tol, s_tol, v_tol):
    # converts bgr values to hsv colour space
    # commonly used for object tracking

    # not sure what this does...
    lowLimit = np.array([max(0, c[0]-h_tol), max(0, c[1]-s_tol), max(0, c[2]-v_tol)], np.uint8)
    upLimit = np.array([min(179, c[0]+h_tol), min(255, c[1]+s_tol), min(255, c[2]+v_tol)], np.uint8)

    return lowLimit, upLimit

'''
Parameters
----------
webcam : video capture object
    Current webcam
Returns
---------
red : 
green :
blue :   
'''
def calibrate():
    webcam = cv2.VideoCapture(0)
  
    # Start a while loop 
    while(1): 
        _, frame = webcam.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        # locate centre
        cx = int(width / 2)
        cy = int(height / 2)
        cv2.circle(frame, (cx, cy),  5, (255, 0, 0), 3)
        
        cv2.imshow("calibration", frame)
        key = cv2.waitKey(1)
        if key == 114: # pressed r
            red = hsv_frame[cy, cx]
            print(red)
        if key == 103: # pressed g
            green = hsv_frame[cy, cx]
            print(green)
        if key == 98: # pressed b
            blue = hsv_frame[cy, cx]
            print(blue)
        if key == 32: # pressed space
            webcam.release() 
            cv2.destroyAllWindows() 
            break
    return red, green, blue

        
