# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 12:11:54 2025

@author: nicol
"""
#%%
mitt_heltall = 64
print(mitt_heltall)

mitt_desimaltall = 3.1415
print(mitt_desimaltall)

min_tekst = "God dag"
print(min_tekst)

min_sannhetsverdi = True
print(min_sannhetsverdi)

min_liste = [2,3,4,5]
print(min_liste)
print(min_liste[2])
min_liste[2] = 7
print(min_liste)

#%%

tuppel_1 = (2,3,4,5,6)
print(tuppel_1)
print(tuppel_1[2])
# ikke lov med tuppel_1[2] = 7
tuppel_2 = (3,3,3)
print(tuppel_2)

tuppel_3 = tuppel_1 + tuppel_2
print(tuppel_3)

tuppel_4 = tuppel_1 * 3
print(tuppel_4)

tuppel_4 = (2,6,34)
print(tuppel_4)

#%%

bil = {'merke': 'Tesla',
       'modell': 'Y',
       'år': 2022}
print(bil['merke'])
print(bil['modell'])
print(bil['år'])

bil['reg_nr'] = 'KYS123'
bil['år'] = 2024
bil['år'] = bil['år'] + 1
print(bil)

bil['merke'] = 'BMW'
bil['modell'] = 'IX'
print(bil)

bil_som_liste = ['BMW', 'IX', 2025, 'KYS123']
print(bil_som_liste[3])
print(bil['reg_nr'])

#%%

import numpy as np

liste1 = [1,2,3,4,5]
arr1 = np.array(liste1)
print(liste1)
print(arr1)

print(liste1[2])
print(arr1[2])

arr2 = np.array([6,7,8,9])
print(arr2)

arr3 = np.zeros(12)
print(arr3)

arr4 = np.ones(8)
print(arr4)
#%%
import numpy as np
l1 = [1,2,3]
a1 = np.array(l1)
print('l1 =', l1)
print('a1 =', a1)

l2 = l1*4
a2 = a1*4 
print("l2 =", l2)
print("a2 =", a2)

l3 = l1 + [10]
a3 = a1 + 10
print("l3 =", l3)
print("a3 =", a3)

#toere = np.zeros(8)
#toere = toere+2
#toere = np.zeros(8)+2
toere = np.ones(8)*2
print(toere)

toere_liste = [2.]*8
print(toere_liste)

en_til_to = np.linspace(1.0, 2.0, 101)
print(en_til_to)

en_til_to2 = np.arange(1.0, 2.0, 0.1)
print(en_til_to2)
#%%
import numpy as np
arr = np.array([2.543,4.23,-342.2,-4.24])
max_index = np.argmax(arr)
print("den største index verdien er:",max_index,
      "det største tallet er:", arr[max_index])

min_index = np.argmin(arr)
print("den minste index verdien er:",min_index,
      "det minste tallet er:", arr[min_index])

#%%
import numpy as np
arr2D = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
print(arr2D)
print(arr2D[1])
print(arr2D[2][1])


