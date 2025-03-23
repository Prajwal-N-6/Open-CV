import cv2 as cv                      
img = cv.imread("img1.jpg",1)                    # read image from relative path 
cv.imshow("Cat",img,)                            # display the image in a window titled "Cat"
cv.waitKey(0)                                    # window handling
cv.destroyAllWindows()
