import cv2
import numpy as np

img=cv2.imread('/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/rice_grains.jpg',cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)


R, G, B = cv2.split(img)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Red.jpg", R)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Green.jpg",G)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Blue.jpg",B)


H,S,V=cv2.split(hsv)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Hue.jpg",H)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Saturation.jpg",S)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Value.jpg",V)


Y,Cb,Cr=cv2.split(ycrcb)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Y.jpg",Y)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Cb.jpg",Cb)
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/ex2/rice_grains/Cr.jpg",Cr)