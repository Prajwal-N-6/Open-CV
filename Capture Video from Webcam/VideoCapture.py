import cv2 as cv
video = cv.VideoCapture("Cat_Video.mp4")

ret = True
while ret:
    
    ret,frame = video.read()
    if ret:
        cv.imshow('frame',frame)
        cv.waitKey(40)            # 24 frames per sec: 1/24 = 0.040     

video.release()
cv.destroyAllWindows()
