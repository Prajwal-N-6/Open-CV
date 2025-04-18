#applications of blur-filters 

import cv2 as cv

img = cv.imread("noise.jpg")

blur_classic = cv.blur(img,(7,7))
blur_gauss = cv.GaussianBlur(img,(7,7),7)
blur_median = cv.medianBlur(img,7)

cv.imshow('img_noise',img)                        # Original Image with Noise
cv.imshow('blur_classic',blur_classic)            # Smoothed Image using Classic Blur
cv.imshow('blur_gauss',blur_gauss)                # Smoothed Image using Gaussian Blur
cv.imshow('blur_median',blur_median)              # Smoothed Image using Media Blur (best).  

cv.waitKey(0)
cv.destroyAllWindows()
