# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 00:07:32 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Round 1B\C')


file = open("test.txt",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])


#######################################################


    





#######################################################
"""
def main():
    for cases in range (1,number_of_cases+1):
        A = answer(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
main()  

            
file.close()
monfichier.close()
"""