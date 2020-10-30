# from cv2 import *
import cv2

#global variable for mouse
clicked = False
x = y = r = b = g =0

def getMousePosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = image[x,y,0]
        g = image[x,y,1]
        r = image[x,y,2]
        print(b,g,r)

image = cv2.imread('hand.jpg')

cv2.imshow('Image',image)
cv2.setMouseCallback('Image',getMousePosition)
cv2.waitKey(0)
cv2.destroyAllWindows()