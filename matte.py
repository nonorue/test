# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 10:54:37 2025

@author: nicol
"""
#%%
import numpy as np

def andregrad(a, b, c):
    x1 = ((b*-1) + np.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = ((b*-1) - np.sqrt(b**2-(4*a*c)))/(2*a)
    return x1, x2

tall1 = float(input("Skriv inn a verdi:"))
tall2 = float(input("Skriv inn b verdi:"))
tall3 = float(input("Skriv inn c verdi:"))

resultat = andregrad(tall1, tall2, tall3)

print(resultat)

#%%

