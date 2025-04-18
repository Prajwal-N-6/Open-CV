import cv2 as cv 

img = cv.imread("img4.jpg")
w = 700
l = 700
rs_img = cv.resize(img,(w,l))

img_gray = cv.cvtColor(rs_img,cv.COLOR_BGR2GRAY)
# gray image of original image. Input to the threshold must be a gray image. 

ret, thresh = cv.threshold(img_gray,100,255,cv.THRESH_BINARY)
# set a lower thereshold.. anything above threshold will turn white while anything below will turn black (binary image). 

cv.imshow('img',rs_img)
cv.imshow('img_gray',img_gray)
cv.imshow('img_thresh',thresh)

cv.waitKey(0)
cv.destroyAllWindows()
