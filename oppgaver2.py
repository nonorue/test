# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 17:24:11 2025

@author: nicol
"""

#%%
#oppgave 3.12

navn = ['Eli', 'Ola', 'Ali', 'Ela']
tlf = [9423234, 9223001, 4756001, 9592676]
print(navn)
input_nummer = input("Skriv inn navnet til personen du vil få nummer til:")
hentet_navn = navn.index(input_nummer)


print("Nummeret til", navn[hentet_navn],"er:", tlf[hentet_navn])

#%%
#oppgave 3.18

import numpy as np

L = [-2.2, -1, 0, 1.1, 2]

A = np.array(L)

print("L sin type er:", type(L))
print("A sin type er:", type(A))
print("Innholdet i L er:", L)
print("Innholdet i A er:", A)

#%%
#oppgave 3.19

import numpy as np

A = np.array([-2.2, -1, 0, 1.1, 2])
L = [A]

print(L)
print("Datatypen til L er:", type(L))

#%%
#oppgave 3.20

import numpy as np

A1 = np.zeros(5)

A2 = np.ones(5) 

A3 = np.zeros(5)+8.3

A4 = np.zeros(len(A3))+9.4

interval = 0.2
start = 0
slutt = 1
N = int((slutt-start) / interval + 1)

A5 = np.linspace(start, slutt, N)

A6 = np.arange(start, slutt+interval, interval)

print('A1:',A1)
print('A2:',A2)
print('A3:',A3)
print('A4:',A4)
print('A5:',A5)
print('A6:',A6)

#%%
#oppgave 3.21

import numpy as np

B = np.zeros(5)

print("Ved bruk av 'len()' metoden finner vi at B er", len(B),"nuller lang.")
print("Ved bruk av 'np.size()' metoden finner vi at B er", np.size(B),"nuller lang.")
print("Ved bruk av '.shape[]' metoden finner vi at B er", B.shape[0],"nuller lang.")

#%%
#oppgave 3.22

import numpy as np

C = np.array([0,10,20,30])

x = C[0]
print("x er :", x)

y = C[-1]
print("y er:", y)

z = C[1:] # her er fra og med index 1
print("z er:", z)

C[-1] = 50

C[0:2] = 1

print("C =", C)

#%%
#oppgave 3.23

import numpy as np

D = np.array([0, 10, 20, 30])
# Vi skal utvide D med 40 og 50

D = np.append(D,[40,50])
print(D)

#%% 
#oppgave 3.24

import numpy as np

E = np.array([0, 2, 4, 5, 3, 1])

print("Maksimale verdien oppgitt i array er", np.max(E))
print("Indeksen til største verdien er:", np.argmax(E))
#%% ELLER
import numpy as np

E = np.array([0, 2, 4, 5, 3, 1])
max_index = np.argmax(E)
print("Maksimale verdien oppgitt i array er", E[max_index])
print("Indeksen til største verdien er:", max_index)

#%%
#oppgave 3.25

import numpy as np

A = np.array([2,1,3,8,5,4,0])

x = float(input("Enter any number:"))
index_match = np.argmin(np.abs(x - A))
number_match = A[index_match]

print("Matching index number is:", index_match)
print("Number match is:", number_match)

#%%
#oppgave 3.26

import numpy as np

F = np.array([0,1,2,3])
print("F er:", F)
F = F+10
print("Ny F er:", F)

#%%
#oppgave 3.27

import numpy as np
r = np.array([1,2,3])#meter
# V = 4/3 * pi * r**3
V = np.array(4/3*np.pi*r**3)
print("Radiuser i meter:", r)
print("Volum i kubikkmeter:", V)

