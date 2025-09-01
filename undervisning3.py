# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 12:15:48 2025

@author: nicol
"""

#abs() = absolutt verdi av ett tall

import numpy as np


def avrund_tall(tall):
    res_avrund = round(tall, 2)
    res_opp = np.ceil(int(tall))
    res_ned = np.floor(int(tall))
    return res_avrund, res_opp, res_ned


tall_input = float(input("Sett inn tall:"))
svar = avrund_tall(tall_input)


print("Når vi runder av med to desimaler får vi:", svar[0])
print("Når vi runder opp blir heltall:", svar[1])
print("Når vi runder ned blir heltall:", svar[2])

#print("Når vi runder av med to desimaler får vi:", res_avrund)
#print("Når vi runder opp blir heltall:", int(res_opp))
#print("Når vi runder ned blir heltall:", int(res_ned))

#%%

def total_sekund(t, m, s):
    timer_til_sek = t * 60 * 60
    min_til_sek = m * 60
    sek_tot = timer_til_sek + min_til_sek + s
    return sek_tot


t = float(input("Sett inn timer:"))
m = float(input("Sett inn minutter:"))
s = float(input("Sett inn sekunder:"))
svar = total_sekund(t,m,s)
print("Totalt er det", int(svar), "sekunder")

#%%

def sek2tms(sek):
    t, rest = divmod(sek, 3600)
    m, rest = divmod(rest, 60)
    s = rest
    return t, m ,s


sekunder = int(input("Sett inn sekunder:"))
svar = sek2tms(sekunder)
# timer, minutter, sekunder = sek2tms(sekunder)
#print("Timer er:", timer)
#print("Minutter er:", minutter)
#print("Sekunder er:", sekunder)
print("Timer:", svar[0])
print("Minutter:", svar[1])
print("Sekunder:", svar[2])

#%%

import numpy as np

def beregn_array(arr):
    lengde = np.size(arr)
    gj_snitt = (arr[0] + arr[lengde-1])/2
    pos = np.argmin(arr)
    svar = arr[0]>0
    return lengde, gj_snitt, pos, svar

 
my_array = np.array([3,8,-1,-4.8,23,7])
resultat = beregn_array(my_array)

print(resultat)

    
    
    

    