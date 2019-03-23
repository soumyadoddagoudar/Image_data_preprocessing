# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:21:22 2018

@author: soumya.doddagoudar

This code returns average image width and height off all images in a given folder.
"""

from PIL import Image
from PIL import *
import os.path
i=0 #to get the total number of images to get the average
width_sum=0
height_sum=0
inputpath=str(input("ENTER path to folder which contains images: \n"))
for k in os.listdir(inputpath):
    print("K:",k)
    img=Image.open(inputpath+k)
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






  



