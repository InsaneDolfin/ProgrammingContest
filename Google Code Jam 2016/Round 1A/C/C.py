# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:27:40 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2016\Round 1A\C')

file = open("C-small-practice.in",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])

def myCase (case):
    ligneOfCase = 2*case-1
    numberStudent = int(lines[ligneOfCase])
    l = lines[ligneOfCase+1].split(' ')
    for i in range (len(l)):
        l[i] = int(l[i])
    return numberStudent,l
    
def calcul (case):
    numberStudent, affinity = myCase (case)
    pile = []
    pile.append (affinity[0])
    for i in range (1,numberStudent):
        if affinity[i] not in pile:
            pile.append(affinity[i])
    return pile
    
print(myCase(4))  
print(calcul(4)) 
    
    