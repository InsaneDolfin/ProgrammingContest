# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:06:57 2017

@author: Justin Guirautane
"""

import os, itertools

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Fractiles')

file = open("D-small-practice.in",'r')

text = file.read()
monfichier = open("output_small.txt",'w')
lines = text.split('\n')


number_cases = int(lines[0])

def info_case (case):
    numberOfTiles = int(lines[case].split(' ')[0])
    complexity = int(lines[case].split(' ')[1])
    numberOfClean = int(lines[case].split(' ')[2])
    numberTotalTiles = numberOfTiles**complexity
    return numberOfTiles, complexity, numberOfClean, numberTotalTiles
    
def possible_original_sequence (case):
    possibleSequences = []
    K, _, _, N = info_case (case)
    seq = []
    for i in range(K):
        seq.append
    possibleSequences = itertools.product(['L','G'],repeat = K)
    return list(possibleSequences)
        
    
    
c = info_case(4)
print(c)
comb = possible_original_sequence(1)
print(comb)
    