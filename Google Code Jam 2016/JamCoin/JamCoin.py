# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:08:41 2017

@author: Justin Guirautane
"""

import os, itertools

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\JamCoin')

file = open("C-small-practice.in",'r')

text = file.read()
monfichier = open("output_small.txt",'w')
lines = text.split('\n')

len_to_do = int(lines[1].split(' ')[0])
nb_to_do = int(lines[1].split(' ')[1])


def convert_10 (N):
    baseDix = 0
    chiffre = list(N)
    n = len(chiffre)-1
    for i in range (0,len(chiffre)):
        baseDix += int(chiffre[i])*(2**(n))
        n -= 1
    return baseDix
    
def convert_10_to_x (x,N):
    baseX = []
    while N >= x:
        baseX.append(str(int(N%x)))
        N = int(N/x)
    baseX.append(str(N))
    baseX.reverse()
    result = ''.join(baseX)           
    return result
    
def generate_bits():
    potential_JamCoins = []
    l = ["".join(seq) for seq in itertools.product("01", repeat=len_to_do)]    
    for i in l:
        if list(i)[0] == '1' and list(i)[-1] == '1':
            potential_JamCoins.append(i)
    return potential_JamCoins    
    

    
def test_seq(N):
    baseDix= convert_10(N)
    if baseDix == 2 or baseDix == 5:
        return True
    else:
        for i in range (2, baseDix):
            if baseDix%i == 0:
                return False, i
        return True,i
    
            
def main():
    jamcoins = {}
    potentials = generate_bits()
    
    for sequence in potentials:
        if len(jamcoins) < 50:
            if test_seq(sequence)[0] == False:
                jamcoins[sequence] = []
                jamcoins[sequence].append(str(test_seq(sequence)[1]))
                
                for base in range (2,10):
                    jamcoins[sequence].append( convert_10_to_x (base,test_seq(sequence)[1]) )
        else:
            break
    return jamcoins

        
coins = main()
print(coins)

monfichier.write('Case #1:\n')
for jams in coins:
    monfichier.write(jams+' ' + ' '.join(coins[jams]))
    monfichier.write('\n')
    
  
        

    
    
    
monfichier.close()
file.close()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    