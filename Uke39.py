# -*- coding: utf-8 -*-
"""
Plotting

"""

import numpy as np
import matplotlib.pyplot as plt

x_vals = np.array([0,1,2])

y_vals = np.array([5,3,4])

x_vals2 = np.array([1,2,3])
y_vals2 = np.array([1,0,4])


plt.figure(1)#Figurer
plt.plot(x_vals, y_vals)
plt.figure(2)#Figurer, vil komme i to egne bilder
plt.plot(x_vals2, y_vals2)
plt.figure(1)#Åpner for bilde 1 på nytt slik at man kan putte nye ting inn
plt.plot(x_vals, y_vals2) #Hvis linje 22 blir fjernet havner dette i figure 2

#%%

plt.figure(3)
plt.subplot(2,2,1)# Øverst til venstre
plt.plot(x_vals, y_vals, 's:g') #s for firkant, : for stipla linje, g for grønn
plt.subplot(2,2,2)
plt.plot(x_vals2, y_vals2, 'h-m') # uten linje "-" vil linje være usyndlig så ledd kan fjernes
plt.subplot(2,2,3)
plt.plot(x_vals2, y_vals, marker='o', linestyle='dotted', color='black')
plt.subplot(2,2,4)
plt.plot(x_vals, y_vals2)

# plt.show()

#%%

mnd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
kr = np.array([3212,4532,7765,12343,1234,4532,25354,4534,7743,2345,554,7654])

plt.figure(4)
plt.xlabel('Måned')
plt.ylabel('Saldo')
plt.plot(mnd, kr)
plt.axis([0, 13, -500, 30000])
plt.grid()#Rutenett
plt.title('Saldo gjennom året')

#%%

x_vals = np.linspace(1, 400, 1000)
y_vals = np.sqrt(x_vals)


plt.figure(5)
plt.plot(x_vals, y_vals)

#%%

x_vals = np.linspace(0, np.pi*4, 1000)
#y_vals = np.sin(x_vals)
plt.figure(6)
plt.plot(x_vals, np.sin(x_vals), label='Sinus(x)')
plt.plot(x_vals, np.cos(x_vals), label='Cosinus(x)')
plt.legend()
plt.axis([0, np.pi*4+5, -1.5, 1.5])

#%%

plt.figure(7)
karakterer = np.array(['F', 'E', 'D', 'C', 'B', 'A'])
fordeling = np.array([3, 6, 15, 43, 34, 23])
plt.bar(karakterer, fordeling, color=('green', 'black', 'orange'))#Bruker farger på nytt når liste er brukt opp
plt.xlabel('Karakter')
plt.ylabel('Antall')
plt.title('Karakterer til studenter')

#%%

karakterer = np.array(['F', 'E', 'D', 'C', 'B', 'A'])
fordeling = np.array([3, 6, 15, 43, 34, 23])

plt.figure(8)
plt.title('Karakterer til studenter')
plt.pie(fordeling, labels=karakterer) #Se her den hener fra karakterer variabel

#%%

n = 10000
x = np.random.randn(n) # kaller opp n tilfeldige tall med 0 som gjennomsnitt
bins = 100 # Bokser
plt.figure(9)
plt.hist(x, bins) # Tall fordelt inn i bokser

#%%
# Oppgave 4.1-6 og 5.10-11
# Oppgave 4.1

#Vi skulle ta utgnagspunkt i program 4.2

"""
Middeltempratur pr mnd i Skien
"""
import numpy as np
import matplotlib.pyplot as plt

mnd = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
temp = np.array([-3,-2,2,7,11,15,17,16,12,6,2,-3])

mean_temp = np.mean(temp) #middelverdi av grader
print(f'Middelverdi = {mean_temp:.1f} Celsius')

plt.close('all')
plt.figure(10)
plt.plot(mnd, temp, 'b-o', label='Temperatur')
plt.plot(mnd, temp*0 + mean_temp, 'g', label='Middelverdi')
plt.legend()
plt.title('Midlere månedstemp i Skien 2005-2015')
plt.xlabel('Måned nr.')
plt.ylabel('Grader Celsius')
plt.xlim(0,13)
plt.ylim(-5,20)
plt.grid()
plt.show()

#%%
# Modifisert program ifølge oppgave 4.1:

"""
Meanian temperature in Skien
program made by NN : n.n@usn.no

"""
import numpy as np
import matplotlib.pyplot as plt

