import cv2 as cv

img = cv.imread("img8.jpg")
print(img.shape)

cv.line(img,(0,0),(849,499),(0,255,0),5)

cv.rectangle(img,(200,150),(450,300),(0,255,255),4)

cv.circle(img,(630,145),100,(255,255,0),5)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
