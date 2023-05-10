# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)
	image1 = cv2.imread(/images/videoname1 + '1')
image2 = cv2.imread(/images/videoname1 + '2')
image3 = cv2.imread(/images/videoname1 + '3')
image4 = cv2.imread(/images/videoname2 + '1')
image5 = cv2.imread(/images/videoname2 + '2')
image6 = cv2.imread(/images/videoname2 + '3')
	
	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth


videoname1 = intruding.mp4
videoname2 = extruding.mp4



marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

# loop over the images
for imagePath in sorted(paths.list_images(/images)):
	# load the image, find the marker in the image, then compute the
	# distance to the marker from the camera
	image 1= cv2.imread(imagePath)
	marker = find_marker('image' + str(n))
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
	n+=1
	if n>6
	break
	
