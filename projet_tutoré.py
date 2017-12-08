import cv2
import numpy as np
import os
import math
import operator
cap = cv2.VideoCapture('video.avi')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
files = []
currentFrame = 0
while(currentFrame<9000):
    if (currentFrame % 9 == 0):
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
        # To stop duplicate images
    currentFrame += 1
cap.release()
# When everything done, release the capture

    
