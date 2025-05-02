import cv2

img1_path = "../images/image1.png"
img3_path = "../images/image3.jpg"

img1 = cv2.imread(img1_path)
shape1 = img1.shape[:2]

img2 = cv2.imread(img3_path)
shape2 = img2.shape[:2]

new_img2 = cv2.resize(img2,shape1)

sub = img1 - new_img2
diff = cv2.absdiff(img1,new_img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',new_img2)

cv2.imshow('Subtract Image',sub)

cv2.imshow('Difference Image',diff)

cv2.waitKey(0)
cv2.destroyAllWindows()