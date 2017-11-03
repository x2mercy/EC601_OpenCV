#Copyright 2017 mengxi wang wmx@bu.edu 
import numpy as np  
import cv2  
  
baboon = cv2.imread("/Users/wangmengxi/Documents/mercy/ec601/openCV/OpenCV_homework/Test_images/baboon.jpg")
hsv=cv2.cvtColor(baboon,cv2.COLOR_BGR2HSV)
ycrcb=cv2.cvtColor(baboon,cv2.COLOR_BGR2YCrCb)
(b,g,r) = baboon[20,25]
(Cr,Cb,Y)=ycrcb[20,25]
(v,s,h)=hsv[20,25]
#print("baboon.jpg:")
print("BGR:")

print(b,g,r)

print("ycrcb:")

print(Cr,Cb,Y)

print("hsv:")
print(v,s,h)


