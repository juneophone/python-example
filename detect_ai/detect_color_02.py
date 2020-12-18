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
imagePath = '../demo_image/brid_03.jpg'

# define range of blue color in HSV
lower_red_0 = np.array([0, 70, 0]) 
upper_red_0 = np.array([5, 255, 255])
lower_red_1 = np.array([175, 70, 0]) 
upper_red_1 = np.array([180, 255, 255])

# ----------------------------------------------------

image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to get only blue colors
mask0 = cv2.inRange(hsv, lower_red_0, upper_red_0)
mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
mask  = cv2.bitwise_or(mask0, mask1) 

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask = mask)

  
# save image
processFileName(imagePath)
cv2.imwrite(filename + "_mask.png", mask)
cv2.imwrite(filename + "_result.png", result)