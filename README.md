# Image-Mosaic
This repository implements an image stitcher that uses image warping and homographies to automatically create an image mosaic
Getting correspondences: Code to get manually identified corresponding points from two views.
Computing the homography parameters: ComputeH takes a set of corresponding image points t1, t2 (both t1 and t2 should be 2xN matrices) and computes the associated 3 x 3 homography matrix H
Warping between image planes: warpImage(inputIm, refIm, H), takes as input an image inputIm, a reference image refIm, and a 3x3 homography matrix H. This function returns two images as outputs. The first image, warpIm, is the input image inputIm warped according to H to fit within the frame of the reference image refIm. The second output image, mergeIm, is a single mosaic image with a larger field of view containing
both input images
