import cv2
import mediapipe as mp
import time
mpPose= mp.solutions.pose
mpDraw= mp.solutions.drawing_utils
pose=mpPose.Pose()
cap=cv2.VideoCapture('C:/Users/acer/Desktop/Computer Vision/boy_walking.mp4')
pTime=0
while True:
    SUCCESS, img = cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #frame is in color image but module compatible to gray so convert
    results= pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks)

 # frame rate
    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)),(70,50), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,0),3)
    cv2.imshow("Image", img)
    cv2.waitKey(100)