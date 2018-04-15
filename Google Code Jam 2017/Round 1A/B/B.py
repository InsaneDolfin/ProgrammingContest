# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:07:13 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round 1A\B')


#file = open("A-small.in",'r')
file = open("B-small-attempt2.in",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])


#print(lines)


#######################################################

def caseLines ():
    caseLines = []
    caseLines.append(1)
    for i in range (number_of_cases):
        #print(caseLines)
        caseLines.append(caseLines[-1] + int(lines[caseLines[-1]].split(' ')[0]) + 2)
    caseLines.pop()
    return caseLines
        
#print(caseLines())

def getInfo (case):
        
    Ligne = caseLines()[case-1]
    IngredientQuantity = {}
    Recipe = {}
    numberOfIngredients = int(lines[Ligne].split(' ')[0])
    numberOfPackage = int(lines[Ligne].split(' ')[1])
    for i in range (numberOfIngredients):
        
        Recipe[i] = int(lines[Ligne+1].split(' ')[i])
    for j in range (numberOfIngredients):
        IngredientQuantity [j] = []
        for i in range (numberOfPackage):
            IngredientQuantity [j].append(int(lines[Ligne+2+j].split(' ')[i]))
    
    return numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity
    

def answer(case):
    
    numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity = getInfo(case)
    #print(Recipe)
    #print(IngredientQuantity)
    Kompteur = 0
    
    for package in range (numberOfPackage): #je parcours l'ingrédient 0 seulement
    
            
        
        packageQuantity = IngredientQuantity[0][package]
        
        #print('>>>  ',packageQuantity)        
        
        #nbr de clients
        numberOfClient = [] 
        for number in range (15000) :
            
            if int(number*Recipe[0]*0.9) <= packageQuantity <= int(number*Recipe[0]*1.1) :
                
                numberOfClient.append(number)
        
        if numberOfClient == []:
            numberOfClient.append(0)
                
        #print(numberOfClient)
        
        if numberOfIngredients == 1:
            if numberOfClient[0] != 0:
                Kompteur += len(numberOfClient)
            
        
        #je parcours les autres ingrédients pour savoir si je trouve une association
        arreter = False
        for ingredients in range (1,numberOfIngredients):
            for pack in range (numberOfPackage):
                for clients in numberOfClient:
                    if clients*Recipe[ingredients]*0.9 <= IngredientQuantity[ingredients][pack] <= clients*Recipe[ingredients]*1.1:
                        #print(ingredients,pack)                   
                        Kompteur += 1
                        #del IngredientQuantity[0][package]
                        #del IngredientQuantity[ingredients][pack]
                        arreter = True
                        break
                if (arreter == True):
                    break
            if (arreter == True):
                break
        
    return Kompteur

#print(answer(6))




#######################################################

def main():
    for cases in range (1,number_of_cases+1):
        A = answer(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()  

            
file.close()
monfichier.close()
