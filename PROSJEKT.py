# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 14:21:52 2025

@author: nicol
"""

#%% Oppgave 1

alder = int(input('Hvilket år er du født? '))

def alder_2025(x):
    return 2025-x

alder2 = alder_2025(alder)
print("I 2025 vil du bli", alder2, "år gammel")

#%% Oppgave 2

import math as m


antall_elever = int(input('Skriv inn antall elever:'))

ant_pizza = m.ceil(antall_elever*0.25)

print("Det må kjøpes inn", int(ant_pizza), "pizza.")

#%% Oppgave 3

import numpy as np  

v_g = float(input('Skriv inn gradtallet:')) 

def g_til_r(x):
    radian = (x * np.pi)/180
    print("Din radian med gitt gradtall er:", f'{radian:.2f}')

g_til_r(v_g)

#%% Oppgave 4 a)

# Be brukeren om å skrive inn antall sekunder
totalt_sekunder = int(input("Skriv inn antall sekunder: "))

# Beregn timer, minutter og sekunder
timer = totalt_sekunder // 3600
resterende_sekunder = totalt_sekunder % 3600
minutter = resterende_sekunder // 60
sekunder = resterende_sekunder % 60

# Skriv ut resultatet
print(f"{totalt_sekunder} sekunder tilsvarer {timer} timer, {minutter} minutter og {sekunder} sekunder.")

#%% Oppgave 4 b)

def konverter_tid(sekunder):
    """Tar et antall sekunder og returnerer timer, minutter og sekunder."""
    timer = sekunder // 3600
    resterende = sekunder % 3600
    minutter = resterende // 60
    sekunder = resterende % 60
    return timer, minutter, sekunder

# Hovedprogram
totalt_sekunder = int(input("Skriv inn antall sekunder: "))
timer, minutter, sekunder = konverter_tid(totalt_sekunder)

print(f"{totalt_sekunder} sekunder tilsvarer {timer} timer, {minutter} minutter og {sekunder} sekunder.")

#%% Oppgave 4 c)

import matplotlib.pyplot as plt

def konverter_tid(sekunder):
    """Tar et antall sekunder og returnerer timer, minutter og sekunder."""
    timer = sekunder // 3600
    resterende = sekunder % 3600
    minutter = resterende // 60
    sekunder = resterende % 60
    return timer, minutter, sekunder

# Hovedprogram
totalt_sekunder = int(input("Skriv inn antall sekunder: "))
timer, minutter, sekunder = konverter_tid(totalt_sekunder)

print(f"{totalt_sekunder} sekunder tilsvarer {timer} timer, {minutter} minutter og {sekunder} sekunder.")

# Data for visualisering
labels = ['Timer', 'Minutter', 'Sekunder']
verdier = [timer, minutter, sekunder]

# Barplot
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.bar(labels, verdier, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Tid i Barplot')
plt.ylabel('Antall')

# Sektordiagram
plt.subplot(1, 2, 2)
plt.pie(verdier, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Tid i Sektordiagram')

plt.tight_layout()
plt.show()

#%% Oppgave 4 d)

# Importerer matplotlib for å lage grafer
import matplotlib.pyplot as plt

def konverter_tid(sekunder):
    """
    Konverterer et gitt antall sekunder til timer, minutter og sekunder.

    Parametere:
        sekunder (int): Totalt antall sekunder som skal konverteres.

    Returnerer:
        tuple: (timer, minutter, sekunder)
    """
    # Beregner antall hele timer ved å dele på 3600 (sekunder per time)
    timer = sekunder // 3600

    # Finner resterende sekunder etter at timer er trukket fra
    resterende = sekunder % 3600

    # Beregner antall hele minutter fra de resterende sekundene
    minutter = resterende // 60

    # Finner de siste sekundene som ikke utgjør en hel time eller et helt minutt
    sekunder = resterende % 60

    # Returnerer resultatet som en tuple
    return timer, minutter, sekunder

# Starter hovedprogrammet
# Ber brukeren om å skrive inn et heltall som representerer antall sekunder
totalt_sekunder = int(input("Skriv inn antall sekunder: "))

# Kaller funksjonen for å konvertere sekunder til timer, minutter og sekunder
timer, minutter, sekunder = konverter_tid(totalt_sekunder)

# Skriver ut resultatet i et lesbart format
print(f"{totalt_sekunder} sekunder tilsvarer {timer} timer, {minutter} minutter og {sekunder} sekunder.")

# Lager en liste med etiketter for hver tidsenhet
labels = ['Timer', 'Minutter', 'Sekunder']

# Lager en liste med verdiene som skal visualiseres
verdier = [timer, minutter, sekunder]

# Oppretter en ny figur med bredde 10 og høyde 4 tommer
plt.figure(figsize=(10, 4))

# Første subplot: Barplot
plt.subplot(1, 2, 1)  # Plasserer barplot i første kolonne
plt.bar(labels, verdier, color=['skyblue', 'lightgreen', 'salmon'])  # Lager stolpediagram med farger
plt.title('Tid i Barplot')  # Setter tittel på diagrammet
plt.ylabel('Antall')  # Setter etikett på y-aksen

# Andre subplot: Sektordiagram (pie chart)
plt.subplot(1, 2, 2)  # Plasserer sektordiagram i andre kolonne
plt.pie(
    verdier,  # Verdiene som skal fordeles
    labels=labels,  # Etiketter for hver sektor
    autopct='%1.1f%%',  # Viser prosent med én desimal
    colors=['skyblue', 'lightgreen', 'salmon']  # Farger som matcher barplot
)
plt.title('Tid i Sektordiagram')  # Setter tittel på sektordiagrammet

# Justerer layout slik at begge diagrammene vises pent ved siden av hverandre
plt.tight_layout()

# Viser grafene i et nytt vindu
plt.show()

#%% Oppgave 4 e) 

import matplotlib.pyplot as plt

def konverter_tid(sekunder):
    # Konverterer sekunder til timer, minutter og sekunder
    timer = sekunder // 3600
    resterende = sekunder % 3600
    minutter = resterende // 60
    sekunder = resterende % 60
    return timer, minutter, sekunder

# Input fra bruker
totalt_sekunder = int(input("Skriv inn antall sekunder: "))
timer, minutter, sekunder = konverter_tid(totalt_sekunder)

# Skriver ut i formatet 5:33:20
print(f"{timer}:{minutter:02}:{sekunder:02}")

# Visualisering
labels = ['Timer', 'Minutter', 'Sekunder']
verdier = [timer, minutter, sekunder]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.bar(labels, verdier, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Tid i Barplot')

plt.subplot(1, 2, 2)
plt.pie(verdier, labels=labels, autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'salmon'])
plt.title('Tid i Sektordiagram')

plt.tight_layout()
plt.show()

#%% Oppgave 4 f)

import matplotlib.pyplot as plt

def konverter_tid(sekunder):
    """
    Konverterer et gitt antall sekunder til timer, minutter og sekunder.
    """
    timer = sekunder // 3600
    resterende = sekunder % 3600
    minutter = resterende // 60
    sekunder = resterende % 60
    return timer, minutter, sekunder

# Input fra bruker
totalt_sekunder = int(input("Skriv inn antall sekunder: "))
timer, minutter, sekunder = konverter_tid(totalt_sekunder)

# Formaterer tiden som en digital klokke med to sifre per enhet
digital_tid = f"{timer:02}:{minutter:02}:{sekunder:02}"

# Lager en figur som viser tiden som en digital klokke
fig, ax = plt.subplots(figsize=(6, 3))
ax.set_facecolor("black")  # Bakgrunnsfarge som en digital skjerm
ax.text(0.5, 0.5, digital_tid, fontsize=60, color="lime", ha='center', va='center', fontweight='bold')

# Fjerner akser og rammer for å få et rent klokkeutseende
ax.set_xticks([])  # Skjuler x-aksens tallverdier
ax.set_yticks([])  # Skjuler y-aksens tallverdier

# Denne for-løkken går gjennom alle kantlinjene (spines) i figuren
# Spines er linjene som omgir figuren (venstre, høyre, topp og bunn)
for navn, spine in ax.spines.items():
    # 'navn' er navnet på kanten (f.eks. 'left', 'right', 'top', 'bottom')
    # 'spine' er selve objektet som representerer den kanten
    # Vi setter synligheten til False for å skjule hver enkelt kant
    spine.set_visible(False)

# Viser figuren
plt.title("Digital klokkevisning", color="white", pad=20)
plt.tight_layout()
plt.show()

















