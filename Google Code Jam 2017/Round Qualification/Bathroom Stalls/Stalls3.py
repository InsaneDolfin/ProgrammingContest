# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 02:43:04 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round Qualification\Bathroom Stalls')

file = open("C-small-2-attempt2.in",'r')
#file = open("test.txt",'r')
text = file.read()
monfichier = open("output_small2.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])

def get_info (caseNb):
    S = int(lines[caseNb].split(' ')[0])
    K = int(lines[caseNb].split(' ')[1])
    return S,K
    
def nombreBlank(S,K):
    blank = []
    
    blankNb = S-K
    espNb = K + 1
    blankPerSpace = (blankNb//espNb, blankNb%espNb)
        
    while blankPerSpace[1] != 0:
            
        blank.append(blankNb//espNb)
        blankNb -= blank[-1]
        espNb -= 1
        blankPerSpace = (blankNb//espNb, blankNb%espNb)
        
    while blankPerSpace[0] != 0 and espNb > 1:
        blank.append(blankNb//espNb)
        blankNb -= blank[-1]
        espNb -= 1
        blankPerSpace = (blankNb//espNb, blankNb%espNb)
        
    blank.append(blankNb)
    
        
        
    return blank

print(nombreBlank(20,4))
    
    