mnth = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
temp_c = np.array([-3,-2,2,7,11,15,17,16,12,6,2,-3])

mean_temp_c = np.mean(temp) #middelverdi av grader Celsius
mean_temp_f = mean_temp_c*(9/5)+32
print(f'Median = {mean_temp_f:.1f} ')

temp_f = temp_c*(9/5)+32 # Konverterer til farenheit

plt.close('all')
plt.figure(10)

plt.plot(mnth, temp_f, 'b-*', color='g', label='Temperature')
plt.plot(mnth, temp_f*0 + mean_temp_f, 'r', label='Median')

plt.legend()
plt.title('Monthly degrees with median in Skien 2005-2015')
plt.xlabel('Month nr.')
plt.ylabel('Degrees in Farenheit')
plt.xlim(1,12)
# plt.ylim(-5,20) denne fjernes 
plt.grid()
plt.show()

#%%
# Oppgave 4.2

x_vals = np.array([0,1,2,3,4,5])
y_vals = x_vals
z_vals = np.sqrt(x_vals)


plt.figure(11)
plt.plot(x_vals, y_vals, color='r', marker='*', label='X og Y')
plt.plot(x_vals, z_vals, color='b', marker='o', label='X og Z')
plt.legend()
plt.grid()
plt.xlabel('x[s]')
plt.ylabel('[m]')


plt.savefig('plott1.pdf')

#%%
#Oppgave 4.3
#Samme som 4.2 vare med subplot

x_vals = np.array([0,1,2,3,4,5])
y_vals = x_vals
z_vals = np.sqrt(x_vals)


plt.figure(11)
plt.subplot(2, 1, 1)
plt.plot(x_vals, y_vals, color='r', marker='*', label='X og Y')
plt.grid()
plt.xlabel('x[s]')
plt.ylabel('[m]')
plt.legend()
plt.xlim(-0.5,5.5)
plt.ylim(-1,6)


plt.subplot(2, 1, 2)
plt.plot(x_vals, z_vals, color='b', marker='o', label='X og Z')
plt.legend()
plt.grid()
plt.xlabel('x[s]')
plt.ylabel('[m]')
plt.xlim(-0.5,5.5)
plt.ylim(-1,6)


plt.savefig('plott2.pdf')

#%%
#Oppgave 4.4

firma = ['Firma A', 'Firma B', 'Firma C']
salg = [1204, 1119, 998]
plt.figure(12)
plt.bar(firma, salg)

#%%
#Oppgave 4.5
# Modifiser 4.4 slik at firmanavn nå vises på y akse og salg på x

firma = ['Firma A', 'Firma B', 'Firma C']
salg = [1204, 1119, 998]
plt.figure(13)
plt.barh(firma, salg)

#%%
#Oppgave 4.6
# Nå lage ett kakediagram

firma = ['Firma A', 'Firma B', 'Firma C']
salg = [1204, 1119, 998]
plt.figure(14)
plt.pie(salg, labels=firma, autopct='%1.1f%%')

plt.axis('equal') # Perfekt sirkel
plt.title('Salgfordeling')

#%%
#Oppgave 5.10

def f(x):
    return x**2 + 3
def g(x):
    return 3*x - 1 

# Plott så funksjonene på intervallet xE [-2, 3] legg kurvebeskrivelser inn i plott

x_aks1 = np.linspace(-2,3, 10000)
y_aks1 = f(x_aks1)

x_aks2 = np.linspace(-2,3, 10000)
y_aks2 = g(x_aks2)

plt.figure(15)
plt.plot(x_aks1, y_aks1, label='f(x)', color='g')
plt.plot(x_aks2, y_aks2, label='g(x)', color='black')
plt.legend()

#%%
#Oppgave 5.11
# Plott f(g(x)) og g(f(x)) på intervallet xE [-2, 3] legg kurvebeskrivelser inn i plott

def f(x):
    return x**2 + 3
def g(x):
    return 3*x - 1 

x_aks1 = np.linspace(-2,3, 10000)
y_aks1 = f(g(x_aks1))

x_aks2 = np.linspace(-2,3, 10000)
y_aks2 = g(f(x_aks2))

plt.figure(15)
plt.plot(x_aks1, y_aks1, label='f(g(x))', color='g')
plt.plot(x_aks2, y_aks2, label='g(f(x))', color='black')
plt.legend()











    



























