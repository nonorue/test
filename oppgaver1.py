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

import numpy as n
number = n.array(

#%%
#oppgave 3.3
#%%
#oppgave 3.4
#%%
#oppgave 3.5
#%%
#oppgave 3.6
#%%
#oppgave 3.7
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





















    

      



    