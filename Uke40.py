# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 12:09:12 2025

@author: nicol
"""

# if elif og else
# Undervising er lett da jeg har gjort dette i OLA timene allerede så læremålene er oppnådd
#%% Ikke komplett se "matte" py filen
#Oppgradert andregradsformel
import matplotlib.pyplot as plt
import numpy as np

def andregrad(a, b, c):
    x1 = ((b*-1) + np.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = ((b*-1) - np.sqrt(b**2-(4*a*c)))/(2*a)
    return x1, x2

a = float(input("Skriv inn konstanten a:"))
b = float(input("Skriv inn konstanten b:"))
c = float(input("Skriv inn konstanten c:"))
resultat = np.array(andregrad(a, b, c))
test = b**2 - (4*a*c)

x = np.linspace(resultat-1, resultat+1)

if test > 0:
    print("Denne formelen har to løsninger")
    print(resultat[0], resultat[1])
    #Sett inn plot her
elif test ==0:
    print("Denne formelen har en løsning")
    print(resultat[0])
    #Sett in plot her
else:
    print("Denne ligningen har ingen løsninger")
    
#%% OPPGAVER 7.1-7.8 og 13.3 a)b)
# Oppgave 7.1
# Lag program som angir i konsollen hvilken fase H2= er i for angitt "innlest" temp i grader C, is, vann eller damp

temp = float(input("Angi temperatur (i Celcius)"))

if temp <= 0:
    print("H20 er nå is!")
elif temp < 100:
    print("H20 er nå vann!")
else:
    print("H20 er nå damp!")

#%% Oppgave 7.2
# Personnumme, 11 siffer, siffer 9 er oddetall for gutt partall for jente, er personen oppgitt gutt eller jente?

pers_nummer = int(input("Oppgi de niende sifferet i personnummeret:"))
25120198338
if (pers_nummer % 2) == 0:
    print("Personen er en jente")
else:
    print("Personen er en gutt")

#%% Oppgave 7.3
# avgjør om punktet P = (x,y) ligger i 1..,2..,3. eller 4 kvadrant. x og y skal oppgis i kommandolinjen.
# Altså hvilken sider av aksene punktet er, så (1,1) for eksempel vil ligge i første, (-1, 1) vil ligge i andre, (-1,-1) vil ligge i tredje og (1,-1) vil ligge i fjerde.
x = float(input("Oppgi x koordinat: "))
y = float(input("Oppgi y koordinat: "))


if x==0 or y==0:
    if x==0:
        print("Koordinatene ligger på y-aksen")
    else:
        print("Koordinatene ligger på x-aksen")       
elif (x > 0) and (y > 0):
    print("Koordinatene oppgitt vil ligge i første kvadrant.")
elif (x < 0) and (y > 0):
    print("Koordinatene oppgitt vil ligge i andre kvadrant.")
elif (x < 0) and (y < 0):
    print("Koordinatene oppgitt vil ligge i tredje kvadrant.")
elif (x > 0) and (y < 0):
    print("Koordinatene oppgitt vil ligge i fjerde kvadrant.")
else:
    print("Her har det skjedd noe galt")

#%% Oppgave 7.4
# Bot

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
    
#%% Oppgave 7.5
# A.M eller P.M? Oppgi forekempel 00:00, hint bruk split(':') funksjonen

klokkeslett = input("Oppgi ett klokkeslett (**:**): ")
split_timer = int(klokkeslett.split(':')[0])
split_minutter = int(klokkeslett.split(':')[1])

if (split_timer > 24) or (split_minutter > 60):
    print("Ugyldige verdier oppgitt!")
elif (split_timer == 0) or split_timer < 12:
    print("Oppgitt klokkeslett er A.M!")
else:
    print("Oppgitt klokkeslett er P.M!")
    
#%% Oppgave 7.6
# Gjenta 7.5 til at foreksempel "23:45" blir skrevet som "11:45 pm", og 03:31 blir "3:31 am"

klokkeslett = input("Oppgi ett klokkeslett (**:**): ")
split_timer = int(klokkeslett.split(':')[0])
split_minutter = int(klokkeslett.split(':')[1])

if (split_timer > 24) or (split_minutter > 60):
    print("Ugyldige verdier oppgitt!")
elif split_timer == 12:
    print("Oppgitt klokkeslett er P.M!")
    print("Current time:", split_timer,":", split_minutter,"P.M")
elif (split_timer > 12):
    print("Oppgitt klokkeslett er P.M!")
    print("Current time:", split_timer-12,":", split_minutter,"P.M")
elif split_timer == 0:
    print("Oppgitt klokkeslett er A.M!")
    print("Current time:", split_timer+12,":", split_minutter,"A.M")
else:
    print("Oppgitt klokkeslett er A.M!")
    print("Current time:", split_timer,":", split_minutter,"A.M")

#%% Oppgave 7.7
# last ned of_slo_til.py STUDER hvor mange ganger vil if-testen slå til? summen av array blir 0.1

import numpy as np

arr1 = np.array([1, 2, 3, -5, 7, 0.1, -6])
summen = np.sum(arr1)
size = np.size(arr1)

if_slo_til = 0

if arr1[2] > np.sum(arr1): #denne slår til siden 3 er større enn 2.1
    if_slo_til += 1

if np.size(arr1) == 6 and arr1[0] + arr1[3] < 0: # Denne vil ikke slå inn siden size er 6 og ikke 7, her tok jeg feil.
    if_slo_til += 1

if np.size(arr1) == 6 or arr1[0] + arr1[3] < 0:
    if_slo_til += 1

if arr1[1]*arr1[2] >= 2 and arr1[-1] < 0 or arr1[0]**2 == 4:
    if_slo_til += 1 
    
if  7 in arr1 and np.min(arr1) == -5:    
     if_slo_til += 1

print("Antall ganger if-testen slo til var", if_slo_til)

#%% Oppgave 7.8
# f(x) = sin(x), opp og ned mellom -1 og 1
# dersom x_koor ligger utenfor intervallet [0,4pi] skal tekst "x-koordinaten ligger utenfor intervallet".
# dersom x_koor ligger i intervallet [0,4pi] og f(x_koor) > 1/2 skrives "f(x) er større enn 0.5"
# dersom x_koor ligger i intervallet [0,4pi] og f(x_koor) <= 1/2 skrives "f(x) er mindre eller lik enn 0.5"
# test med ulike x verdier eksempel: -1.2, 0.1, 1.6, 3.1 og 35

import numpy as np
import matplotlib.pyplot as plt
 
def f(x):
    return np.sin(x)

x_koor = float(input("Skriv inn en x-koordinat: "))

x_start = 0
x_slutt = 4*np.pi

x_vals = np.linspace(x_start, x_slutt, 500)
y_vals = f(x_vals)

x_sin = f(x_koor)

plt.figure(1)
plt.plot(x_vals, y_vals, label="f(x)", color='black')
plt.axhline(y=0.5, color='red', linestyle='--', label='$y = 0.5$')



if x_koor < x_start or x_koor > x_slutt:
    print("x-koordinaten ligger utenfor intervallet")
elif x_sin > 0.5:
    print(f"f({x_koor}) er større enn 0.5, det blir {x_sin:.2f}")
    plt.plot(x_koor, x_sin, 'o', markersize=8, color='green', label=f'{x_koor}, {x_sin:.2f}')
else:
    print(f"f({x_koor}) er mindre eller lik enn 0.5, det blir {x_sin:.2f}")
    plt.plot(x_koor, x_sin, 'o', markersize=8, color='green', label=f'Punkt: {x_koor}, {x_sin:.2f}')

plt.legend()
plt.grid()



#%% Hjelp fra AI

import numpy as np
import matplotlib.pyplot as plt

# Definisjon av funksjonen
def f(x):
    return np.sin(x)

# Definer intervallet for plotting
x_start = 0
x_slutt = 4 * np.pi

# Opprett x-verdier for plotting (jevn fordeling av punkter)
x_verdier = np.linspace(x_start, x_slutt, 500)
y_verdier = f(x_verdier)

# --- Få input fra brukeren (som i din opprinnelige kode) ---
try:
    x_koor = float(input("Skriv inn en x-koordinat: "))
except ValueError:
    print("Ugyldig input. Vennligst skriv inn et tall.")
    exit()

# --- Plotting starter her ---
plt.figure(figsize=(10, 6))

# 1. Plott selve funksjonen (sin(x))
plt.plot(x_verdier, y_verdier, label='$f(x) = \sin(x)$', color='blue')

# 2. Plott referanselinjen y = 0.5 (grensen for if/else sjekken)
plt.axhline(y=0.5, color='red', linestyle='--', label='$y = 0.5$')

# 3. Markering av input-punktet og logikk
if x_koor < x_start or x_koor > x_slutt:
   print("x-koordinaten ligger utenfor intervallet [0, 4*pi]")
   # Setter tittelen for å indikere at punktet er utenfor
   plt.title(f'Funksjonen $f(x) = \sin(x)$ i $[0, 4\\pi]$') 
else:
    # Beregn y-verdien for det gitte x
    y_koor = f(x_koor)

    # Marker punktet
    plt.plot(x_koor, y_koor, 'o', color='green', markersize=8, label=f'Punkt: ({x_koor:.2f}, {y_koor:.2f})')

    # Skriv ut meldingen basert på din logikk
    if y_koor <= 0.5:
        print(f"f({x_koor:.2f}) er mindre eller lik 0.5 (Verdi: {y_koor:.2f})")
        plt.vlines(x_koor, ymin=-1, ymax=y_koor, color='green', linestyle=':', linewidth=1)
        
    else:
        print(f"f({x_koor:.2f}) er større enn 0.5 (Verdi: {y_koor:.2f})")
        plt.vlines(x_koor, ymin=-1, ymax=y_koor, color='orange', linestyle=':', linewidth=1)
        
    # Sett tittel med resultat
    plt.title(f'Funksjonen $f(x) = \sin(x)$ i $[0, 4\\pi]$ \nResultat: {y_koor:.2f} vs 0.5')


# 4. Standard plottinnstillinger
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True, which='both', linestyle='-', linewidth=0.5)
plt.xticks(np.arange(0, x_slutt + 1, np.pi), 
           ['0', '$\\pi$', '$2\\pi$', '$3\\pi$', '$4\\pi$']) # Gjør x-aksen penere med pi-verdier
plt.xlim(x_start, x_slutt) # Begrens x-aksen til intervallet
plt.ylim(-1.1, 1.1)    # Begrens y-aksen til sinus-området
plt.legend()
plt.show() # Vis plottet

#%% Oppgave 13.13 WHOOPS
# Trapes a) lag funk med navn trapes med inn(a,b,h) som beregner og returnerer A for et trapes formel = h(a+b)/2
# Test med følgende a = 8, b = 10, h = 5

def trapes(a,b,h):
    return (h*(a+b))/2

side_a = float(input("Oppgi a sidekanten: "))
side_b = float(input("Oppgi b sidekanten: "))
høyde = float(input("Oppgi høyden"))

areal = trapes(side_a, side_b, høyde)
print(f'Totalt areal blir {areal:.2f} kvadrat')

#%% Oppgave 13.3 a)b)
# Bremselengde, formler hvordan man kan regne ut omtrentlig bremselengde (b) i meter for en bil:
# på sommerføre: b = x**2/2, der x er 1/10 av farten v, altså x = v/10
# på vinterføre: b = 2x**2, der x er 1/10 av farten v, altså x = v/10
# merk fart er girr i km/t
# lag funk med navn bremselengde1 med(v), hva blir både sommer og vinter når farten er 90 km/t?

def bremselengde1(v):
    #v_meter = v*3.6 DET ER VIST KILMOTER I TIMEN SOM SKAL INN I FORMELEN WTH
    sommer = (v/10)**2/2
    vinter = 2*((v/10)**2)
    return sommer, vinter

fart = float(input("Oppgi farten, km/t: "))

sommer_resultat, vinter_resultat = bremselengde1(fart)

print(f"\nBremselengden på sommer ved fart på {fart} km/t blir: {sommer_resultat} meter")
print(f"\nBremselengden på vinter ved fart på {fart} km/t blir: {vinter_resultat} meter")

#%% Oppgave 13.3 b) 
# bremselengde2 skal ha iin fart og føre, ved føre indentisk med sommer vil sommer lengden returneres, ved vinter så vinter

def bremselengde2(v, føre):
    if føre == 'sommer':
        brems = (v/10)**2/2
    elif føre == 'vinter':
        brems = 2*((v/10)**2)
    else:
        print("Her har noe gått galt")
    sommer_vinter = føre
    return brems, sommer_vinter

føre = input("Er det 'sommer' eller 'vinter'? Skriv uten '' : ")
fart = float(input("Oppgi farten, km/t: "))

bremse_lengde, sesong = bremselengde2(fart, føre)

print(f"\nBremselengden på {sesong} ved fart på {fart} km/t blir: {bremse_lengde} meter")
#print(f"\nBremselengden på {vinter} ved fart på {fart} km/t blir: {vinter_resultat} meter")





























