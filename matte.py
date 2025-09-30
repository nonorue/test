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

a = float(input("Skriv inn konstanten a:"))
b = float(input("Skriv inn konstanten b:"))
c = float(input("Skriv inn konstanten c:"))

test = b**2 - (4*a*c)

if test > 0:
    print("Denne formelen har to løsninger")
    print(float(andregrad(a, b, c)[0]), float(andregrad(a, b, c)[1]))
elif test ==0:
    print("Denne formelen har en løsning")
    print(andregrad(a, b, c)[0])
else:
    print("Denne ligningen har ingen løsninger")

#%% Areal av rettvinklet rekant med y = ax + b
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

#%% Omkrets av rettvinklet rekant med y = ax + b

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

import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen

# Generer en rekke t-verdier
t_verdier = np.linspace(0, 10, 200)

# Beregn de tilsvarende h(t)-verdiene
h_verdier = h(t_verdier)

# Lag plottet
plt.figure(figsize=(8, 6))
plt.plot(t_verdier, h_verdier)
plt.xlabel('t')
plt.ylabel('h(t)')
plt.xlim(0,20)
plt.ylim(0,30)
plt.grid(True)
plt.show()



