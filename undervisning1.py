# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:16:54 2025

@author: nicol
"""

#sånn her lager jeg kommentarer
print(4*3)

tall = 5+2
print(tall)

tall2 = 3*tall
print(tall2)

#tall får ny verdi når den er skrevet på nytt, men tidkligete tall beholdert verdi
tall = 4
print(tall)
print(tall2)

asdf = 5
ASDF = 7
#IKKE LOV MED TALL FØRST
asdf1 = 10
studenter_nye = 13

studenter_antall = 123
print(studenter_antall+studenter_nye)

print(type(tall))

desimaltall = 6.9
print(type(desimaltall))

desimaltall2 = 100/3
print(desimaltall2)
print(round(desimaltall2,2))
print(f'{desimaltall2:.3f}')
stort_desimaltall = 32132435466542.34243234432432
print(stort_desimaltall)
print(f'{stort_desimaltall:.2e}')
lite_desimaltall = 0.000000000000000312312313432
print(f'{lite_desimaltall:.2e}')
#%%
tall3 = desimaltall+4
print(tall3)
#%%
tekst1 = "dette er en tekst"
print(tekst1)
tekst2 = 'dette er også en tekst'
print(tekst2)

tekst3 = "tom's cat"
print(tekst3)
#%%
tekst4 = tekst1 + ' ' + tekst2
print(tekst4)

tall1 = '4'
tall2 = '5'
print(tall1 + tall2)

tall3 = 4
tall4 = 5
print(tall3 + tall4)

#%%

alder = input('hvor gammel er du?')
#sett da tall etter hvor gammel er du? i konsoll for å gi verdi til string
print('du er', alder, 'år gammel')
print("neste år er du", int(alder) + 1, "år")
print("når du er dobbel så gammel så er du", alder*2, "år")

#%%

b1 = True
b2 = False

print(b1)
print(b1 or b2)
print(b1 and b2)
print(not b2)

#%%
a = 4 
b = 3

print(a<b)
print(a>b)
print(a<=b)
#må bruke to == for å bruke =, for ellers så sier du at du vil a skal få samme verdi som b
print(a==b)
# ! spør er om a forskjelling fra b
print(a!=b)

boolsverdi = a<b
print(boolsverdi)

#%%

liste1 = []
print(liste1)
#index på liste begynner på 0
liste2 = [2,5,8,2,9,4]
print(liste2)

liste3 = [2,9.87,"hei",True,liste2, [3,6]]
print(liste3)
print(liste3[2])
#her kan du bytte tall i liste
liste3[1] = 4.5
print(liste3)
#her definerer du en ting i listen
var1 = liste3[2]

var2 = liste3[1:4]
print(var2)
#bytt flere ting samtidig
liste3[0:3] = [100, 200, 300]
print(liste3)
#legge til på slutten av liste
liste3.append(9999)
print(liste3)
#legger til alt fra liste 2 bakerst i liste 3
liste3.extend(liste2)
print(liste3)






















