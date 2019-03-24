# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:54:22 2018
This function checks whether bbox is inside the rectangle region.
@author: soumya.doddagoudar
"""
import cv2
import numpy as np

def point_poylgontest(Roi_bbox,coord):
    #centroid=object_bbox[:,2]-(object_bbox[2:]-object_bbox[:,2])/2
    centroid = ((coord[0]+coord[2])/2, (coord[1]+coord[3])/2)
    print(centroid)
    left=Roi_bbox[0]
    top=Roi_bbox[1]
    right=Roi_bbox[0]+Roi_bbox[2]
    bottom=Roi_bbox[3]+Roi_bbox[1]
    cnt=[[left,top],[Roi_bbox[0]+Roi_bbox[2],top],[right,bottom],[left,bottom]]
    cnt=np.array(cnt)
    dist = cv2.pointPolygonTest(cnt,(centroid[0],centroid[1]),False)
    print(dist)
    if dist == 1:
        print("point is inside contour" )
    elif dist==-1:
        print("point is outside contour")
    elif dist==0:
        print("point is on contour")
                                                                    
    #point is inside or outside or on the contour (it returns +1, -1, 0 respectively). 
Roi_bbox=[235,85,501-235,233-85]  
coord=(259,147,290,192)  


point_poylgontest(Roi_bbox,coord)
#ROI_bbox-rectangle region --- x,y,w,h(top,left,width,height)
#coord-object/boundingbox coordinates ------(top,left,bottom,right)
