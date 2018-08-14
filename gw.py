import cv2
import numpy as np
from numpy import random as nr

cl1, cl2 = (0, 0, 0), (255, 255, 255)   # bnw
cl1, cl2 = (178, 103, 0), (95, 105, 242)   # rb
#cl1, cl2 = (56, 37, 16), (208, 230, 220)   # blue
sf = 15   # scale factor, also it is the height of stripes
cr = 0.8   # circle ratio, the ratio of radius and stripe height
r = int(cr*sf)  # radius
stripe = None

def create_stripe(w, h):   # create stripe image
    img = np.zeros((sf * h, sf * w, 3), np.uint8)
    for i in range(0, h):
        if (i % 2) == 0:
            img[sf*i:sf*(i+1), 0:sf*w] = cl1
        else:
            img[sf*i:sf*(i+1), 0:sf*w] = cl2
    return img


def putblock(img, bnr, w, h):   # put blocks on stripe image
    for i in range(0, h):
        for j in range(0, w):
            if bnr[i, j] == 0:
                if (i % 2) == 0:
                    img[sf * i:sf * (i + 1), sf * j:sf * (j + 1)] = cl2
                else:
                    img[sf * i:sf * (i + 1), sf * j:sf * (j + 1)] = cl1
    return img


def putcircles2(img, cl, bgcl, i, j):   # put 2 circles
    img[sf * i:sf * (i + 1), (sf * j):sf * (j + 2)] = bgcl  # put background color
    cv2.circle(img, (sf * j, int(sf * (i + 1 - cr)) - 1),  r, cl, -1, lineType=cv2.LINE_AA)  # lineType=cv2.LINE_AA, 4, 8
    cv2.circle(img, (sf * (j + 2), int(sf * (i + 1 - cr)) - 1),  r, cl, -1, lineType=cv2.LINE_AA)
    img[sf * (i + 1):sf * (i + 2), (sf * j)-r:sf * (j + 2)+r] = bgcl   # put background color on next line


def putcircles3(img, cl, bgcl, i, j):   # put 3 circles
    img[sf * i:sf * (i + 1), (sf * j):int(sf*(2+2*cr+j))] = bgcl  # put background color
    cv2.circle(img, (sf*j, int(sf*(i+1-cr))-1),  r, cl, -1, lineType=cv2.LINE_AA)  # lineType=cv2.LINE_AA, 4, 8
    cv2.circle(img, (int(sf*(1+cr+j)), int(sf*(i+1-cr))-1), r, cl, -1, lineType=cv2.LINE_AA)
    cv2.circle(img, (int(sf*(2+2*cr+j)), int(sf*(i+1-cr))-1), r, cl, -1, lineType=cv2.LINE_AA)
    img[sf * (i + 1):sf * (i + 2), (sf * j)-r:int(sf*(2+2*cr+j))+r] = bgcl   # put background color on next line


def gw_filter(img, bnr, w, h):   # put circles on stripe image
    for i in range(0, h):
        for j in range(0, w):
            if bnr[i, j] == 0:
                pass
            else:
                p = nr.randint(0, 5)   # probability of putting 3 circles
                #print(p)
                if p <= 3:   # p<=3
                    if (i % 2) == 0:
                        cl, bgcl = cl1, cl2
                        putcircles2(img, cl, bgcl, i, j)
                    else:
                        cl, bgcl = cl2, cl1
                        putcircles2(img, cl, bgcl, i, j)
                else:
                    if (i % 2) == 0:
                        cl, bgcl = cl1, cl2
                        putcircles3(img, cl, bgcl, i, j)
                    else:
                        cl, bgcl = cl2, cl1
                        putcircles3(img, cl, bgcl, i, j)
    return img


