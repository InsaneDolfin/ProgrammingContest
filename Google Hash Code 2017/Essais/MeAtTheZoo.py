# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 19:34:48 2017

@author: Justin Guirautane
"""

import os, operator
os.chdir("D:\Google Hash Code 2017")


vidSize = {}
vidRequest = {}
cacheSizeRemaining = {}
lines = {}
end = {}
latence = {}
endpointcache= {}



file = open("me_at_the_zoo.in",'r')

text = file.read()
print(text)

ligne = text.split("\n")
nbLigne = len(ligne)


#encodage des lignes en liste
for i in range(0,nbLigne):
    lines[i] = ligne[i].split(" ")

 
nbVids = int(lines[0][0])
nbCache = int(lines[0][3])
cacheSize = int(lines[0][4])
nbRequest = int(lines[0][2])
nbEndpoint = int(lines[0][1])


#DICO VIDEO - TAILLE
sizeOfVideos = ligne[1].split(" ")
for i in range (0, nbVids):
    vidSize[i] = int(sizeOfVideos[i])
    
#DICO cache - taille restante
for i in range (0, nbCache):
    cacheSizeRemaining[i] = cacheSize

#Lignes Request
lignesRequest = []
for i in range (2,nbLigne):
    if len(lines[i]) == 3:
        lignesRequest.append(i)

#DICO video ID - request
for i in range (0,len(lignesRequest)):
    if int(lines[lignesRequest[i]][0]) in vidRequest:
        vidRequest[int(lines[lignesRequest[i]][0])] = vidRequest[int(lines[lignesRequest[i]][0])] + int(lines[lignesRequest[i]][2])
    else:
         vidRequest[int(lines[lignesRequest[i]][0])] = int(lines[lignesRequest[i]][2])
         
# TRI de vidRequest
vidRequest = sorted(vidRequest, key = vidRequest.get)

#association aux caches
#cache = 0
#li = []
#for video in vidRequest:
#    if vidSize[video] < cacheSizeRemaining[cache]:
#        li.append(video)       
#        cacheSizeRemaining[cache] = cacheSizeRemaining[cache] - vidSize[video]
#    else:
#        end[cache] = li
#        li = []
#        if cache <11 :
#            cache += 1
#        else:
#            break
#
#print(end)
#print("   ")
#print(vidRequest)


c = 1
l = 2
while l < 42 : 
    for endpoints in range (0, int(nbEndpoint)):
        latence[endpoints] = int(lines[l][0])
        for i in range (0, int(lines[l][1])):            
            endpointcache[endpoints][int(lines[l+c][0])] = int(lines[l+c][1])
            c += 1
        l += int(lines[l][1]) + 1
       
print(latence)      

latenceSorted = sorted (latence, reverse = True, key = latence.get)   

print((lines[2+1]))
    
    
    









file.close()