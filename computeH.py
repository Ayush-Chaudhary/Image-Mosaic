# Write a function computeH (t1,
# t2) that takes a set of corresponding image points t1, t2 (both t1 and t2 should be 2xN
# matrices) and computes the associated 3 x 3 homography matrix H. The function should
# take a list of n ≥ 4 pairs of corresponding points from the two views, where each point is
# specified with its 2d image coordinates. 

import numpy as np

def computeH(t1, t2):
    # throw an error if the number of points is less than 4
    if t1.shape[0] < 4 or t2.shape[0] < 4:
        raise ValueError('Number of points should be greater than 3')

    t1_new = t1
    t2_new = t2

    # change the points from 12*2 to 12*3 by adding a row of ones
    t1_new = np.hstack((t1_new, np.ones((t1_new.shape[0], 1))))
    t2_new = np.hstack((t2_new, np.ones((t2_new.shape[0], 1))))

    # create the A matrix
    A = np.zeros((2 * t1_new.shape[0], 9))

    # fill the A matrix
    for i in range(t1_new.shape[0]):
        A[2 * i, 3:6] = -t2_new[i, 2] * t1_new[i, :]
        A[2 * i, 6:] = t2_new[i, 1] * t1_new[i, :]
        A[2 * i + 1, :3] = t2_new[i, 2] * t1_new[i, :]
        A[2 * i + 1, 6:] = -t2_new[i, 0] * t1_new[i, :]

    # compute the SVD of A
    _, _, V = np.linalg.svd(A)

    # extract the homography matrix
    H = V[-1, :].reshape(3, 3)

    return H
