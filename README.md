Image_data_preprocessing

#Introduction
 	Python code for some preprocessing of IMAGE data.
  
Quick start
 	Required python packages:
•	pandas  0.19.2
•	opencv 3.4.2

crop_bbox_from_xml.py- overview
In deep learning model training we prepare a data which includes image and corresponding xml files which contains bounding box(bbox) of object and label. This data can be prepared using labelimg tool(https://github.com/qaprosoft/labelImg) or other tools. In this repository I uploaded 2 example image and xml files for review. Sometimes we need only exact croped object out of image to prepare dataset. So this code helps you to do that.
Example:


 
 	To run the file open spyder or Anaconda prompt and type below command:
Python crop_bbox_from_xml.py
It will ask for path, provide your system path where image and corresponding xml files are stored.




