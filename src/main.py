import numpy as np
import cv2 as cv
import imutils

# from util import colour_limits

# recommended range of colors in HSV color space
lower_limit_HSV = np.array([161, 165, 127])
upper_limit_HSV = np.array([178, 255, 255])

# previous range of colors in HSV color space
# lower_limit_HSV = np.array([160, 50, 50])
# upper_limit_HSV = np.array([180, 255, 255])

# range of colors in Lab color space
# lower_limit_LAB = np.array([64, 59, 32])
# upper_limit_LAB = np.array([0, 128, 127])
lower_limit_LAB = np.array([20, 150, 150])
upper_limit_LAB = np.array([190, 255, 255])
BORDER_COLOUR = (0, 255, 0)
BORDER_THICKNESS = 3
CENTRE_COLOUR = (0, 0, 0)
CENTRE_RADIUS = 5
MESSAGE = 'Red Detected'
TEXT_COLOR = (0, 0, 0)
THRESHOLD = 100 # can be adjusted to determine the distance at which we should identify objects

# VideoCapture() opens camera
# 0 is the default camera, but may take string or other index
ID = 0
cap = cv.VideoCapture(ID)

if not cap.isOpened():
    print("Error: Cannot open camera.")
    exit()

while True:
    # Captures frame by frame and ret is false if frame cannot be detected
    ret, frame = cap.read()
    if not ret:
        break
    output_frame = frame.copy()

    # Blur the image for processing
    # medianBlur preserves edges and is beneficial for high contrast
    # blurred_frame = cv.medianBlur(frame, 3)

    frame_lab = cv.cvtColor(frame, cv.COLOR_BGR2Lab)
    # frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(frame_lab, lower_limit_LAB, upper_limit_LAB)

    # Find contours:
    contours = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for c in contours:
        if cv.contourArea(c) > THRESHOLD:  # only if countour is big enough, then
            M = cv.moments(c)
            cx = int(M['m10'] / (M['m00'] + 1e-5))  # calculate X position and add 1e-5 to avoid division by 0
            cy = int(M['m01'] / (M['m00'] + 1e-5))  # calculate Y position

            # Draw contours on output frame
            cv.drawContours(output_frame, c, -1, BORDER_COLOUR, BORDER_THICKNESS)
            # Draw centre circle on output frame
            cv.circle(output_frame, (cx, cy), CENTRE_RADIUS, CENTRE_COLOUR, -1)
            # Put text on output frame
            cv.putText(output_frame, MESSAGE, (cx, cy), cv.FONT_HERSHEY_SIMPLEX, 1, TEXT_COLOR, 1)  # put text

    # Show image:
    cv.imshow("Red Detector", output_frame)

    # waitKey(0) produces still images until
    # a key is pressed. Parameter of 1 produces
    # constant images.
    # the following essentially means we will
    # stop recording frames when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

