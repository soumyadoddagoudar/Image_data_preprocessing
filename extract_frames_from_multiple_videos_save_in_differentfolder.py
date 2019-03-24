# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:27:49 2019

@author: soumya.doddagoudar


This code extracts the frame from different videos stored in a folder and save the framea in respective video name folder.
"""

#extract frames for every second
import cv2
import math
import os

rootdir = str(input("ENTER path which has input videos: \n"))
def main(rootdir):
    for directory, subdirectories, files in os.walk(rootdir):
        for file in files:
            file=os.path.join(directory, file)
            if file.split(".")[-1]=="mp4":
                videoFile = file
                name=(videoFile.split('\\')[-1]).split('.')[-2]
                filepath=videoFile.split('.')[:-1]
                str1 = ''.join(filepath)
                os.mkdir(str1)
                #print(str1)
                cap = cv2.VideoCapture(videoFile)
                frameRate = cap.get(5)//4
                while(cap.isOpened()):
                    frameId =cap.get(1) #current frame number
                    ret, frame = cap.read()
                    if (ret != True):
                        break
                    if (frameId % math.floor(frameRate) == 0):
                        filename = str1+"\\"+ str(name)+ str(int(frameId)) + ".jpg"
                        cv2.imwrite(filename, frame)
                cap.release()
main(rootdir)
print("done")


