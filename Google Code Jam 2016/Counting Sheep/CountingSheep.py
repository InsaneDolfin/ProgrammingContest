# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 17:09:04 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2016\Counting Sheep')

file = open("A-large-practice.in",'r')

text = file.read()
monfichier = open("output_large.txt",'w')
lines = text.split('\n')
number_of_cases = int(lines[0])

print(lines)

def last_number_seen (N):
    digits_seen = []
    digitsInN = digits_in_N(N)
    for n in range(0,len(digitsInN)):
        if digitsInN[n] not in digits_seen:
            digits_seen.append(digitsInN[n])
    
    
       
    for i in range(2,2000): #timeout
        if len(digits_seen) == 10:
            occur = (i-1)*N
            return occur
            break
        else:
            occur = i*N
            newDigits = digits_in_N(occur)
            for n in range(0,len(newDigits)):
                if newDigits[n] not in digits_seen:
                    digits_seen.append(newDigits[n])
    
    return "INSOMNIA"
        
        
def list_N ():
    listN = []
    for i in range (1,number_of_cases+1):
        listN.append(int(lines[i]))
    return listN
    
def digits_in_N (N):
    digitsInN = []
    for i in str(N):
        digitsInN.append(int(i))
    return digitsInN
    

def main():
    cases = list_N()
    c = 1
    for n in cases:
        out = last_number_seen(n)
        print(out)
        monfichier.write('Case #'+str(c)+':'+' '+str(out)+'\n')
        c += 1
        
   
        
    monfichier.close()
    file.close()
       
        
        
#♠main()
    