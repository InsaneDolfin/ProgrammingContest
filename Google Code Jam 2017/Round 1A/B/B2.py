# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:07:13 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round 1A\B')


#file = open("A-small.in",'r')
file = open("B-small-practice.in",'r')
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
    



def ingredientPackQuantity(case):
    numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity = getInfo(case)
    
    ingPackQuantity = {}
    
    for ingredient in range(numberOfIngredients):
        ingPackQuantity[ingredient] = {}
        for package in range (numberOfPackage):
            ingPackQuantity[ingredient][package] = IngredientQuantity[ingredient][package]
            
    return ingPackQuantity

#print(ingredientPackQuantity(3))

def numberClientPackage(case):
    numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity = getInfo(case)
    ingPackQuantity = ingredientPackQuantity(case)
    ingPackClients = {}
    
    for ingredient in range(numberOfIngredients):
        ingPackClients[ingredient] = {}
        for package in range(numberOfPackage):
            ingPackClients[ingredient][package] = []
            
            for nb in range (15000):
                if 0.9*Recipe[ingredient]*nb <= ingPackQuantity[ingredient][package] <= 1.1*Recipe[ingredient]*nb:
                    ingPackClients[ingredient][package].append(nb)
                    
    return ingPackClients
    
#print(numberClientPackage(3))
        

def ingredientList(case):
    numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity = getInfo(case)
    ingPackClients = numberClientPackage(case)
    
    ingredientList = {}
    for ing in range (numberOfIngredients):
        ingredientList[ing] = []
        for package in range (numberOfPackage):
            for i in range (len(ingPackClients[ing][package])):
                if ingPackClients[ing][package][i] not in ingredientList[ing]:
                    ingredientList[ing].append(ingPackClients[ing][package][i])
        ingredientList[ing] = sorted(ingredientList[ing])
    return ingredientList
    

    
def answer(case):
    numberOfIngredients, numberOfPackage, Recipe, IngredientQuantity = getInfo(case)
    ingList = ingredientList(case)
    Kompteur = 0
    
    if numberOfIngredients == 1:
        a = numberClientPackage(case)
        for pac in range(numberOfPackage):
            if a[0][pac] != []:
                Kompteur += 1
        
        return Kompteur
                
    
    for client in ingList[0]:
        #print('>>> ',client)
        c = 1
        for other in range(1,numberOfIngredients):
            #print(other)
            if other == 0:
                break
            else:
                #print(ingList[other])
                
                for i in range (len(ingList[other])):
                    if ingList[other][i] == client:
                        #print('client in it')
                        c += 1
        if c == len(ingList):
            Kompteur += 1
            ingList[0].remove(client)
        #print(ingList[0])
            
    
    return Kompteur
    
#print(numberClientPackage(5))
#print(ingredientList(5))    
#print(answer(1))
                
    
    
    
    
    


    




#######################################################

def main():
    for cases in range (1,number_of_cases+1):
        A = answer(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()  

            
file.close()
monfichier.close()
