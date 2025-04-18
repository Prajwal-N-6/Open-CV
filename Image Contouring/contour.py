import cv2 as cv

img = cv.imread("contour.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv.contourArea(cnt))
    if cv.contourArea(cnt) > 200:
        cv.drawContours(img, cnt, -1, (0,255,0),4)            # draw green color outline around the birds in the image. 

cv.imshow('img',img)
cv.imshow('img_gray',img_gray)
cv.imshow('thresh', thresh)

cv.waitKey(0)
cv.destroyAllWindows()
