import pandas as pd 
import cv2
filename = []
dataset = pd.read_csv("Train.csv")
cnt = 0
while cnt<900:
	name = './data/frame' + str(cnt) + '.jpg'
	filename.append(name)
	cnt = cnt + 1
for files in filename:
	orig1 = cv2.imread(files)
	orig = cv2.cvtColor(orig1, cv2.COLOR_BGR2GRAY)


	sobel_dx = cv2.Sobel(orig, cv2.CV_64F, 1, 0, ksize=9)

	sobel_dy = cv2.Sobel(orig, cv2.CV_64F, 0, 1, ksize=13)
	magnitude_image = cv2.magnitude(sobel_dx,sobel_dy,orig)

	mag, ang = cv2.cartToPolar(sobel_dx, sobel_dy, magnitude_image) 

	ratio = cv2.sumElems(mag[0])

	print ratio[0]/100
	if (ratio[0]/100 > 12600 and ratio[0]/100 <13447):
		print "image is good"
		#	cv2.imshow("Good quality",orig1)	
	else :
		print "image is bad"
		#cv2.imshow("Bad quality",orig1)	
