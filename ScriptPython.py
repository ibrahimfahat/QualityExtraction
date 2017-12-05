# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:33:12 2017

@author: ibrahim
"""

import cv2
import numpy as np
import os
import math
import operator

#def quality_filter(im)


cap = cv2.VideoCapture('video.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
files = []
currentFrame = 0
while(currentFrame<900):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(ret) 
    #print('\n')
    #print(frame)
   
    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    
    cv2.imwrite(name, frame)
    files.append(name)
    currentFrame += 1
cap.release()
# When everything done, release the capture

#Starting to Indicate Picture 
#The methode is simple Compute a soble over X and Y, and Calculate the magnitude of pixels , if pixels mangnitude is very hiegh the is a Flou Noise , in that Pixel

all_ratio = {}
for filename in files:
    orig = cv2.imread(filename)

    sobel_dx = cv2.Sobel(orig, cv2.CV_64F, 1, 0, ksize=5)
    sobel_dy = cv2.Sobel(orig, cv2.CV_64F, 0, 1, ksize=5)
    magnitude_image = cv2.magnitude(sobel_dx,sobel_dy,sobel_dx)
    mag, ang = cv2.cartToPolar(sobel_dx, sobel_dy, magnitude_image) 

    ratio = cv2.sumElems(mag[0])
    all_ratio[filename] = ratio[0]

sorted_ratio = sorted(all_ratio.items(), key=operator.itemgetter(1))
index = 0
print(" Rang | Fichier      | Valeur calculee")
print("------|--------------|----------------")

table = []
for (filename, ratio) in reversed(sorted_ratio):
    print(" %04d | %s | %d" % (index, filename, ratio)) 
    table.append((filename,ratio))
    
#print(table[0][0], table[0][1])
img_rgb = cv2.imread(table[0][0])
img_gray =  cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('image.jpg',0)
#tamplate_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imwrite('res.jpg',img_rgb)

#str1 = cv2.imread('./data/frame'+str(maxmin[0][1])+'.jpg',0)

#cv2.imshow(str(maxmin[0][1]),str1)
#str2 = cv2.imread('./data/frame'+str(maxmin[len(maxmin)-1][1])+'.jpg')
#cv2.imshow(str(maxmin[len(maxmin)-1][0]),str2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

