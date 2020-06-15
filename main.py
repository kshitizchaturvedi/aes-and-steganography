'''
Created on Apr 21, 2020

@author: KSHITIZ CHATURVEDI
'''
from aes import AES
from aes import unpad
if __name__ == '__main__':
    
    
    text="Two One Nine TwoTwo One Nine abcd" #input("Enter plain text")
    key="Thats My Kung Fu"  #input("Enter key")
    iv="given initializa"
    obj=AES(key)
    cipher=obj.encrypt_cbc(text,iv )
    print(cipher)
    msg=obj.decrypt_cbc(cipher, iv)
    print(msg)
    msgstr=""
    for i in msg:
        for j in i:
            msgstr+=chr(j)
    print(unpad(msgstr))
    
            
