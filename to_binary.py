import cv2

ALL = 0
NEXT = 1
def tobnr(img, sc=10):   # scale ratio
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    img = cv2.medianBlur(img, 5)
    scaled = cv2.resize(img, (int(w/sc), int(h/sc)), interpolation=cv2.INTER_AREA)
    ret, thresh = cv2.threshold(scaled, 127, 225, cv2.THRESH_BINARY)
    laplacian = cv2.Laplacian(thresh, 0)
    blank_image_large = cv2.resize(laplacian, (w, h), interpolation=cv2.INTER_AREA)
    #cv2.imshow('threshold', thresh)
    #cv2.imshow('laplacian', laplacian)
    return laplacian, blank_image_large


def tobnr2(img, sc=10):   # scale ratio
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    img = cv2.medianBlur(img, 5)
    scaled = cv2.resize(img, (int(w/sc), int(h/sc)), interpolation=cv2.INTER_AREA)
    laplacian = cv2.Laplacian(scaled, 0)
    ret, thresh = cv2.threshold(laplacian, 20, 255, cv2.THRESH_BINARY)
    blank_image_large = cv2.resize(thresh, (w, h), interpolation=cv2.INTER_AREA)
    #cv2.imshow('threshold', thresh)
    #cv2.imshow('laplacian', laplacian)
    return thresh, blank_image_large


def check_binary_delete(bnr, w, h, mode=0):   # delete pixels in influenced area
    for i in range(0, h):  # put blocks on stripe image
        for j in range(0, w):
            if bnr[i, j] == 0:
                pass
            else:
                if mode == 0:
                    bnr[i:i+1, j+1:j+6] = 0   # delete pixels in same line
                elif mode == 1:
                    pass
                edge_l = j - 4
                if edge_l < 0:
                    edge_l = 0
                bnr[i+1:i+2, edge_l:j+6] = 0   # delete pixels in next line
    return bnr
