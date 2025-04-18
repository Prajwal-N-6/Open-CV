import cv2 as cv

img = cv.imread("img2.jpg")

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('img',img)
cv.imshow('img_rgb',img_rgb)
cv.imshow('img_gray',img_gray)
cv.imshow('img_hsv',img_hsv)
cv.waitKey(0)
cv.destroyAllWindows()
