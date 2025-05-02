import cv2
import matplotlib.pyplot as plt
from scipy.signal.windows import hamming


def MakeORB(img,title):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    orb = cv2.ORB_create()
    keypoints,descriptors = orb.detectAndCompute(gray,None)

    img_kp = cv2.drawKeypoints(img,keypoints,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow(title,img_kp)#show ORBed image
    cv2.waitKey()
    cv2.destroyAllWindows()

    return keypoints,descriptors


img1_path = "../images/image5.jpg"
img2_path = "../images/image6.jpg"

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

kp1,des1 = MakeORB(img1,"img1")
kp2,des2 = MakeORB(img2,"img2")


#Use KNN to match two images
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

filtered_matches = []
for i,j in matches:
    if i.distance < 0.8*j.distance:
        filtered_matches.append([i])


knn_matched_image = cv2.drawMatchesKnn(img1,kp1,img2,kp2,filtered_matches,None,flags=2)

plt.figure()
plt.title("knnMatch")
plt.imshow(cv2.cvtColor(knn_matched_image,cv2.COLOR_BGR2RGB))
plt.show()

#Hamming distance
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda  x:x.distance)

hamming_matched_image = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=2)
plt.figure()
plt.title("hammingMatch")
plt.imshow(cv2.cvtColor(hamming_matched_image,cv2.COLOR_BGR2RGB))
plt.show()