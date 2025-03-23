import cv2 as cv
img = cv.imread("img1.jpg",1)
w = 700
l = 700
rs_img = cv.resize(img,(w,l))
txt  = cv.putText(
img = rs_img,
text = "I Love Cats",
org = (50,50),
fontFace = cv.FONT_HERSHEY_DUPLEX,
fontScale = 2,
color = (146,76,26),
thickness = 3,
lineType = cv.LINE_8,
bottomLeftOrigin = False
)
txt  = cv.putText(
img = txt, text = "I Love Cats",
org = (50,60),
fontFace = cv.FONT_HERSHEY_DUPLEX,
fontScale = 2,
color = (146,76,26),
thickness = 3,
lineType = cv.LINE_8,
bottomLeftOrigin = True
)
cv.imshow("Cat",rs_img,)
cv.waitKey(0)
cv.destroyAllWindows()
