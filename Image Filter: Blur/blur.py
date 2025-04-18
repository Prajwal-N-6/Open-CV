import cv2 as cv

img = cv.imread("img2.jpg")

k_size = 7
blur_classic = cv.blur(img, (k_size,k_size))                        # Classic Blur
blur_gauss = cv.GaussianBlur(img,(k_size,k_size),7)                 # Gaussian Blur
blur_median = cv.medianBlur(img,k_size)                             # Median Blur

cv.imshow('img',img)
cv.imshow('blur',blur_classic)
cv.imshow('gauss_blur',blur_gauss)
cv.imshow('median_blur',blur_median)

cv.waitKey(0)
cv.destroyAllWindows()
