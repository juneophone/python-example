# -*- coding: utf-8 -*-
"""
@author		: 	jongwaye.ou
@Version 	: 	1.0
@Description:	Histogram Of RGB Images
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

input_filepath = 'images/kodim23.bmp'
#input_filepath = 'demo_image/flower.png'
img = cv2.imread(input_filepath)

# RGB
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hist = [cv2.calcHist([imgRGB], [k], None, [256], [0, 256]) for k in range(3)]
x = np.arange(256) + 0.5
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist) 

# 將 RGB 分別以灰度顯示圖片
(r,g,b) = cv2.split(imgRGB)
img_r = cv2.merge([r,r,r])
img_g = cv2.merge([g,g,g]) 
img_b = cv2.merge([b,b,b]) 

# plot 
plt.figure(figsize=(18, 5))
co = 240
plt.subplot(co+1), plt.imshow(imgRGB), plt.title('Image'), plt.axis('off')
plt.subplot(co+2), plt.imshow(img_r), plt.title('R'), plt.axis('off')
plt.subplot(co+3), plt.imshow(img_g), plt.title('G'), plt.axis('off')
plt.subplot(co+4), plt.imshow(img_b), plt.title('B'), plt.axis('off')

plt.subplot(co+5), plt.plot(x, hist[0], label='R', color='red'), \
                   plt.plot(x, hist[1], label='G', color='green'), \
                   plt.plot(x, hist[2], label='B', color='blue')
                   
plt.subplot(co+6), plt.plot(x, hist[0], color = 'r')
plt.subplot(co+7), plt.plot(x, hist[1], color = 'g')
plt.subplot(co+8), plt.plot(x, hist[2], color = 'b')

#plt.savefig('output/RGB_Histogram.png', dpi = 300);
plt.show()
