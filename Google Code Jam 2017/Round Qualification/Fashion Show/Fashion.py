# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:40:05 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round Qualification\Fashion Show')

file = open("FashionShowTest.txt",'r')
text = file.read()
monfichier = open("output_small2.txt",'w')

lines = text.split('\n')

numberOfCases = int(lines[0])

def indiceOfNewCase ():
    casesList = []
    casesList.append(1)
    for i in range (2, numberOfCases+1):
        newCase = casesList[-1] + int(lines[casesList[-1]].split(' ')[1]) + 1
        casesList.append(newCase)
    return casesList
    
def drawTheCase (caseIndice):
    N = int(lines[caseIndice].split(' ')[0])
    M = int(lines[caseIndice].split(' ')[0])
    grid = []
    for i in range (N):
        grid.append(['.']*N)
    for j in range (M+1):
        tip = lines[caseIndice+1+j].split(' ')[0]
        x = int(lines[caseIndice+1+j].split(' ')[1]) - 1
        y = int(lines[caseIndice+1+j].split(' ')[2]) - 1
        grid[x][y] = tip    
    return grid


        
            


    
g = drawTheCase(4)
print(g[0])