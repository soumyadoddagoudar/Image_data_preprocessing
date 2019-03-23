# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:21:22 2018

import numpy as np
print (img.size)
#print(img.size[0])
height = np.size(img, 0)
width = np.size(img, 1)

filename = os.path.join("D:\\gensimworkspace\\neuralnetworks\\HOG\\person_data\\positive_images_person\\0.png")

height, width = img.shape[:2]

@author: soumya.doddagoudar
"""

from PIL import Image
from PIL import *
import os.path
i=0 #to get the total number of images to get the average
width_sum=0
height_sum=0

for k in os.listdir("D:\\gensimworkspace\\neuralnetworks\\HOG\\person_data\\positive_images_person\\"):
    print("K:",k)
    img=Image.open('D:\\gensimworkspace\\neuralnetworks\\HOG\\person_data\\positive_images_person\\'+k)
    i=i+1
    width, heigth = img.size
    width_sum=width_sum+width
    height_sum=height_sum+heigth
print("i:",i)
print("width_sum: ",width_sum)
print("height_sum:",height_sum)
Average_width=width_sum/i
Average_height=height_sum/i

print("Average_width:",Average_width)
print("Average_height:", Average_height)


"""""Result 2/7/2018
i: 2305
width_sum:  170602
height_sum: 482398
Average_width: 74.01388286334057
Average_height: 209.28329718004338
"""



  



