## Color-Detector

# Colour Detection Model Version 1
The colour detection model uses Python and the Open CV Python library to analyze videos obtained through a computer’s default camera. Several iterations were made to improve the accuracy of colour detection and how the model communicated its detection (e.g. the inclusion of object outlines, text, etc.). Iterations were based on researched tutorials or code segments and were modified for our specific purposes.

In the first iteration of the colour detection model, a simple online tutorial was followed, which detected a range of yellow colours in the HSV colour space, created a mask for such colours and created a green bounding box around all pixels included in the mask (link). The code was modified to detect red colours instead, as shown below in Figure 1A.

<p align="center">
<img src="https://github.com/rMacD64/Color-Detector/assets/91086955/da0798d2-b841-4842-b2b6-9a454040fd7a"\>
</p>

However, as seen above from the top part of Figure 1B, the first version of the colour detection model would not detect all colours the human eye would normally perceive as red. Since different camera modalities and lighting conditions may impact how the computer perceives colours, it was necessary to improve the range of reds which the model detected. Additionally, as seen in Figure 1C the bounding box would expand to fit all red objects in view. This was not ideal for our purposes because it meant multiple fingertips in the frame would be merged into one box; specific finger tips could not be monitored simultaneously.

# Colour Detection Model Version 2
In the second iteration of the colour detection model, several pieces of researched code were merged and modified. One detected red colours in the LAB colour space and used blurring methods to increase accuracy of detection (link). It also placed a circular bounding box around red objects (link). Another model created an outline and centre point on an image showing a masked object (link) and another model created an outline, centre point and text indicating the colour of several various coloured objects (link). The latter model also required coloured objects to cover a minimum portion of the screen, so coloured objects far from the camera would not be detected (link). The latter model was tested with two HSV colour ranges and the recommended LAB range from the first code segment, but as seen in Table 3, the LAB colour range appeared to be the most accurate.

Table 3. Colour spaces, lower and upper range and associated accuracy.


HSV colour space: [160, 50, 50] to [180, 255, 255]
HSV colour space: [161, 165, 127] to [178, 255, 255]
LAB colour space: [20, 150, 150] to [190, 255, 255]
Resulting Output




The code resources were merged and modified. Ultimately the model used the LAB colour space and blurring effects to accurately create a mask for red coloured objects. If red-coloured objects covered a certain portion of the screen, the model outlined the object in blue, created a green centre point and indicated the pixel coordinates of the centre point on the output video (see Figure 2).


Figure 2. Video output of colour detector version 2.

However, the model would also detect colours that were closely related to red, like pink or orange, as shown in Figure 3 below.


Figure 3. Error in colour detector version 2.

3.1.3 Colour Detection Model Version 3
In the final version of the colour detector model, another group member iterated on the first version by adding a calibration step. The user is meant to place a colour that they would like to detect within a blue circle on the screen. The user presses a key on the computer and the colour of the pixels defined within the blue circle are used to create a range of acceptable colours for a mask (see Figure 4A below). The range was created in the HSV colour space with adaptable tolerance values. The mask it creates is used label red objects with a blue centre point and red text (see Figure 4B). As a proof of concept, the design also included a large green bounding box fixed in place on the screen, which is where the PCU would be placed by the user. Two smaller squares to the left of the bounding box represent buttons. If the blue centre point located on a red object was positioned within the bottom square, the detector would fill the square red, indicating to the user the wrong button has been pressed (see Figure 4C). If the centre point was located in the top square, the program would indicate the correct button has been pressed by filling the square green (see Figure 4D). In this way, the centre point locations could be used to indicate to the user which button they should press on the PCU. However, this method would only work if we knew where the buttons were located in relation to the camera, which is why the PCU must be placed inside the large green bounding box.



Figure 4. Calibration stage (top left). colour detector version 3 in progress (top right). Proof of concept, indicating wrong button has been pressed (bottom left). Proof of concept indicating the correct button has been pressed (bottom right).

This version introduced interesting concepts and provided greater flexibility since colours other than red could be easily calibrated for and detected. However, the model was not effective in detecting the desired coloured objects that lie outside the centre of the screen and it did not provide measurable coordinates of pixel location, which was estimated to be useful for testing. Therefore, this implementation was combined with the LAB colour space and the masking and labelling techniques used in the previous version, so specifically coloured objects were more effectively detected and it was clear where the coloured object was specifically being detected. The calibration point was also changed to exist in the main screen, so the colour detector could be calibrated or recalibrated during run time. The final design is shown in Figure 5 below.


Figure 5. Final colour detector version with recalibration circle, blue bounding box and pixel coordinates. In this case, the detector is detecting the blue on the index finger of the glove because it was calibrated with this colour.

References
1. 
