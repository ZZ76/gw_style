import cv2
import gw_img as gi

cap = cv2.VideoCapture(0)

while(True):
    _, frame = cap.read()
    ho, wo, _ = frame.shape
    frame, bnr_lrg, bnr_lrg2 = gi.read_img(frame, wn=400, wn2=600)
    cv2.imshow('lrg', bnr_lrg)
    cv2.imshow('lrg2', bnr_lrg2)
    cv2.imshow('main', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
