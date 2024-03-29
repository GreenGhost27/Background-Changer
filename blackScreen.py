import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("man-standing-on-top-of-mountain-person-people.jpg") 
  
while True: 
    ret, frame = video.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
    uBlack = np.array([104, 153, 70]) 
    lBlack = np.array([30, 30, 0]) 
    mask = cv2.inRange(frame, lBlack, uBlack) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
    f = frame - res 
    f = np.where(f == 0, image, f) 
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
video.release() 
cv2.destroyAllWindows() 
