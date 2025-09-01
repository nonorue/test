# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 14:36:05 2025

@author: nicol
"""

#%%
#oppgave 5.1

# Tallverdien som blir skrevet til skjerm er A, og denne funksjonen ser ut til å beregne arealet til en trekant.

def hemmelig(g,h):
    A = g*h/2
    return A

print(hemmelig(4.5, 4))

#%%
#oppgave 5.2
#For å gjøre funksjonen om til beregning av A til rektangel gjør vi følgene:
    
def A_rek(l,b):
    A = l*b
    return A

print(A_rek(5,5),"m**2")

#%%
#oppgave 5.3 Valuta kalkulator

def val_calc(eur):
    nok = eur*10.42
    usd = eur*1.19
    return nok, usd

eur_in = float(input("Skriv inn mengde Euro:"))
svar = val_calc(eur_in)
print("Ved", int(eur_in), "Euro får vi", f'{svar[0]:.2f}', "Norske kroner.")
print("Ved", int(eur_in), "Euro får vi", f'{svar[1]:.2f}', "Amerikanse dollar.")

#%%
#oppgave 5.4 
#Lag funksjon som regner stor katet
# Formel er storKatet = numpy.sqrt(hypot**2 - litenKatet**2)

import numpy as np

def beregn_katet(k_1, hyp):
    k_2 = np.sqrt(hyp**2 - k_1**2)
    return k_2

liten_katet =  float(input("Skirv inn lengde [m] på liten katet:"))
hypotenus = float(input("Skriv inn lengde [m] på hypotenus:"))

stor_katet = beregn_katet(liten_katet,hypotenus)

print("Stor katet er:",f'{stor_katet:.2f}', "meter")   

#%%
#oppgave 5.5
# Studer program uten å kjøre, vil det funkere? I så fall hva vil skrives til skjerm?

x = 10

def myfun():
    print(x)
    
myfun()

# Nei det vil ikke fungere siden myfun() ikke er gitt verdi i def så funksjonen vet ikke hva x er. JODA
# Programmet kjørte og hentet x variablen selv!!!! så () kan stå tom hvis det gir mening for funksjon

#%%
#oppgave 5.6

x = 10 

def myfun(): 
    x = x + 1
    print(x)

myfun()

# Her vil antaglig vis 11 bli skrevet til skjermen? NEI her kommer vi innpå det jeg trodde forrige gang.
# Hvis vi skal få ut 11 må x inn i begge myfun() funksjonene.

#%%
#oppgave 5.7
#oppgaven ber om m = 80 og v = 12
masse = float(input("Skriv in verdien for masse [kg]:"))
fart = float(input("Skriv inn verdien for fart [m/s]:"))

def kin_erg(m,v):
    energi = 0.5*m*v**2 
    return energi

kinetisk_energi = kin_erg(masse, fart)

print("Kinetiske energien er:", kinetisk_energi, "Joule")

#%% 
#Oppgave 5.8
# Finn høyde når Ep = m*g*h og Ep=34.37 g=9.81 og m=0.48
# h = Ep/m*g

def regn_høyde(Ep,m,g):
    høyde = Ep/(m*g)
    return høyde

masse = 0.48
aks = 9.81
pot_energi = 34.37

resultat = regn_høyde(pot_energi, masse, aks)

print("Høyden med verdiene gitt i oppgave er:", f'{resultat:.2f}', "meter")

#%% 
#Oppgave 5.9
# Gi g standardverdien på 9.81 og så gi g en verdi på 1.6 i variablen, så test.
# h = Ep/m*g



def regn_høyde(Ep,m,g=9.81):
    høyde = Ep/(m*g)
    return høyde

masse = 0.48
aks = 1.6
pot_energi = 34.37

resultat = regn_høyde(pot_energi, masse, aks)

print("Høyden med verdiene gitt i oppgave er:", f'{resultat:.2f}', "meter")
