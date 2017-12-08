# cmd  python flou.py --images nom_de_dossier 
import cv2 
from imutils import paths
import argparse
import csv
import numpy
import scipy.stats
def variance_of_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
	help="path to input directory of images")
# in the next line you can fix your own threshold of image bluriness
ap.add_argument("-t", "--threshold", type=float, default=110.0,
	help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())
l = []
for imagePath in paths.list_images(args["images"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    snr = scipy.stats.signaltonoise(gray, axis=None)
    if fm < args["threshold"] :
        l.append((snr,fm,0))
    else:
        l.append((snr,fm,1))
print (l)
with open('persons.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['id','snr','indice','class'])
    cnt = 0
    for ele in l :
        filewriter.writerow([cnt,ele[0],numpy.round(ele[1]),ele[2]])
        cnt = cnt+1
