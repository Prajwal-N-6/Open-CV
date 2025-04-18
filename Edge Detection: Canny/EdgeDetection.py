import cv2 as cv

img = cv.imread("img7.jpg")

img_edge = cv.Canny(img,100,200)

cv.imshow('img',img)
cv.imshow('img_edge',img_edge)
cv.waitKey(0)
cv.destroyAllWindows()
