import cv2 as cv
img = cv.imread("img2.jpg",1)
rs_img = cv.resize(img,(700,700))
cv.imshow("Cat",rs_img,)
cv.waitKey(0)
cv.destroyAllWindows()
