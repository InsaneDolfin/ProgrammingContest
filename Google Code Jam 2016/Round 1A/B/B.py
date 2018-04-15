# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:19:22 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2016\Round 1A\B')

file = open("B-large-practice.in",'r')
text = file.read()
monfichier = open("output_large.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])
casesLine = {}
c = 1
l = 1
while l != len(lines)-1:
    casesLine[c] = l
    l += int(lines[l])*2
    c += 1


def intToString(liste):
    for i in range (len(liste)):
        liste[i] = str(liste[i])
    return liste
    


def answer (case):
    
    aaa = []
    nombre= []
    ligneDepart = casesLine[case]
    nombreD = int(lines[ligneDepart])

    for line in range (ligneDepart+1,ligneDepart+nombreD*2):
        l = lines[line].split(' ')
        for i in range (len(l)):
            aaa.append(int(l[i]))
            #print(aaa)
    
    #print (aaa)
          
    for nb in aaa:
        c = 0
        for i in range (len(aaa)):
            if aaa[i] == nb:
                c+=1
        if c%2 != 0:
            if nb not in nombre:
                nombre.append(nb)
    #print (nombre)
    return ' '.join(intToString(sorted(nombre)))
    
#print(answer(50))
        

def main():
    for cases in range (1,number_of_cases+1):
        A = answer(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()              
file.close()
monfichier.close()

        
    



        

