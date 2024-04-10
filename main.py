import numpy as np
from computeH import computeH
from warpImage import warpImage

# Specify the paths to the input images
image1_path = "images/image1.jpg"
image2_path = "images/image2.jpg"

# Load the input images
image1 = np.load(image1_path)
image2 = np.load(image2_path)

# Load the correspondences
points1 = np.load('points/img1.npy')
points2 = np.load('points/img2.npy')

# Compute the homography matrix
H = computeH(points1, points2)

# Warp image2 to align with image1
warped_image, merged_image = warpImage(image1, image2, H)