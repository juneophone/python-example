# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:46:50 2020

@author: jongwaye.ou
"""


from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "brid_03.jpg"), output_image_path=os.path.join(execution_path , "result_image.jpg"), minimum_percentage_probability=80)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")