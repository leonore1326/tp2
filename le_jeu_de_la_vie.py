#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:21:20 2020

@author: leonore
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
from copy import deepcopy

def matrice_initiale():    
    situation_initiale=open("/Users/leonore/Desktop/Programmation/input.txt","r")
    chaine_initiale=situation_initiale.read()
    situation_initiale.close()
    liste_initiale=chaine_initiale.split('\n')
    matrice_initiale=[]
    for k in range (len(liste_initiale)-1):
        matrice_initiale.append([])
        for j in range (len(liste_initiale[k])):
            matrice_initiale[k].append(int(liste_initiale[k][j]))
    #for i in range(len(matrice_initiale)):
        #print(matrice_initiale[i],'\n')
    return(matrice_initiale)

def voisines(abscisse,ordonnee,matrice):
    somme=matrice[abscisse-1][ordonnee+1]+matrice[abscisse][ordonnee+1]+matrice[abscisse+1][ordonnee+1]
    somme+=matrice[abscisse-1][ordonnee-1]+matrice[abscisse][ordonnee-1]+matrice[abscisse+1][ordonnee-1]
    somme+=matrice[abscisse-1][ordonnee]+matrice[abscisse+1][ordonnee]
    return(somme)
    

def evolution(matrice):
    copie=deepcopy(matrice)
    for ordonnee in range(1,len(matrice)-1):
        for abscisse in range (1,len(matrice[ordonnee])-1):
            eval=voisines(abscisse,ordonnee,matrice)
            if copie[abscisse][ordonnee]==1:
                if not(eval==2 or eval==3):
                    copie[abscisse][ordonnee]=0
            if copie[abscisse][ordonnee]==0:
                if eval==3:
                    copie[abscisse][ordonnee]=1
    matrice=copie
    return(matrice)

def updater (temps, img, M): #pour l'interface graphique on crée une fonction qui fait évoluer la matrice 
    for i in range(temps): #et qui met à jour l'image correspondante
        M=evolution(M)
        img.set_data(M)
    return img        

### MAIN
    
jeu_de_la_vie=matrice_initiale()
temps=int(input("combien de temps la grille evolue-t-elle?"))
fig,ax = plt.subplots() # Create a figure
img = ax.imshow(jeu_de_la_vie, cmap=cm.RdYlGn) 
#for k in range(temps):
ani=animation.FuncAnimation(fig, updater, fargs=(img, jeu_de_la_vie), frames=temps, repeat=False, interval=200)
plt.show()









