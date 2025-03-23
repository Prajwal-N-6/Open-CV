import cv2 as cv
img = cv.imread("img1.jpg",1)
cv.imshow("Cat",img,)
cv.waitKey(0)
cv.destroyAllWindows()
