# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 17:16:31 2025

@author: nicol
"""

#%%
# Oppgave 5.12

import numpy as np

def arrlenmax(a):
    arrlen = len(a)
    arrmax = np.argmax(a)
    return arrlen, arrmax

myarr = np.array([1.2, 5.9, -3.1, 7.9, 0.6])
myarrlenmax = arrlenmax(myarr)
myarrlen = myarrlenmax[0]
myarrmax = myarrlenmax[1]

print("Lengden til arrayet er:", myarrlen)
print("Største verdien har index på:", myarrmax, "og verdi på:", myarr[myarrmax])

#%%
# Oppgave 5.13
import numpy as np
# Lag funksjon som regner gjennomsnittlige farten
# Etter listen så ser vi at det har gått 10 sekunder så det tar vi med i regnestykket
def gjenfart(s, t):
    gjenfart = sum(s)
    v = gjenfart/t
    return v

S = np.array([1.05, 1.30, 1.10, 0.94, 1.21])
T = len(S)*2
print("Gjennomsnittsfarten er:", gjenfart(S, T), "m i sekundet.")
#ved konstat fart gjelder formel v = s/t

#%%
# Oppgave 5.14
# y = f(x) = ax + b
# Lag en funksjon som regner arealet som er avgrenset av x aksen y aksen og linja y = ax + b

def beregn_areal(x, stig, kons):
    y = stig * x + kons
    a = (x * y) / 2
    return a

x_verdi = int(input("Skriv inn  x verdi:"))
stigning = int(input("Skriv inn  stigningstall verdi:"))
konstant = int(input("Skriv inn  konstantverdi verdi:"))

areal = beregn_areal(x_verdi, stigning, konstant)

print("Arealet avgrenset mellom x-aksen, y-aksen og linjen med verdier oppgitt er:", areal,"m^2")


    