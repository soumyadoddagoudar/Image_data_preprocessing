
import os 
from xml.etree import ElementTree

def main():

  path =str(input("Enter path for annoations/xml folder without quotes"))
  image_path=str(input("Enter path for image folder without quotes"))

  temp = [ f for  f in os.listdir(path) if f.endswith('.xml') ]


  for fileName in temp:
      filepath = path+fileName
      im_path=image_path+fileName.split('.')[-2]+'.jpg'
      print(filepath)
      e = ElementTree.parse(filepath)
      root = e.getroot()
      obj_xml = root.findall('object')
      if len(obj_xml)==0:
          os.remove(filepath)
          os.remove(im_path)
          
          
main()
