# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:17:55 2018
ffmpeg -ss 0 -i corridor2_sep11.mp4 -t 16 -c copy corridor2_out.mp4


extract_frames_from_vid_from_multiple videos_save_in_differentfolder
"""

#extract frames for every second
import cv2
import math
import os

rootdir = "D:\\gensimworkspace\\neuralnetworks\\input_videos\\take2\\"

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
        #filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"

                
        #print("writing")
        




#videoFile.split('.')[:-1]
#imagesFolder = "/other/images"
 #frame rate
#frameRate = cap.get(5)//4 #frame rate






'''

####################################

videoFile = "D:\\gensimworkspace\\neuralnetworks\\input_videos\\overhead-1.mp4"
name=(videoFile.split('\\')[-1]).split('.')[-2]
filepath=videoFile.split('.')[:-1]
str1 = ''.join(filepath)
#videoFile.split('.')[:-1]
#imagesFolder = "/other/images"
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
#frameRate = cap.get(5)//4 #frame rate

while(cap.isOpened()):
    frameId =cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = str1+"\\"+ str(name)+ str(int(frameId)) + ".jpg"
        #filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"

        cv2.imwrite(filename, frame)
        #print("writing")
cap.release()


############################

import cv2
import imutils
print(cv2.__version__)
vidcap = cv2.VideoCapture("D:\\gensimworkspace\\neuralnetworks\\input_videos\\store1.mp4")
success,image = vidcap.read()

count = 0
success = True

while success:
  #image=imutils.resize(image,600,450)
  if count%8 ==0:
      cv2.imwrite("D:\\gensimworkspace\\neuralnetworks\\input_videos\\store1_frames\\frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1
  
  
import cv2
vidcap = cv2.VideoCapture('D:\\gensimworkspace\\neuralnetworks\\input_videos\\ibrands.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)

vidcap.set(cv2.CAP_PROP_POS_MSEC,20000)      # just cue to 20 sec. position
success,image = vidcap.read()
if success:
    cv2.imwrite("frame20sec.jpg", image)     # save frame as JPEG file
    #cv2.imshow("20sec",image)
   # cv2.waitKey()      
   
framerate = vidcap.get(5)
print ("framerate:", framerate)
framecount = vidcap.get(7)
print( "framecount:", framecount)



'''



'''
ibrands.mp4
framerate: 9.997658664347846
framecount: 14151.0


'''