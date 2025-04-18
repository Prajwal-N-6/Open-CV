import cv2 as cv

img = cv.imread("contour.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    print(cv.contourArea(cnt))
    if cv.contourArea(cnt) > 200:
        x1, y1, w, h = cv.boundingRect(cnt)
        cv.rectangle(img, (x1,y1), (x1 + w,y1 + h), (0, 255, 0), 2)                # draw rectangles around the detected object 


cv.imshow('img',img)
cv.imshow('img_gray',img_gray)
cv.imshow('thresh', thresh)

cv.waitKey(0)
cv.destroyAllWindows()
