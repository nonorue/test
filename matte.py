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
def x_nullpunkt(a, b):
    x = (-b/a)
    return x

def areal_av_trekant(g,h):
    return 0.5*g*h

a = float(input("Gi en stigningsverdi:"))
b = float(input("Gi en konstantverdi:"))

y_null = b
x_null = abs(x_nullpunkt(a, b))
areal = areal_av_trekant(y_null, x_null)

print("Null punkt til x blir:", x_null)
print("Arealet avgrenset av x-akse og y-akse når a er:", a, "og b er:", b, "blir:", areal)

