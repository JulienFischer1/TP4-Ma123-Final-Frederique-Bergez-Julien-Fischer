"""TP n°3 génie mathematique (Ma123) 
Julien Fischer, Frédérique Bergez""" 

import math
import matplotlib.pyplot as plt
import numpy as np

"""def f0(x): 
    return x+1
def fder0(x):
    return 1
def f1(x):
    return (x**4)+3*x-9
def fder1(x):
    return 4*(x**3)+3
def f1bis(x):
    return (x**4)+3*x-9
def fder1bis(x):
    return 4*(x**3)+3
def f2(x):
    return x-3*(math.cos(x))+2
def fder2(x):
    return 1+3*math.sin(x)
def f2bis(x):
    return x-3*(math.cos(x))+2
def fder2bis(x):
    return 1+3*math.sin(x)
def f2ter(x):
    return x-3*(math.cos(x))+2
def fder2ter(x):
    return 1+3*math.sin(x)
def f3(x):
    return x*(math.exp(x))-7
def fder3(x):
    return (1+x)*(math.exp(x))
def f4(x):
    return math.exp(x)-x-10
def fder4(x):
    return math.exp(x)-1
def f4bis(x):
    return math.exp(x)-x-10
def fder4bis(x):
    return math.exp(x)-1
def f5(x):
    return 2*math.tan(x)-x-5
def fder5(x):
    return (2/((math.cos(x))**2))-1
def f6(x):
    return math.exp(x)-(x**2)-3
def fder6(x):
    return math.exp(x)-2*x
def f7(x):
    return 3*x+4*math.log(x)-7
def fder7(x):
    return 3+(4/x)
def f8(x):
    return (x**4)-2*(x**2)+4*x-17
def fder8(x):
    return 4*(x**3)-4*x+4
def f8bis(x):
    return (x**4)-2*(x**2)+4*x-17
def fder8bis(x):
    return 4*(x**3)-4*x+4"""
def f9(x):
    return math.exp(x)-2*math.sin(x)-7
def fder9(x):
    return math.exp(x)-2*math.cos(x)
"""def f10(x):
    return math.log((x**2)+4)*math.exp(x)-10
def fder10(x):
    return math.exp(x)*math.log((x**2)+4)+((2*x)/((x**2)+4))
def f11(x):
    return 2*x-(1+math.sin(x))
def fder11(x):
    return 2-math.cos(x)"""

def Newton(f,fder,x0,epsilon,Nitermax,alpha):
    xold = x0
    xnew = xold-((f(xold))/(fder(xold)))
    erreur = xnew - xold
    n = 0
    liste_n = []
    liste_ern = []
    liste_x = []
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold-((f(xold))/(fder(xold)))
        erreur = xnew - xold
        xold = xnew
        n += 1
        ern = abs(xnew - alpha)
        liste_n.append(n)
        liste_ern.append(ern)
        liste_x.append(xnew)
    x = np.array(liste_n)
    y = np.array(liste_ern)
    plt.semilogy(x, y)
    plt.xlabel("valeur de n")
    plt.ylabel("valeur de ern")
    plt.title("Evolution des erreurs (Newton)")
    plt.grid()
    plt.show()
    return liste_n, liste_ern, liste_x

"""print("-----"*10)
print("solution de f0 (test) :")
Newton(f0, fder0,0,1e-4,1e4)
print("-----"*10)


print("solution de f1 :")
print(Newton(f1, fder1,3/2,1e-4,1e4,1.46491770894120))
print("-----"*10)

print("solution de f1bis :")
print(Newton(f1bis, fder1bis,-2,1e-4,1e4,-1.96448573955270))
print("-----"*10)

print("solution de f2 :")
print(Newton(f2, fder2,0.54,1e-4,1e4,0.5529448834034))
print("-----"*10)

print("solution de f2bis :")
print(Newton(f2bis, fder2bis,-1.4,1e-4,1e4,-1.3536404563123))
print("-----"*10)

print("solution de f2ter :")
print(Newton(f2ter, fder2ter,-3.5,1e-4,1e4,-3.9880104536189))
print("-----"*10)

print("solution de f3 :")
print(Newton(f3, fder3,1.4,1e-4,1e4,1.5243449567561))
print("-----"*10)

print("solution de f4 :")
print(Newton(f4, fder4,2.5,1e-4,1e4,2.5279632079786))
print("-----"*10)

print("solution de f4bis :")
print(Newton(f4bis, fder4bis,-10.3,1e-4,1e4,-9.9999545038685))
print("-----"*10)

print("solution de f5 :")
print(Newton(f5, fder5,1.5,1e-4,1e4,1.2616323998446))
print("-----"*10)

print("solution de f6 :")
print(Newton(f6, fder6,1.8,1e-4,1e4,1.8731224913332))
print("-----"*10)

print("solution de f7 :")
print(Newton(f7, fder7,1.4,1e-4,1e4,1.9473946913293))
print("-----"*10)

print("solution de f8 :")
print(Newton(f8, fder8,2,1e-4,1e4,2.034753263539))
print("-----"*10)

print("solution de f8bis :")
print(Newton(f8bis, fder8bis,-2.8,1e-4,1e4,-2.5089616851003))
print("-----"*10)"""

print("solution de f9 :")
print(Newton(f9, fder9,2,1e-4,1e4,1.8607054167921))
print("-----"*10)

"""print("solution de f10 :")
print(Newton(f10, fder10,0,1e-4,1e4,2.3287346158751))
print("-----"*10)

print("solution de f11 :")
print(Newton(f11, fder11,0,1e-4,1e4,0.8878621503814))
print("-----"*10)"""