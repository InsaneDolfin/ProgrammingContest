# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 23:59:01 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round 1B\A')


file = open("A-small-attempt1.in",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])

print (number_of_cases)
#######################################################

def caseLines ():
    caseLines = []
    caseLines.append(1)
    for i in range (number_of_cases):
        #print(caseLines)
        caseLines.append(caseLines[-1] + int(lines[caseLines[-1]].split(' ')[1]) + 1)
    caseLines.pop()
    return caseLines

def get_info(case):
    Ligne = caseLines()[case-1]
    D = int(lines[Ligne].split(' ')[0])
    nbH = int(lines[Ligne].split(' ')[1])
    horsesD = {}
    horsesS = {}
    for i in range (nbH):
        horsesD[i+1] = int(lines[Ligne+i+1].split(' ')[0])
        horsesS[i+1] = int(lines[Ligne+i+1].split(' ')[1])
    return D,nbH,horsesD,horsesS


def Time(case):
    D,nbH,horsesD,horsesS = get_info(case)
    #print (D,nbH,horsesD,horsesS)
    HorsesOrder = sorted(horsesD, key=horsesD.get)
    #print(HorsesOrder)
    if nbH == 2:
        TotalTime = (horsesD[HorsesOrder[1]] - horsesD[HorsesOrder[0]]) / horsesS[HorsesOrder[0]]    
        TotalTime += (D - horsesD[HorsesOrder[-1]] ) / min(horsesS[HorsesOrder[0]],horsesS[HorsesOrder[1]])
    else:
        TotalTime = horsesD[HorsesOrder[0]] / horsesS[HorsesOrder[0]]
    
    
    return TotalTime
    
    
def Speed(case):
    timeT = Time(case)
    D,nbH,horsesD,horsesS = get_info(case)
    Speed = D / timeT
    return '{:2f}'.format(Speed)
    


    
    











#######################################################

def main():
    for cases in range (1,number_of_cases+1):
        A = Speed(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()  

            
file.close()
monfichier.close()
