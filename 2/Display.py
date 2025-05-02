import cv2

#img1_path = "../images/image1.png"

#show image3
img3_path = "../images/image3.jpg"

image = cv2.imread(img3_path)

cv2.imshow('image3',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
