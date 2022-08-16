from pprint import pprint
import cv2
import sys
import numpy as np


symbolic_list=["#", "-", "*", ".", "+", "o"]
thresh_list=[0,50,100,150,200]

def print_image(array):
    for row in array:
        for i in row:
            print(symbolic_list[int(i)%len(symbolic_list)],end="")  
        print()

def image_code(image):
    height,width=image.shape
    print(height,width)
    resize_height=int(height/40)
    resize_width=int(width/20)
    print(resize_height,resize_width)
    """it create (10,21) of height and width"""

    new_image=cv2.resize(image,(resize_width,resize_height))
    print(new_image)
    arr_image=np.zeros(new_image.shape)

    for i,thresh in enumerate(thresh_list):
        arr_image[new_image>thresh]=i
    return arr_image

if __name__=="__main__":
    if len(sys.argv)<2:
        image_path=r'C:\tutorial\project\html\test4.jpg'
    image=cv2.imread(image_path,0)
    result=image_code(image)
    print_image(result)
