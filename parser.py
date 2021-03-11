# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:00:50 2021

@author: joshs
"""


file = r"C:\Users\joshs\OneDrive\Documents\bin.txt"  

CAPTIVATION=['C','A','P','T','I','V','A','T','I','O','N']


def filler(bList,bit):
    bit=str(bit,'utf-8')
    bList.append(bit)
    return bList

def checkFail(bList, bit):
    bit=str(bit,'utf-8')
    bList.pop(0)
    bList.append(bit)
    return bList

#binary to letter takes the binary in our queue
#and joins them into a string
def binToL(bList):
    bini=""
    bini +=''.join(bList)
    return bini
         
#convert string from binary to letter into
#an ASCii Symbol 
def converter(bList):
     bini = binToL(bList)
     x=chr(int(bini,2))
     return x
 
#check if letter is the one we need next
#by converting the queue to an ascii letter
def checkL(bList,cap):
    if(len(bList)>7):
        L=converter(bList)
        if L == CAPTIVATION[cap]:
            return L

def letterPush(bList):
    return converter(bList)
    

# initialize our containers and counters
bytes = [] #window (the container we are looking at as we go along)
letters = []
current=0
cap = 0
chunk=[]
letterP = []
counter = 0

def main(bytes,letters,current,cap):
    with open(file, "rb") as f:
        #print(cap)
        #while loop to go over every bit in the file one at a time
        while (byte := f.read(1)):                    
            #while loop to fill the window if it's not full
            while(len(bytes)<=7):
                #baseCase fills the queue with the next bit
                filler(bytes,byte)
                #here we move the pointer up by 1
                byte=f.read(1)
                #set the current pointer to the next bit in line after filled
                current = f.tell()
                
            # check the letter for the needed next Letter
            if(checkL(bytes,cap)):
                #if true, append to letters list
                letters.append(checkL(bytes,cap))
                #increase the array pointer for next needed letter
                cap +=1 
                #clear window for next 8 bits
                bytes.clear()                
                current= f.tell()
                #go to the next bit 
                f.seek(current-1,0)
                
                #if the next symbol is not needed
            else:
                #clear letters list
                letters.clear()
                #move window up by 1 (pop first bit in window, push next bit in)
                checkFail(bytes,byte)
                #reset letter needed to C
                cap = 0
            #when conditions are met
            if(letters == CAPTIVATION):
                #set our current bit for reference
                current = f.tell()
                #clear our letters array
                letters.clear()
                #clear our window
                bytes.clear()
                #start needed symbols array
                cap = 0
                #initialize our counter to 0
                counter = 0
                #go to the bit following the last letter of needed symbols
                f.seek(current+1,0)
                #until we get the next 800 bits
                while (counter < 800):
                    # if our chunk window is not at 8 bits
                    while(len(chunk) <=7 ):
                        #fill the window
                        filler(chunk, byte)
                        #set byte to the next pointer place in file
                        byte=f.read(1)
                        #increase counter by 1
                        counter += 1
                        
                    #convert our bit to ascii symbol
                    l = converter(chunk)
                    
                    #print to stdout
                    print(l)
                    #clear window to get next 8 bits
                    chunk.clear()
        #once we get the next 800 symbols, we start where we left off after 
        #our condition was met        
        f.seek(current-1,0)
               
           


main(bytes,letters,current,cap)
