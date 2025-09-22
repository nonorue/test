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






#%% OPPGAVER: 5.12-16
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
# Denn formelen ser vi alltid vil danne en rettvinklet trekant
# Vi må ha skjæringspunktet som er når x=0 som blir y=a(0)+b som blir y=b
# Skjæringspunktet til x blir 0=ax+b som blir x= -(b/a)
# Deretter regner vi arealet av den rettvinklede trekanten = 0.5 * g * h som blir A = 0.5 * -(b/a)*b

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

#%%
# Oppgave 5.15
# y = f(x) = ax + b REGN UT OMKRETS AV FLATESTYKKET SOM ER AVGRENSET AV X OG Y
# Da har vi begge katetet så da bruker vi formel for hypotenus som er :

import numpy as np    

def beregn_hypotenus(katet1, katet2):
    hypotenus_squared = katet1**2 + katet2**2
    hypotenus = np.sqrt(hypotenus_squared)
    return hypotenus

def x_nullpunkt(a, b):
    x = (-b/a)
    return x

def areal_av_trekant(g,h):
    return 0.5*g*h

a = float(input("Gi en stigningsverdi:"))
b = float(input("Gi en konstantverdi:"))

y_null = b
x_null = abs(x_nullpunkt(a, b))
omkrets = beregn_hypotenus(y_null, x_null)+y_null+x_null
print(f'Omkrets til flatestykket som er avgrenset med x og y akse med gitte a og b verdier blir: {omkrets:.2f}')

#%% 
# Oppgave 5.16

import numpy
import rektangel_modul as rm

L = 3.0
B = 4.0

areal = rm.areal_rektangel(L, B)
omkrets = rm.omkrets_rektangel(L, B)
diagonal = rm.diagonal_rektangel(L, B)

print("Areal:", areal, "Omkrets:", omkrets, "Diagonal:", diagonal)










































