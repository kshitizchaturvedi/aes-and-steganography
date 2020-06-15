'''
Created on Jun 14, 2020

@author: KSHITIZ CHATURVEDI
'''
'''
Created on Apr 21, 2020

@author: KSHITIZ CHATURVEDI
'''
from aes import AES
from aes import unpad
from imagehide import encode
from imageextract import decode
if __name__ == '__main__':
    
    print("press 1 to ENCRYPT A MESSAGE\npress 2 to DECRYPT A MESSAGE\npress 3 to ENCRYPT A MESSAGE AND HIDE IT IN AN IMAGE\npress 4 to DECRYPT AN IMAGE")
    choice=int(input())
    if choice==1:
        text=input("Enter the text to be encrypted:\n")
        key=input("Enter 16 bytes long encryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=obj.encrypt_cbc(text,iv )
        enctext=""
        for i in cipher:
            for j in i:
                enctext+=chr(j)
        print("Here is your encrypted message:",cipher)
        
    elif choice==2:
        print("A list needs to be passed as encrypted text ,so please modify the same in code")
        key=input("Enter 16 bytes long decryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=[[82, 214, 73, 255, 189, 148, 31, 109, 36, 213, 241, 19, 240, 128, 113, 142], [248, 241, 148, 140, 143, 63, 222, 195, 202, 210, 244, 74, 102, 0, 190, 200], [29, 45, 179, 186, 183, 88, 115, 91, 115, 240, 60, 133, 170, 156, 139, 215]]
        msg=obj.decrypt_cbc(cipher, iv)
        msgstr=""
        for i in msg:
            for j in i:
                msgstr+=chr(j)
        print("Here is your decrypted message:",unpad(msgstr))
        
    elif choice==3:
        text=input("Enter the text to be encrypted:\n")
        key=input("Enter 16 bytes long encryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        cipher=obj.encrypt_cbc(text,iv )
        name=input("Enter the name of the image along with proper extension (.jpg or .bmp):\n")
        encode(name,cipher)
        
    elif choice==4:
        name=input("Enter the name of the image to be decrypted along with proper extension (.jpg or .bmp):\n")
        rval=decode(name)
        print("The information hidden in image is:  ",rval)
        nlist=[]
        tlist=[]
        count=0
        for i in rval:
            tlist.append(i)
            if (count+1)%16==0:
                nlist.append(list(tlist))
                tlist.clear()
            count+=1

        key=input("Enter 16 bytes long decryption key:\n")
        while(len(key)!=16):
            key=input("The length of the key needs to be 16, please enter 16 bytes long key\n")
        iv=input("Enter 16 bytes long initialization vector:\n")
        while(len(iv)!=16):
            iv=input("The length of the initialization vector needs to be 16, please enter 16 bytes long iv\n")
        obj=AES(key)
        msg=obj.decrypt_cbc(nlist, iv)
        print(msg)
        msgstr=""
        for i in msg:
            for j in i:
                msgstr+=chr(j)
        print("Here is your decrypted message:",unpad(msgstr))
        
    else:
        print("You've entered a wrong text")
        
        
         
        
        
    
            
