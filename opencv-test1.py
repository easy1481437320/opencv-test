import cv2
img = cv2.imread("1.jpg")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)

blur_img = cv2.GaussianBlur(invert, (7,7),0)
inverse_blur = cv2.bitwise_not(blur_img)
sketch_img = cv2.divide(grey , inverse_blur , scale=256.0)
cv2.imwrite('test.jpg', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()