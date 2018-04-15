# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:28:50 2017

@author: Justin Guirautane
"""

import os

os.chdir('D:\P a r a C o d e\Google Code Jam 2017\Counting Sheep')

taille_pile = 10
exemple = '++-++--+-+'
exemple2 = '++++'

def main():
    pile = list(exemple)
    #scan if all + or all -
    if exemple == taille_pile*'-' or exemple == taille_pile*'+':
        return 1
    else:
        return 0





print(main())
