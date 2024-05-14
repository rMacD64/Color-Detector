# Color-Detector
This was part of a design project to train Lower Mainland Biomedical Engineer (LMBME) technologists how to conduct preventative maintenance procedure on a BD Alaris Point of Care Unit (PCU). Through abundant research, conversation with clientelle and collaborative brainstorming, my team decided an augmented reality phone application would best suit the user's needs. The design includes a headset which holds the phone and provides visual and audio feedback/instructions to the user. The phone camera is used in conjuction with object and colour detection software to detect user motion in reference to the PCU, allowing the application to accurately determine if the instructions/feedback are being followed by the user. Originally, the user was meant to wear red finger-tipped gloves, so the colour detector model could determine which button on the PCU the user was pressing or not pressing, however in the final version of the model the colour being detected may be calibrated to any colour shown on screen.

The sections below discuss how the detector was developed including references and prelimitive testing. Descriptive videos which summarize the various prototype versions may be found [here](https://drive.google.com/drive/folders/1AvaDCTcdqhrKJqsUbiWlbtn1ayG1NXrz?usp=sharing).

## Colour Detection Model Version 1
The colour detection model uses Python and the Open CV Python library to analyze videos obtained through a computer’s default camera. Several iterations were made to improve the accuracy of colour detection and how the model communicated its detection (e.g. the inclusion of object outlines, text, etc.). Iterations were based on researched tutorials or code segments and were modified for our specific purposes.

In the first iteration of the colour detection model, a simple online tutorial was followed, which detected a range of yellow colours in the HSV colour space, created a mask for such colours and created a green bounding box around all pixels included in the mask ([1]). The code was modified to detect red colours instead, as shown below in Figure 1A.

<p align="center">
  <img src="https://github.com/rMacD64/Color-Detector/assets/91086955/da0798d2-b841-4842-b2b6-9a454040fd7a"><br>
  <i>Figure 1. Video output from colour detection version 1.</i>
</p>

However, as seen above from the top part of Figure 1B, the first version of the colour detection model would not detect all colours the human eye would normally perceive as red. Since different camera modalities and lighting conditions may impact how the computer perceives colours, it was necessary to improve the range of reds which the model detected. Additionally, as seen in Figure 1C the bounding box would expand to fit all red objects in view. This was not ideal for our purposes because it meant multiple fingertips in the frame would be merged into one box; specific finger tips could not be monitored simultaneously.

## Colour Detection Model Version 2
In the second iteration of the colour detection model, several pieces of researched code were merged and modified. One detected red colours in the LAB colour space and used blurring methods to increase accuracy of detection ([2]). It also placed a circular bounding box around red objects ([2]). Another model created an outline and centre point on an image showing a masked object ([3]) and another model created an outline, centre point and text indicating the colour of several various coloured objects ([4]). The latter model also required coloured objects to cover a minimum portion of the screen, so coloured objects far from the camera would not be detected ([4]). The latter model was tested with two HSV colour ranges and the recommended LAB range from the first code segment, but as seen in Table 1, the LAB colour range appeared to be the most accurate.

*Table 1. Colour spaces, lower and upper range and associated accuracy.*
| HSV colour space: [160, 50, 50] to [180, 255, 255] | HSV colour space: [161, 165, 127] to [178, 255, 255] | LAB colour space: [20, 150, 150] to [190, 255, 255] |
|---|---|---|
| ![image](https://github.com/rMacD64/Color-Detector/assets/91086955/00ad18e8-e3b5-482a-9f9b-18cc42fbc221) | ![image](https://github.com/rMacD64/Color-Detector/assets/91086955/55396444-dbcc-4ee9-a484-160b48ff3dca) | ![image](https://github.com/rMacD64/Color-Detector/assets/91086955/22491075-0d46-44c8-844d-845d646563a8) |

The code resources were merged and modified. Ultimately the model used the LAB colour space and blurring effects to accurately create a mask for red coloured objects. If red-coloured objects covered a certain portion of the screen, the model outlined the object in blue, created a green centre point and indicated the pixel coordinates of the centre point on the output video (see Figure 2).

<p align="center">
  <img src="https://github.com/rMacD64/Color-Detector/assets/91086955/ab7b1e8a-68f2-457d-8903-31fc19ef2066"><br>
  <i>Figure 2. Video output of colour detector version 2.</i>
</p>

However, the model would also detect colours that were closely related to red, like pink or orange, as shown in Figure 3 below.

<p align="center">
  <img src="https://github.com/rMacD64/Color-Detector/assets/91086955/f68d5c77-4519-4f2c-9403-2016b136ba0a"><br>
  <i>Figure 3. Error in colour detector version 2.</i>
</p>

## Colour Detection Model Version 3
In the final version of the colour detector model, another group member iterated on the first version by adding a calibration step. The user is meant to place a colour that they would like to detect within a blue circle on the screen. The user presses a key on the computer and the colour of the pixels defined within the blue circle are used to create a range of acceptable colours for a mask (see Figure 4A below). The range was created in the HSV colour space with adaptable tolerance values. The mask it creates is used label red objects with a blue centre point and red text (see Figure 4B). As a proof of concept, the design also included a large green bounding box fixed in place on the screen, which is where the PCU would be placed by the user. Two smaller squares to the left of the bounding box represent buttons. If the blue centre point located on a red object was positioned within the bottom square, the detector would fill the square red, indicating to the user the wrong button has been pressed (see Figure 4C). If the centre point was located in the top square, the program would indicate the correct button has been pressed by filling the square green (see Figure 4D). In this way, the centre point locations could be used to indicate to the user which button they should press on the PCU. However, this method would only work if we knew where the buttons were located in relation to the camera, which is why the PCU must be placed inside the large green bounding box.

<p align="center">
  <img src="https://github.com/rMacD64/Color-Detector/assets/91086955/d02935a9-4644-4243-8611-56c02cc57c7e"><br>
  <i>Figure 4. Calibration stage (top left). colour detector version 3 in progress (top right). Proof of concept, indicating wrong button has been pressed (bottom left). Proof of concept indicating the correct button has been pressed (bottom right).</i>
</p>

This version introduced interesting concepts and provided greater flexibility since colours other than red could be easily calibrated for and detected. However, the model was not effective in detecting the desired coloured objects that lie outside the centre of the screen and it did not provide measurable coordinates of pixel location, which was estimated to be useful for testing. Therefore, this implementation was combined with the LAB colour space and the masking and labelling techniques used in the previous version, so specifically coloured objects were more effectively detected and it was clear where the coloured object was specifically being detected. The calibration point was also changed to exist in the main screen, so the colour detector could be calibrated or recalibrated during run time. The final design is shown in Figure 5 below.

<p align="center">
  <img src="https://github.com/rMacD64/Color-Detector/assets/91086955/a727931f-795f-48f4-847e-c8523a63877d"><br>
  <i>Figure 5. Final colour detector version with recalibration circle, blue bounding box and pixel coordinates. In this case, the detector is detecting the blue on the index finger of the glove because it was calibrated with this colour.</i>
</p>

[1]: https://www.youtube.com/watch?v=aFNDh5k3SjU
[2]: https://github.com/ChristophRahn/red-circle-detection/blob/master/red-circle-detection.py
[3]: https://answers.opencv.org/question/204175/how-to-get-boundry-and-center-information-of-a-mask/
[4]: https://medium.com/@sardorabdirayimov/colors-detection-using-masks-contours-in-opencv-72d127f0797e
