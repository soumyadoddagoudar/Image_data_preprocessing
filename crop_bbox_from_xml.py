
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:23:20 2018

@author: soumya.doddagoudar



INPUT - give path which has both image and xml files.
OUTPUT - croped object from image stored in respective folder with label name.
"""

import os
import cv2
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    '''
    Reads xml files and stores values in csv file.
    '''
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    image_path = str(input("ENTER PATH which contains images AND ANNOATIONSXML without quotes : \n"))
    #os.path.join(os.getcwd(), 'peson_annotations')
    
    #calling function
    xml_df = xml_to_csv(image_path)
    xml_df.to_csv('labels.csv', index=None)
    print('Successfully converted xml to csv.')
    import csv
    
    #reads csv file and parse through each row
    with open('labels.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        # n value will increment so has to give different image names to be saved
        n=1
        header=1
        for row in readCSV:
            if header==1:
                header=header+1
                continue
            img = cv2.imread(image_path+str(row[0]))
            
            #print(row[0])
           # print(img)
            xmin=int(row[4])
            ymin=int(row[5])
            xmax=int(row[6])
            ymax=int(row[7])
            cropped = img[ymin:ymax, xmin:xmax] 
            #check if already folder with label name exists if not create it.
            if not  os.path.exists(str(image_path+str(row[3]))):
                os.makedirs(image_path+str(row[3]))
            #write a cropped image to respective folder.
            cv2.imwrite(image_path+str(row[3])+"/"+str(row[3])+str(n)+".jpg", cropped)
            n=n+1
          
            #print(row[4],row[5],row[6],row[7])


main()
print("EXECUTION DONE")
