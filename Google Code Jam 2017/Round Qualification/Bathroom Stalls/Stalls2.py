# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:48:57 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round Qualification\Bathroom Stalls')

file = open("C-small-1-attempt0.in",'r')
#file = open("test.txt",'r')
text = file.read()
monfichier = open("output_small2.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])




def get_info (caseNb):
    S = int(lines[caseNb].split(' ')[0])
    K = int(lines[caseNb].split(' ')[1])
    
    print(S,K)
    return S, K

def newOccupied (occupied, indice):
    occupied.append(indice)
    occupied.sort()
    return occupied
    
def init(caseNb):
    occupied = []
    S, K = get_info(caseNb)
    occupied = newOccupied(occupied, 0)
    occupied = newOccupied(occupied, S+1)
    return S,K,occupied

   
def newPeople(occupied):
    maxDistance = 0
    maxInd = (0,0)
    for people in range (1,len(occupied)):
        distance = occupied[people] - occupied[people - 1] -1
        if distance > maxDistance:
            maxDistance = distance
            maxInd = (occupied[people-1], occupied[people])
    
    indiceToOccupate = (maxInd[1]-maxInd[0])//2 + maxInd[0]
    occupied = newOccupied(occupied, indiceToOccupate)
       
    return occupied, indiceToOccupate




def calculLastPerson(occupied, indiceOccupied):
    
    for i in range (len(occupied)):
        if occupied[i] == indiceOccupied:
            I = i
          
    Ls = occupied[I] - occupied[I-1] - 1
    Rs = occupied[I+1] - occupied[I] -1
    
    MAX = max(Ls,Rs)
    MIN = min(Ls,Rs)
    
    return MAX,MIN
            
def main():
    for cases in range (1,number_of_cases+1):
        
        s,k,o = init(cases)
        for i in range (k-1):
            o, _ = newPeople(o)
        o, ind = newPeople(o)
        MAX, MIN = calculLastPerson(o,ind)
        print(cases,'    ###    ',MAX,MIN)
        
        
        
        
        monfichier.write("Case #"+str(cases)+':'+' '+str(MAX)+' '+str(MIN)+"\n")
        
main() 


file.close()
monfichier.close()


