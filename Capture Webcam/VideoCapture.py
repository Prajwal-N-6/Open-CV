import cv2 as cv 

webcam = cv.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    cv.imshow("WebCam",frame)
    if cv.waitKey(40) & 0xFF == ord('q'):          # press 'q' to quit Webcam
        break
    

webcam.release()
cv.destroyAllWindows()
