# Basics of Image Processing

This project is designed to learn the basics of image processing and Python programming using OpenCV and NumPy. It includes fundamental operations such as matrix arithmetic, image transformations, and feature extraction techniques.

---

## Contents

1. **Build Python + OpenCV Programming Environment**  
   Set up a working environment to run image processing code using Python and OpenCV.

2. **Matrix Arithmetic using NumPy**  
   Learn how to perform addition, subtraction, multiplication, and division on matrices.  
   You can define your own matrix values and visualize results by printing or screenshotting.

3. **Image Operations**  
   - Display images  
   - Resize (scale) images  
   - Rotate images  
   - Binarize (threshold) images  
   You can use any image of your choice.

4. **Difference Image Generation**  
   Create and visualize the absolute difference between two different images.  
   Select images with clear visual differences for better comparison.

5. **Image Feature Extraction and Visualization**  
   Explore various image feature descriptors such as:  
   - RGB Histogram  
   - LBP (Local Binary Pattern)  
   - ORB (Oriented FAST and Rotated BRIEF)  
   - SIFT (Scale-Invariant Feature Transform)  
   
   Compare the feature vectors extracted from different images to understand how image similarity can be measured.

---

## Project Structure

```
.
├── 1/
│   └── Try_Numpy.py               # Basic NumPy operations on Matrix
├── 2/
│   ├── Display.py                 # Display
│   ├── Scale.py                   # Image resizing
│   ├── Rotate.py                  # Image rotation
│   └── Binarize.py                # Binarization (thresholding)
├── 3/
│   └── Difference_Image.py        # Compute and display difference image
├── 4/
│   ├── Histogram.py               # RGB histogram extraction and comparison
│   ├── LBP.py                     # Local Binary Pattern texture feature
│   ├── ORB.py                     # ORB keypoint detection and matching
│   └── SIFT.py                    # SIFT keypoint detection and KNN matching
├── images/
│   ├── image1.png
│   ├── image2.jpg
│   ├── image3.jpg
│   ├── image4.jpg
│   ├── image5.jpg
│   └── image6.jpg
└── README.md                      # Project description
```

---

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib
- scikit-image
- SciPy

### Install dependencies:

```bash
pip install opencv-python matplotlib numpy scikit-image scipy
```

---

## Usage

Each script can be run independently. For example:

```bash
python 3/Difference_Image.py
python 2/Rotate.py
```
