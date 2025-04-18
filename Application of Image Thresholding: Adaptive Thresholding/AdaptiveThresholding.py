import cv2 as cv 

img = cv.imread("img6.jpg")
rs_img = cv.resize(img,(700,700))

img_gray = cv.cvtColor(rs_img,cv.COLOR_BGR2GRAY)

ret, simple_thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY)

adaptive_thresh = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,21,30)

cv.imshow('rs_img',rs_img)
cv.imshow('simple_thresh',simple_thresh)
cv.imshow('adaptive_thresh',adaptive_thresh)

cv.waitKey(0)
cv.destroyAllWindows()
