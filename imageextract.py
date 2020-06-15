'''
Created on Jun 14, 2020

@author: KSHITIZ CHATURVEDI
'''
from __future__ import print_function
from PIL import Image
def decode(image_name):
    im=Image.open(image_name)
    if(im.mode!= "RGB"):
        print("PLEASE PROVIDE A SUITABLE IMAGE FORMAT")
        exit()
    
    width,height=im.size  
    pix_map=im.load()
    newstr=""
    for count in range(8):
        row=count//width
        col=count%width
        r,g,b=pix_map[col,row]
        newstr+=bin(r)[-1]
        newstr+=bin(g)[-1]
        newstr+=bin(b)[-1]
    length=int(newstr,2)
   # print(length)
    #length is the length of the list in bytes not bits
    #index is the index to pixel in pixel map
    newstr=""
    for index in range(8,(length*8)//3+8):
        row=index//width
        col=index%width
        r,g,b=pix_map[col,row]
        newstr+=bin(r)[-1]
        newstr+=bin(g)[-1]
        newstr+=bin(b)[-1]
    
    if (length*8)%3==1:
        index+=1
        row=index//width
        col=index%width
        r,g,b=pix_map[col,row]
        newstr+=bin(r)[-1]
        
    if (length*8)%3==2:
        index+=1
        row=index//width
        col=index%width
        r,g,b=pix_map[col,row]
        newstr+=bin(r)[-1]
        newstr+=bin(g)[-1]
    newlist=[]
    for i in range(length):
        start=8*i
        newlist.append(int(newstr[start:start+8],2))
    return newlist
        

#print(decode("RAY_hidden.bmp"))
    