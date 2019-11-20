# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:42:25 2019

@author: Fabi
"""

import scipy as sp
import matplotlib.pylab as plt

x = [3.55*(2**-5), 3.55*(2**-6), 3.55*(2**-7), 3.55*(2**-8)]
Num = len(x)

#Resultados exactos de cada valor de la lista x, evaluados en la funcion x**3  
resultados_exactos = [0.00136532211, 0.00017066526, 0.00002133315, 0.00000266664 ]


#Funcion que muestra los resultados de la avaluacion de los valores en la funcion, pero en float 32
en_float_32 = []
for i in x:
    x_32=sp.float32(i**3)
    en_float_32.append(x_32)
#Funcion que muestra los resultados de la avaluacion de los valores en la funcion, pero en float 64
en_float_64 = []
for i in x:
    x_64=sp.float64(i**3)
    en_float_64.append(x_64)
    
    #Calculo de errores
erroren_float32 = []
erroren_float64 = []

i = 0
while i < Num:
    erroren_float32.append((abs(en_float_64[i] - resultados_exactos[i]))/resultados_exactos[i])
    erroren_float64.append((abs(en_float_32[i] - resultados_exactos[i]))/resultados_exactos[i])
    i+=1


#Grafica de los errores
plt.figure(1)
plt.plot(x,erroren_float32, label="Error float 32" )
plt.plot(x,erroren_float64, label="Error float 64" )

plt.xlabel("x")
plt.ylabel("Error relativo f(x) = x^3")
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=1.)

plt.show()
#Resultados mostrados en la consola

print "\n"
print "Valores exactos: ", resultados_exactos, "\n"
print "Valores en float 64: \n", en_float_32, "\n"
print "Error en float 64: \n",erroren_float32, "\n"
print "Valores en float 32: \n", en_float_64, "\n"
print "Error en float 32: \n",erroren_float64, "\n"

