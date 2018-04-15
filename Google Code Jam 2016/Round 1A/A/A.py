# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 17:00:06 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2016\Round 1A\A')

file = open("A-large-practice.in",'r')
text = file.read()
monfichier = open("output_large.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])



def answer(case):
    
    source = list(lines[case])
    
    answer = []
    
    answer.append(source[0])
    for letter in range (1,len(source)):
        
        if source[letter] >= answer[0]:
            answer.insert(0,source[letter])
        else:
            answer.append(source[letter])
        
    return ''.join(answer)

def main():
    for cases in range (1,number_of_cases+1):
        A = answer(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()              
file.close()
monfichier.close()