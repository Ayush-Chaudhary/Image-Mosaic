import numpy as np

def perspectiveTransform(points, H):
    points = np.array(points)
    points = np.hstack((points, np.ones((points.shape[0], 1))))
    points = np.dot(H, points.T).T
    points = points / points[:, 2].reshape(-1, 1)
    return np.round(points[:, :2],4)

def warpPerspective(image, H, min_x, min_y, max_x, max_y):
    height, width = max_y - min_y, max_x - min_x
    warped_image = np.zeros((height, width, 3), dtype=np.uint8)
    H_inv = np.linalg.inv(H)
    for i in range(min_y, max_y):
        for j in range(min_x, max_x):
            point = np.dot(H_inv, np.array([j, i, 1]))
            point = point / point[2]
            x, y = int(point[0]), int(point[1])
            if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
                warped_image[i-min_y, j-min_x] = image[y, x]
    return warped_image

def mergeImages(refIm, warpIm, minX, minY, maxX, maxY):
    height = -min(0, minY) + max(refIm.shape[0], maxY)
    width = -min(0, minX) + max(refIm.shape[1], maxX)
    panorama = np.zeros((height, width, 3), np.uint8)
    print(refIm.shape, warpIm.shape, panorama.shape)

    # find the offset of the warpIm in the panorama
    warp_offset_x = 0
    warp_offset_y = 0
    ref_offset_x = 0
    ref_offset_y = 0
    if minY>0:warp_offset_y = minY
    else: ref_offset_y = -minY
    if minX>0:warp_offset_x = minX
    else: ref_offset_x = -minX

    # copy the refIm into the panorama
    panorama[ref_offset_y:ref_offset_y+refIm.shape[0], ref_offset_x:ref_offset_x+refIm.shape[1]] = refIm

    # copy the warpIm into the panorama
    for i in range(warp_offset_y, warp_offset_y+warpIm.shape[0]):
        for j in range(warp_offset_x, warp_offset_x+warpIm.shape[1]):
            if np.any(warpIm[i-warp_offset_y, j-warp_offset_x]):
                panorama[i, j] = warpIm[i-warp_offset_y, j-warp_offset_x]

    return panorama

def warpImage(inputIm, refIm, H):
    h, w = inputIm.shape[:2]
    points = np.array([[0, 0], [0, h], [w, h], [w, 0]])
    warpedPoints = perspectiveTransform(points, H)
    warpedPoints = warpedPoints.squeeze()

    # Compute the bounding box
    minX = int(np.min(warpedPoints[:, 0]))
    minY = int(np.min(warpedPoints[:, 1]))
    maxX = int(np.max(warpedPoints[:, 0]))
    maxY = int(np.max(warpedPoints[:, 1])) 
    
    warpIm = warpPerspective(inputIm, H, minX, minY, maxX, maxY)

    mergeIm = mergeImages(refIm, warpIm, minX, minY, maxX, maxY)
    return warpIm, mergeIm