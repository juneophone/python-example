# -*- encoding: utf-8 -*-

# 將圖片轉為素描圖
"""
@author		: 	jongwaye.ou
@Version 	: 	1.0
@Description:	Convert pictures into sketches.
"""

# import the necessary packages
import numpy as np
import cv2
import os

# input image path
imagePath = '../demo_image/brid_01.jpg'
image = cv2.imread(imagePath)

# process image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(image, (21, 21), 0, 0)
img_blend = cv2.divide(image, img_blur, scale=256)

# process file path and name
(filepath, tempfilename) = os.path.split(imagePath)
(filename, extension) = os.path.splitext(tempfilename)

# save image 
cv2.imwrite(filename + "_output_gray.png", img_blend)