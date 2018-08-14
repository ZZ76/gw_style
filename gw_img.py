import cv2
import to_binary
import gw
import numpy as np
from numpy import random as nr


def random_binary(w, h):
    binary_image = np.zeros((h, w), np.uint8)
    for i in range(1, h-1):   # the first and the last line are empty
        for l in range(0, 1):   # how many pixels in each line
            p = nr.randint(1, w-1)   # and the first and the last row are also empty
            binary_image[i, p] = 255
    binary_image_large = cv2.resize(binary_image, (15*w, 15*h), interpolation=cv2.INTER_AREA)
    return binary_image, binary_image_large


def random_line(w, h):   # generate random line
    f = False
    binary_image = np.zeros((h, w), np.uint8)
    for k in range(1, 3):
        for i in range(k, h-1, 2):   # the first and the last line are empty
            if i == 1 or f is False:
                p = nr.randint(1, w-1)   # and the first and the last row are also empty
                binary_image[i, p] = 255
                f = True
            else:
                offset = nr.randint(-3, 4)
                p = p + offset
                if p >= 1 and p <= w-1:
                    binary_image[i, p] = 255
                else:
                    f = False
    binary_image_large = cv2.resize(binary_image, (gw.sf*w, gw.sf*h), interpolation=cv2.INTER_AREA)
    return binary_image, binary_image_large


def gw_line(w, h, img=None):   # for random line
    if img is None:
        bnr, bnr_lrg = random_line(w, h)
    else:
        print(img)
        bnr = cv2.imread(img)   # read a binary image
        bnr = cv2.cvtColor(bnr, cv2.COLOR_BGR2GRAY)
        h, w = bnr.shape
        bnr_lrg = cv2.resize(bnr, (gw.sf*w, gw.sf*h), interpolation=cv2.INTER_AREA)
    bnr2 = to_binary.check_binary_delete(bnr, w, h)
    bnr_lrg2 = cv2.resize(bnr2, (gw.sf * w, gw.sf * h), interpolation=cv2.INTER_AREA)
    bnr = to_binary.check_binary_delete(bnr, w, h)
    img = gw.create_stripe(w, h)
    img = gw.gw_filter(img, bnr, w, h)
    return bnr_lrg, bnr_lrg2, img


def gw_img(img):   # for image
    bnr, bnr_lrg = to_binary.tobnr2(img, 5)   # binary method
    h, w = bnr.shape
    bnr = to_binary.check_binary_delete(bnr, w, h, mode=0)
    bnr_lrg2 = cv2.resize(bnr, (gw.sf * w, gw.sf * h), interpolation=cv2.INTER_AREA)
    img = gw.create_stripe(w, h)
    img = gw.gw_filter(img, bnr, w, h)
    return bnr_lrg, bnr_lrg2, img

# img
img = cv2.imread('kim.jpg')
ho, wo, _ = img.shape
wn = 300
hn = int(wn*ho/wo)
img = cv2.resize(img, (wn, hn))
bnr_lrg, bnr_lrg2, img = gw_img(img)
wn2 = 400
hn2 = int(wn2*ho/wo)
bnr_lrg2 = cv2.resize(bnr_lrg2, (wn2, hn2))
img = cv2.resize(img, (wn2, hn2))

# random line
#w, h = 30, 40
#bnr_lrg, bnr_lrg2, img = gw_line(w, h, img=None)

cv2.imshow('lrg', bnr_lrg)
cv2.imshow('lrg2', bnr_lrg2)
cv2.imshow('gw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
