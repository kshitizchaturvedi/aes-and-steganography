'''
Created on May 3, 2020

@author: KSHITIZ CHATURVEDI
'''
from __future__ import print_function
from PIL import Image

def length_bits(length):
    tstr=bin(length)
    tstr=tstr[2:]
    count=24-len(tstr)
    newstr=""
    for i in range(count):
        newstr+='0'
    tstr=newstr+tstr
    a=int(tstr[:8],2)
    b=int(tstr[8:16],2)
    c=int(tstr[16:24],2)
    return (a,b,c)



def encode(image_name,intext):
    # text is a list containing the ascii value of characters
    text=[]
    for i in intext:
        for j in i:
            text.append(j)
    im=Image.open(image_name)
    if(im.mode!= "RGB"):
        print("PLEASE PROVIDE A SUITABLE IMAGE FORMAT")
        exit()
    
    width,height=im.size  
    print(im.size)  
    avl_chars=((width*height*3)//8)-3
    if(len(text)>avl_chars or len(text)>2**24):
        print("MESSAGE IS TOO LONG TO BE ACCOMODATED IN GIVEN IMAGE")
        exit()
    
    new_img=im.copy()
    pix_map=new_img.load()
    a,b,c=length_bits(len(text))
    text.insert(0,c)
    text.insert(0,b)
    text.insert(0,a)
    textstr=""
    for i in text:
        newstr=""
        binstr=bin(i)
        binstr=binstr[2:]
        for m in range(8-len(binstr)):
            newstr+='0'
        binstr=newstr+binstr
        textstr=textstr+binstr
    print(textstr)
    print(len(textstr)//3)
    bitno=0   #bitno is index to textstr 
    #count is index to pixel of pixelmap   
    for count in range(len(textstr)//3):
        row=count//width
        col=count%width
        r,g,b=pix_map[col,row]
        bit=int(textstr[bitno])
        if bit==0:
            r&=(~1)
        else:
            r|=1
        bitno+=1
        bit=int(textstr[bitno])
        if bit==0:
            g&=(~1)
        else:
            g|=1
        bitno+=1
        bit=int(textstr[bitno])
        if bit==0:
            b&=(~1)
        else:
            b|=1
        bitno+=1
        pix_map[col,row]=(r,g,b)
        print("count=",count,pix_map[col,row])
    
    remaining=len(textstr)%3
    if remaining==1:
        count+=1
        row=count//width
        col=count%width
        r,g,b=pix_map[col,row]
        bit=int(textstr[bitno])
        if bit==0:
            r&=(~1)
        else:
            r|=1
        pix_map[col,row]=(r,g,b)
        print(pix_map[col,row])

        
        
    if remaining==2:
        count+=1
        row=count//width
        col=count%width
        r,g,b=pix_map[col,row]
        bit=int(textstr[bitno])
        if bit==0:
            r&=(~1)
        else:
            r|=1
        bitno+=1
        bit=int(textstr[bitno])
        if bit==0:
            g&=(~1)
        else:
            g|=1
        pix_map[col,row]=(r,g,b)
        print(pix_map[col,row])

        
    new_name=image_name[:-4]+"_hidden.bmp"
    new_img.save(new_name)
    print("The image has been encrypted and saved")
    print("count=",count)

    
#text=[42, 214, 73, 255, 189, 148, 31, 109, 36, 213, 211, 19, 240, 128, 113, 142,248, 241, 148, 140, 143, 63, 222, 195, 202, 210, 244, 74, 102, 0, 190, 200,29, 45, 179, 186, 183, 88, 115, 91, 115, 240, 60, 133, 170, 156, 139, 215]
#name="RAY.BMP"
#encode(name, text)

    
    