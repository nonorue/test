# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 14:13:03 2025

OLA 6 Uke 39
"""

import numpy as np
import matplotlib.pyplot as plt

# Plot y = 2x + 3for x E -5,5
# oppgave 1
x = np.linspace(-5, 5, 1000)
y = 2*x + 3

plt.plot(x, y)

#%%


x = np.linspace(-2,2, 1000)
y1 = x**2
y2 = x**3

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()

#%% 

dager = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag','Lørdag','Søndag']
tempratur = [3,5,7,6,4,8,10]

plt.plot(dager, tempratur)

#%% oppgave 4
# plot y=e^x
x = np.linspace(-2,2,1000)
y = np.e ** x
plt.plot(x,y)

#%%

x = np.linspace(np.pi*-2, np.pi*2, 10000)
y1 = x - ((x**3)/6)
y2 = np.sin(x)
plt.plot(x, y2, label='x - ((x**3)/6)')
plt.plot(x, y1, label='sin(x)')
plt.legend()

#%%

tall = 10

for i in range(10):
    print(tall)
    
x = 0
while x < 10:
    print(x)
    x = x + 1
    
#%% if

temp = float(input('Oppgi temperatur på H2O i Celsius:'))

if (temp >= 100):
    print('H2O er damp')
elif (temp>=0): # hvis bare if og det er 100 grader vil damp og væske printes
    print('H2O er væske')
else:
    print('H2O er is')
    
#%%

# % operatoren blir rest av en divisjon

tall = int(input('skriv inn et heltall:'))

if (tall % 2 == 0):
    print(tall, 'er et partall')
else:
    print(tall, 'er et oddetall')
    
#%%

fart = int(input("Skriv inn din fart (km/t) i 60 sonen:"))

sone = 60

if (fart <= sone):
    print("Du har ikke fått bot")
elif (fart <= sone+5):
    print("Du har fått 800 kr i bot")
elif (fart <= sone+10):
    print("Du har fått 2100 kr i bot")
elif (fart <= sone+15):
    print("Du har fått 3800 kr i bot")
elif (fart <= sone+20):
    print("Du har fått 5500 kr i bot")
elif (fart <= sone+25):
    print("Du har fått 8500 kr i bot")
else:
    print('Du er kjørt')

        

    
    























