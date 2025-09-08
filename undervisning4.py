# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 12:10:18 2025

@author: nicol
"""

innverdi = float(input("Skriv inn tall her:"))

mvaverdi = 25

def moms(beløp, mva):
    return beløp * mva / 100
    

moms = moms(innverdi, mvaverdi)

print("Momsen til gitt verdi:", innverdi, "kr", "Så er momsen:", moms, "kr")
print("Total pris med moms er:", innverdi+moms, "kr")

#%%



def moms(beløp, mva = 25):
    return beløp * mva / 100


innverdi = float(input("Skriv inn tall her:"))  

mvaverdi = 15 # Nå brukes 15

moms = moms(innverdi, mvaverdi) # Når mva verdi ikke er sendt inn vil mva = 25 i def bli brukt

print("Momsen til gitt verdi:", innverdi, "kr", "Så er momsen:", moms, "kr")
print("Total pris med moms er:", innverdi+moms, "kr")

#%%

import numpy as np

a = np.linspace(0, 10)
b = np.linspace(1, 12, 10) # Endrer Size
c = np.linspace(0, 10, 4, False) # Sluttpunktet er ikke med

print(np.mean(a))

min_arr = np.array([[1,200,3,4], [5,6,7,8]])
svar = np.mean(min_arr)
print(svar)

#%%

navn = "Ola" #Global variabel

def si_navn():
    navn = "Geir" #Lokal variabel med samme navn
    print("Inne i funksjon:", navn)

print("Untenfor funksjonen:", navn)
si_navn() # Vil ikke overstride globale variablet
print("Untenfor funksjonen:", navn) #Derfor er det god programmering vaner og ha andre navn inne i funksjoner

#%%

skatt_prosent = .30
tillegg_prosent = .15

def beregn_netto_lønn(brutto_lønn, skatt, tillegg):
    lønn_med_tillegg = brutto_lønn + brutto_lønn*tillegg
    tot_skatt = lønn_med_tillegg * skatt
    netto_lønn = lønn_med_tillegg - tot_skatt
    return netto_lønn

brutto_lønnen = 40000
netto_lønnen = beregn_netto_lønn(brutto_lønnen, skatt_prosent, tillegg_prosent)

print("Lønn utbetalt lønn totalt med tillegg blir:", netto_lønnen, "kr")

#%%
# MODULER VI KOMMER TIL Å BRUKE MYE
# numpy
# matplotlib.pyplot Visualisering av foreksempel grafer
# pandas Excel filer

def stigende_rekke(a, b, c):
    svar = a <= b <= c
    return svar









































