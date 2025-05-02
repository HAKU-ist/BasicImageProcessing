import cv2
import matplotlib.pyplot as plt

#surf = cv2.xfeatures2d.SURF_create(hessianThreshold=400)

def MakeSift(img,title):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints,descriptors = sift.detectAndCompute(gray,None)

    img_kp = cv2.drawKeypoints(img,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow(title,img_kp)#show SITFed image
    cv2.waitKey()
    cv2.destroyAllWindows()

    return keypoints,descriptors


img1_path = "../images/image5.jpg"
img2_path = "../images/image6.jpg"

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

kp1,des1 = MakeSift(img1,"img1")
kp2,des2 = MakeSift(img2,"img2")


#Use KNN to match two images
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

filtered_matches = []
for i,j in matches:
    if i.distance < 0.85*j.distance:
        filtered_matches.append([i])


matched_image = cv2.drawMatchesKnn(img1,kp1,img2,kp2,filtered_matches,None,flags=2)

plt.figure()
plt.title("knnMatch")
plt.imshow(cv2.cvtColor(matched_image,cv2.COLOR_BGR2RGB))
plt.show()

