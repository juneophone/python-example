# -*- encoding: utf-8 -*-

"""
@author		: 	jongwaye.ou
@Version 	: 	1.0
@Description:	Color recognition
"""

# import the necessary packages
import numpy as np
import cv2
import os

# process file path and name
def processFileName(sPath):
	global filename, extension
	(filepath, tempfilename) = os.path.split(sPath)
	(filename, extension) = os.path.splitext(tempfilename)
	
# data setting----------------------------------------

# input image path
imagePath = '../demo_image/brid_02.jpg'

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# ----------------------------------------------------

image = cv2.imread(imagePath)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask = mask)

  
# save image
processFileName(imagePath)
cv2.imwrite(filename + "_mask.png", mask)
cv2.imwrite(filename + "_result.png", result)