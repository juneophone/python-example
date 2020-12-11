

# import the necessary packages
import numpy as np
import cv2

# input image path
imagePath = '../demo_image/kodim23.bmp'
image = cv2.imread(imagePath)

boundaries = {'B': ([0, 0, 0], [255, 0, 0]),
              'G': ([0, 0, 0], [0, 255, 0]),
              'R': ([0, 0, 0], [0, 0, 255])}

# loop over the boundaries
for key in boundaries:
    low, up = boundaries[key]
    # create NumPy arrays from the boundaries
    lower = np.array(low, dtype="uint8")
    upper = np.array(up, dtype="uint8")
    
    # find the colors within the specified boundaries and apply
    # the mask    
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    
    # save the images
    saveImage = np.hstack([image, output])
    #imgBuf = cv2.cvtColor(saveImage, cv2.COLOR_BGR2RGB)
    cv2.imwrite("output_" + key + ".png", saveImage)