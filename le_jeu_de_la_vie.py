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
import numpy as np
from random import random

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

def matrice0_aleatoire(n,pourcentage_de_cellules_vivantes):
    mat=np.zeros((n,n))
    for k in range (n):
        for j in range(n):
            cellule=random()
            if cellule>(1-(pourcentage_de_cellules_vivantes/100)):
                cellule=1
                mat[k][j]=1
    return(mat)
        
    
    
    

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


jeu_de_la_vie=matrice0_aleatoire(30, 15)

def updater (temps, img): #pour l'interface graphique on crée une fonction qui fait évoluer la matrice 
    global jeu_de_la_vie
    #for i in range(temps): #et qui met à jour l'image correspondante
    jeu_de_la_vie=evolution(jeu_de_la_vie)
    img.set_data(jeu_de_la_vie)
    return (img)        

### MAIN
    
temps=int(input("combien de temps la grille evolue-t-elle?"))
fig,ax=plt.subplots() # Create a figure
img=ax.imshow(jeu_de_la_vie, cmap=cm.RdYlGn) 
#for k in range(temps):
ani=animation.FuncAnimation(fig, updater, fargs=(img,), frames=temps, repeat=False, interval=20)
plt.show()

















