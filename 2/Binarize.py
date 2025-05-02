import cv2

img3_path = "../images/image3.jpg"

image = cv2.imread(img3_path)

gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

retval,binary1 = cv2.threshold(gray,255//2,255,type=cv2.THRESH_BINARY)

retval,binary2 = cv2.threshold(gray,255//3,255,type=cv2.THRESH_BINARY)


cv2.imshow("thresh127",binary1)

cv2.imshow("thresh85",binary2)

cv2.waitKey(0)
cv2.destroyAllWindows()