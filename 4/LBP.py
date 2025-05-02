import cv2
import numpy as np
import matplotlib.pyplot as plt
from pydeck.data_utils.viewport_helpers import euclidean
from skimage.feature import local_binary_pattern

radius = 1
n_points = 8*radius

def myLBP(img,title):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    lbp = local_binary_pattern(gray,n_points,radius,method="uniform")

    plt.imshow(lbp,cmap="gray")
    plt.title(title)

    plt.show()

    hist,k= np.histogram(lbp.ravel(),bins = np.arange(0,n_points+3),range=(0,n_points+2))
    hist = hist.astype("float")
    hist/=(hist.sum() + 1e-6)


    return lbp,hist

img1_path = "../images/image5.jpg"
img2_path = "../images/image6.jpg"

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

lbp1,hist1 = myLBP(img1,"img1")
lbp2,hist2 = myLBP(img2,"img2")

from scipy.spatial import distance

euclidean = distance.euclidean(hist1,hist2)
print(euclidean)

