import cv2

img3_path = "../images/image3.jpg"

image = cv2.imread(img3_path)
small_image = cv2.resize(image,None,fx = 0.5,fy = 0.5,interpolation=cv2.INTER_AREA)
big_image = cv2.resize(image,None,fx = 2,fy = 2,interpolation=cv2.INTER_LINEAR)

cv2.imshow("Scaled(50%)",small_image)
cv2.imshow("Scaled(200%)",big_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
