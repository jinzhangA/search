import numpy as np
import cv2
import sys


# This part of code took some reference from:
# http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
def extract_feature(image, bin_numbers):
    # cv2.imshow("Original image", image)
    # cv2.waitKey(0)

    # convert the image to HSV color
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV image", image)
    # cv2.waitKey(0)

    feature_vector = []
    # extract the size of the image
    (height, width) = image.shape[:2]
    # the X and Y center of the image
    (cX, cY) = (int(0.5*width), int(0.5*height))
    # build segments
    segments = [(0, cX, 0, cY),  # upper left
                (cX, width, 0, cY),  # upper right
                (cX, width, cY, height),  # lower right
                (0, cX, cY, height)]  # lower left

    # build the center mask
    rec = np.zeros((height, width), dtype="uint8")
    cv2.rectangle(rec, (int(0.5*cX), int(0.5*cY)), (int(1.5*cX), int(1.5*cY)), 255, -1)

    # add the four fragments' histogram to the feature vector
    for (X0, X1, Y0, Y1) in segments:
        corner = np.zeros((height, width), dtype="uint8")
        cv2.rectangle(corner, (X0, Y0), (X1, Y1), 255, -1)
        corner = cv2.subtract(corner, rec)
        # cv2.imshow('masked', corner)
        # cv2.waitKey(0)
        # res = cv2.bitwise_and(image, image, mask=corner)
        # cv2.imshow('masked image', res)
        # cv2.waitKey(0)
        corner_hist = cv2.calcHist([image], [0, 1, 2], corner, bin_numbers, [0, 180, 0, 256, 0, 256])
        corner_hist = cv2.normalize(corner_hist).flatten()
        feature_vector.extend(corner_hist)
    # cv2.imshow('masked', rec)
    # cv2.waitKey(0)
    # res = cv2.bitwise_and(image, image, mask=rec)
    # cv2.imshow('masked image', res)
    # cv2.waitKey(0)

    # add the center fragment's histogram to the feature vector
    center_hist = cv2.calcHist([image], [0, 1, 2], rec, bin_numbers, [0, 180, 0, 256, 0, 256])
    center_hist = cv2.normalize(center_hist).flatten()
    feature_vector.extend(center_hist)

    return np.array(feature_vector)

# this function return the chi-2 distance of two histograms
def chi2_distance(histA, histB):
    histA = np.array(histA, dtype='float32')
    histB = np.array(histB, dtype='float32')
    d = cv2.compareHist(histA, histB, cv2.cv.CV_COMP_CHISQR)
    return d
