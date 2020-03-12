# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:50:02 2019

@author: Abhishek
"""

import cv2
# import numpy as num
# from skimage.filters import unsharp_mask
# from skimage.feature import hog

count = 0
CasFile_face = cv2.CascadeClassifier('G:/IPPR/face_img/Haarcascades/haarcascade_frontalface_alt2.xml')
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture('G:/IPPR/face_img/Sample.mp4')
dim = (75,75)
ret = True
frc = 0  
while(ret == True):
    ret,frame = cap.read()
    if ret == False:
        break
    #print(ret)
    frc = frc+1
    cv2.imshow('image',frame)
    cv2.waitKey(5)
    # Load our image then convert it to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = CasFile_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(5,5))
    #s_img = unsharp_mask(frame, radius=1, amount=1)
    if faces is ():
        pass
    else:
        for x,y,w,h in faces:
            count = count + 1     
            c_img = gray[y:y+h, x:x+w]
            #gray = cv2.cvtColor(c_img, cv2.COLOR_BGR2GRAY)
            c_img = cv2.resize(c_img,dim)
            fin = cv2.resize(c_img,dim)
            cv2.imwrite('G:/IPPR/face_img/Sampout/'+str(count)+'.jpg',fin)
            #fd,hog_face = hog(fin, orientations=8, pixels_per_cell=(16, 16),cells_per_block=(1, 1), visualize=True, multichannel=False)
            #cv2.imwrite('G:/IPPR/face_img/Hogout/frame'+str(frc)+'face'+str(count)+'.jpg',hog_face)
cv2.destroyAllWindows()           