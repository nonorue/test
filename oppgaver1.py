# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 14:15:26 2025

@author: nicol
"""
#%%
#oppgave 3.1
beløp = 10000
beløp = beløp*(1+1.85/100)**5
print("Etter fem år er nyet beløpet:", f'{beløp:.2f}',"kr")
#%%
#oppgave 3.2

import numpy as np
number = 8.02
rundNed = np.floor(number)
rundOpp = np.ceil(number)
print(rundNed, rundOpp)
#eller
print(np.floor(number), np.ceil(number))
#Her ser vi at floor og ceil funksjonene begge runder opp men da floor runder ned til nærmeste hele tall og ceil runder opp til nærmeste hele tall

#%%
#oppgave 3.3
#svaret skal bli gitt med en Euklidsk formel for avstand, den er = kvadratrot av (xA-xB)**2+(yA-yB)**2
A = (2.3, 8.1)
xA = 2.3
yA = 8.1
B = (7.4, -13.5)
xB = 7.4
yB = -13.5

import numpy as np

avstand = np.sqrt(((xA-xB)**2)+((yA-yB)**2))
#avstand = np.sqrt(((2.3-7.4)**2)+((8.1-(-13.5))**2))
avstand = float(avstand)
print("Avstand mellom A og B er:", f'{avstand:.3e}')


#%%
#oppgave 3.4

xA = float(input("Kordinat for xA:"))
yA = float(input("Kordinat for yA:"))

xB = float(input("Kordinat for xB:"))
yB = float(input("Kordinat for yB:"))

import numpy as np

avstand = np.sqrt(((xA-xB)**2)+((yA-yB)**2))
#avstand = np.sqrt(((2.3-7.4)**2)+((8.1-(-13.5))**2))

print("Avstand mellom A og B er:", f'{avstand:.3e}')
#%%
#oppgave 3.5
#formel for overflate er = 4pir**2
r = float(input("Skriv inn radius for kule:"))
import math as m
p = m.pi
overflate = float(4*p*(r**2))
#formel til volum er = V = 4pir**3/3
volum = float(4*p*(r**3)/3)
print("Overflate:", f'{overflate:.2f}', "Volum:", f'{volum:.2f}')


#%%
#oppgave 3.6

litenKatet = float(input("Skriv inn lengde [m] på liten katet:"))
hypot = float(input("Skriv inn lengde på [m] hypotenus:"))
# k**2 + k**2 = h**2 så k**2 = h**2 - k**2
# k = kvadratroden av k**2
import numpy as nu
storKatet = nu.sqrt((hypot**2) - (litenKatet**2))
print("Lengde [m] på siste katet er:", f'{storKatet:.1f}')
#omkrets =  h + k1 + k2 areal = g * h /2
omkrets = hypot + litenKatet + storKatet
areal = (litenKatet*storKatet)/2
print("Trekanten har en omkrets [m] på:", f'{omkrets:.1f}', "og ett Areal [m^2] på:", f'{areal:.1f}')
#%%
#oppgave 3.7

litenKatet = float(input("Skriv inn lengde [m] på liten katet:"))
hypot = float(input("Skriv inn lengde på [m] hypotenus:"))
# k**2 + k**2 = h**2 så k**2 = h**2 - k**2
# k = kvadratroden av k**2
import numpy as nu
storKatet = nu.sqrt((hypot**2) - (litenKatet**2))
print("Lengde [m] på siste katet er:", f'{storKatet:.1f}')
#omkrets =  h + k1 + k2 areal = g * h /2
omkrets = hypot + litenKatet + storKatet
areal = (litenKatet*storKatet)/2
print("Trekanten har en omkrets [m] på:", f'{omkrets:.1f}', "og ett Areal [m^2] på:", f'{areal:.1f}')
#cos sin tan
#%%
import numpy as nu
import math as ma
a = 8
b = 5
c = 6.2
abc = nu.array(8,5,6.2)
sin = nu.degrees(abc)0
print(sin)
#%%
#oppgave 3.8
#%% 
#oppgave 3.9
#%%
#oppgave 3.14


#%%
#oppgave 1
energi = 552
tot_energi = energi*2
energi_rute = tot_energi/24
ant_biter = int(input("Skriv inn antall ruter du har spist:"))
total_kcal = ant_biter*energi_rute
print("Du har fått i deg", total_kcal, "kcal")
#hva er int()?


#%%
#oppgave 2
o = 400
l = 5000
ant_runder = l/o
print(ant_runder)
resultat = divmod(l, o)
print("antall runder", resultat[0], "gjenverende meter", resultat[1])

#%%
#oppgave 3

liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(liste1[1:5]) #Her starter listen fra index 1 til og med 4 slutter på index 5
print(liste1[4::]) #Her starter listen fra index 4 til og med 8, altså hele listen
print(liste1[::3]) #Her starter listen på index 0 så hopper tre steg til index 3 så hopper enda tre steg til index 6

#%%
#oppgave 8

bruker_liste = list(input("skriv inn et 3-sifferet  tall: ")) 

tall1 = bruker_liste[0]
tall2 = bruker_liste[1]
tall3 = bruker_liste[2]
#jeg må bli bedre til å ikke hoppe rett til print men å lage verdier som jeg bruker i print.
resultat = (tall1<tall2<tall3)
print("Tall er i stigende rekkefølge:", resultat)
#nedenfor ikke nødvendig kun fancy test, garantert en lettere måte å gjøre på

if(tall1<tall2<tall3):print("Disse tallene er stigende")
else:print("Disse tallene er ikke stigende")


#%%
#oppgave 9 og 10
import string as st 
# Leser inn alfabetet 
alfabet = list(st.ascii_lowercase)
alfabetn = ["æ","ø","å"]
alfabet.extend(alfabetn) #ved å bruke .extend isteden for .append så legger vi til alle i listen med sitt egen index nummer
 #kunne også ifølge svar eks bruke alfabet = alfabet + ["æ", "ø", "å"]  
 
bokstav = input("Skriv inn en bokstav:")
plass = alfabet.index(bokstav) 
#her navngir vi index plassen som bokstaven som blir gitt til navnet "plass" for å kunne bruke nummeret i print kommando for å plusse og minuse
print(alfabet[plass-1],alfabet[plass],alfabet[plass+1])

#%%
#oppgave 11
#bruk av sort()
a = [1.3, 2, 2.5, 2.7, 3, 5.1, 4.3, 17]


#bruk av sorted
a = [1.3, 2, 2.5, 2.7, 3, 5.1, 4.3, 17]
sorted(a)





















    

      



    