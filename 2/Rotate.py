import cv2

img3_path = "../images/image3.jpg"

image = cv2.imread(img3_path)

#Rotate the image 60 degrees around its center
(h,w) = image.shape[:2]
center = (h//2,w//2)

mat = cv2.getRotationMatrix2D(center,angle=60,scale=1)

rotated_image = cv2.warpAffine(image,mat,(w,h))

cv2.imshow("rotated_image",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
