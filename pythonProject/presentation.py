import keyboard
from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import time
import numpy as np

# Parameters
width, height = 1280, 720
gestureThreshold = 300
# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detectorHand = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
imgList = []
delay = 30
buttonPressed = False
counter = 0
drawMode = False
imgNumber = 0
delayCounter = 0
annotations = [[]]
annotationNumber = -1
annotationStart = False
hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image

while True:
    # Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # draw a box in the left of the screen
    cv2.rectangle(img,(0,gestureThreshold),(50,gestureThreshold-200),(255,0,255),cv2.FILLED)

    # draw a box in the right of the screen

    cv2.rectangle(img, (width,gestureThreshold), (width-50,gestureThreshold-200), (255, 0, 255), cv2.FILLED)


    # Find the hand and its landmarks
    hands, img = detectorHand.findHands(img)  # with draw
    # Draw Gesture Threshold line
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 200, 0), 10)
    cv2.line(img, (0, gestureThreshold-200), (width, gestureThreshold-200), (0, 200, 0), 10)
    if hands and buttonPressed is False:  # If hand is detected

        hand = hands[0]
        cx, cy = hand["center"]
        # detect the right hand 
        if (gestureThreshold-200<=cy<=gestureThreshold and hand['type']=='Right' and fingers ==[1,1,1,1,1]):
            cv2.rectangle(img, (0, gestureThreshold), (50, gestureThreshold - 200), (0, 0, 0), 4)
            keyboard.press_and_release('Left')
            time.sleep(0.5)
            print('Right')


            key = cv2.waitKey(10)
        # detect the left hand
        if (gestureThreshold-200<=cy<=gestureThreshold and hand['type']=='Left' and fingers ==[1,1,1,1,1]):
            cv2.rectangle(img, (width, gestureThreshold), (width - 50, gestureThreshold - 200), (0, 0, 0),
                          4)

            keyboard.press_and_release('Right')
            time.sleep(0.5)
            print('Left')
            cv2.imshow("Image", img)

            key = cv2.waitKey(10)



        




        lmList = hand["lmList"]  # List of 21 Landmark points
        fingers = detectorHand.fingersUp(hand)  # List of which fingers are up

        # Constrain values for easier drawing
        xVal = int(np.interp(lmList[8][0], [width // 2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger = xVal, yVal





    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break