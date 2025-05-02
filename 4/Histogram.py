import cv2
import matplotlib.pyplot as plt
import numpy as np

def histogram(image,title):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    channels = cv2.split(image)
    colors = ("r","g","b")
    plt.figure()
    plt.title(title)

    feature_vector = []
    for(channel,color) in zip(channels,colors):
        hist = cv2.calcHist([channel],[0],None,[256],[0,256])
        plt.plot(hist,color = color)
        #plt.title("RGB Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")

        feature_vector.extend(hist.flatten())

    plt.show()
    return feature_vector


img1_path = "../images/image4.jpg"
img2_path = "../images/image6.jpg"

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

hist1 = histogram(img1,"RGB Histogram of Image1")
hist2 = histogram(img2,"RGB Histogram of Image2")

dist = np.linalg.norm(np.array(hist1)-np.array(hist2))
print("Distance:",dist)
