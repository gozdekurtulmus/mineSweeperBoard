# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:01:52 2020

@author: HP
"""

import random

def isBomb(myArray,a,b):
    if ( myArray[a][b] == "#"):       
        return True
    return False

def letsCheck(myArray,a,b):
    
    c=0
    if (myArray[a][b] != "#"): 
       
        if ( a!=0 ):
            if (isBomb(myArray,a-1,b)):          
                c+=1  # i-1  - j                 
                
            if(b != len(myArray)-1):
                if(isBomb(myArray,a-1,b+1)):
                    c+=1 # i-1  j+1
                    
            if(b != 0):            
                if (isBomb(myArray,a-1,b-1)): 
                    c+=1 #i-1 j-1
                
        if ( a!= len(myArray)-1):
            
            if(isBomb(myArray,a+1,b)):
                c+=1
                
            if (b != len(myArray)-1):
                if(isBomb(myArray,a+1,b+1)):
                    c+=1                
                    
            if  (b !=0):
                if(isBomb(myArray,a+1,b-1)):
                    c+=1
        
        if ( b!= len(myArray)-1):
            if(isBomb(myArray,a,b+1)):
                c+=1 # i - j+1
            
        if( b != 0):
            if(isBomb(myArray,a,b-1)):
                c+=1# i - j-1
                
        myArray[a][b]=str(c)
            

if __name__ == "__main__":
    fieldLength = random.randint(5,15)
    mineField = [["-" for x in range(fieldLength)] for y in range(fieldLength)]

    for i in range(fieldLength-1):
        for j in range(fieldLength-1):
            number = random.randint(1,10)
            if(number == 1):
                mineField[i][j] = "#"


    for i in range(fieldLength):
        for j in range(fieldLength):
                letsCheck(mineField,i,j)

    liste=[]
    for line in mineField:
     liste.append(" ".join(line))

    for i in liste:
        print (i)


            
        