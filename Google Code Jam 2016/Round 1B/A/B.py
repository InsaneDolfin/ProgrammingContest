# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:41:07 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2016\Round 1B\A')

file = open("A-small-practice.in",'r')
text = file.read()
monfichier = open("output_small.txt",'w')

lines = text.split('\n')

number_of_cases = int(lines[0])

def getCase(case):
    return lines[case]
    
def numbers(case):
    s = getCase(case)
    l = list(s)
    ans = []
    while l != []:
        for let in l:
            print(let)
            if let == 'Z':
                l.remove('Z')
                l.remove('E')
                l.remove('R')
                l.remove('O')
                ans.append('0')
            elif let == 'W':
                l.remove('T')
                l.remove('W')
                l.remove('O')
                ans.append('2')
            elif let == 'X':
                l.remove('S')
                l.remove('I')
                l.remove('X')
                ans.append('6')
            
            elif let == 'S' and 'V' in l and 'N' in l:
               l.remove('S')
               l.remove('E')
               l.remove('V')
               l.remove('E')
               l.remove('N')
               ans.append('7')
            elif let == 'F' and 'V' in l:
                l.remove('F')
                l.remove('I')
                l.remove('V')
                l.remove('E')
                ans.append('5')
            elif let == 'T' and 'H' in l:
                l.remove('T')
                l.remove('H')
                l.remove('R')
                l.remove('E')
                l.remove('E')
                ans.append('3')
            elif let == 'F' and 'R' in l:
                l.remove('F')
                l.remove('O')
                l.remove('U')
                l.remove('R')
                ans.append('4')
            elif let == 'O' and 'N' in l:
                l.remove('O')
                l.remove('N')
                l.remove('E')
                ans.append('1')
            elif let == 'G' and 'H' in l:
                l.remove('E')
                l.remove('I')
                l.remove('G')
                l.remove('H')
                l.remove('T')
                ans.append('8')
            elif let == 'N' and 'I' in l:
                l.remove('N')
                l.remove('I')
                l.remove('N')
                l.remove('E')
                ans.append('9')
            print(ans)
            print(l)
        
    #print(l)
    return ''.join(sorted(ans))
print(getCase(6))
print(numbers(6))

def main():
    for cases in range (1,number_of_cases+1):
        A = numbers(cases)
        print('Case #'+str(cases)+' : '+str(A))
        monfichier.write("Case #"+str(cases)+':'+' '+str(A)+"\n")              

  
#main()              
file.close()
monfichier.close()            
        