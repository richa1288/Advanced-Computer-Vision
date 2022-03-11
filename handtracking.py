# To show the web cam video

import cv2
import mediapipe as mp
import time

cap= cv2.VideoCapture(0)
mpHands= mp.solutions.hands
hands= mpHands.Hands()
mpDraw= mp.solutions.drawing_utils 


while True:
    success, img= cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    # to check multiple hands or not
    if results.multi_hand_landmarks:   
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):   # to see id and landmarks
                #print(id,lm)     #landmarks are giving ratio of image
                h, w, c= img.shape   # to check height width and channel
                cx, cy= int(lm.x*w),int(lm.y*h)  # calculate pixel value using height width, x value from lm(lm.x) multiplyby width
                print(id,cx, cy)
                if id==0:
                    cv2.circle(img, (cx,cy),25,(255, 0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    
    
   
    cv2.imshow("Image", img)
    cv2.waitKey(1)