# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 14:11:31 2025

@author: nicol
"""

import matplotlib.pyplot as plt

x = []
y = []

def f(x):
    return x/2

#def f(x):
    #return x*2

#for i in range(100):
    #x.append(i)
    #y.append(f(i))

x_verdi = 10
x.append(x_verdi)
y.append(f(x_verdi))

x_verdi = 100
x.append(x_verdi)
y.append(f(x_verdi))



plt.plot(x,y)

#%%

a = 10
b = 20
c = 20/2

if(a<b):  # Betingelse
    print("a er mindre enn b")  
if(b==c):
    print("b er lik c")
else: c = b
print(c)

#%%

tall = float(input("Skriv inn ett tall:"))

if (tall>=0):
    print("Tallet", tall, "er større eller lik 0")
else: 
    print("Tallet", tall, "er ikke større eller lik 0")
    
#%%

tall = float(input("Skriv inn ett tall:"))

if (tall>100):
    print("Tallet", tall, "er større enn 100")
elif(tall>50):
    print("Tallet", tall, "er mindre enn 100 og større enn 50")
elif(tall>25):
    print("Tallet", tall, "er mindre enn 50 og større enn 25")
else: 
    print("Tallet", tall, "er mindre enn 25")



































