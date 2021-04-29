"""TP n°2 génie mathematique (Ma123) 
Julien Fischer, Frédérique Bergez"""

import math
import matplotlib.pyplot as plt
import numpy as np

"""def g1(x):
    return (9-3*x)**(1/4)
def g1bis(x):
    return -1*((9-3*x)**(1/4))
def g2(x):
    return math.acos((2+x)/3)
def g3(x):
    return math.log(7)-math.log(x)
def g4(x):
    return math.log(10+x)
def g5(x):
    return math.atan((x+5)/2)
def g6(x):
    return math.log((x**2)+3)
def g7(x):
    return (7-(4*math.log(x)))/3
def g8(x):
    return (2*(x**2)-4*x+17)**(1/4)"""
def g9(x):
    return math.log(2*(math.sin(x))+7)
"""def g10(x):
    return math.log(10)-math.log(math.log((x**2)+4))
def g11(x):
    return (1+math.sin(x))/2"""
    

def PointFixe(g,x0,epsilon,Nitermax, alpha):
    xold = x0
    xnew = g(xold)
    erreur = xnew - xold
    n = 0
    liste_n = []
    liste_ern = []
    liste_x = []
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = g(xold)
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
    plt.title("Evolution des erreurs (pt fixe)")
    plt.grid()
    plt.show()
    return liste_n, liste_ern, liste_x

"""print("-----"*10)
print("solution de g1(x) = x pour f1 :")
print(PointFixe(g1,3/2,1e-4,1e4,1.46491770894120))
print("-----"*10)

print("solution de g1bis(x) = x pour f1 :")
print(PointFixe(g1bis,-2,1e-4,1e4,-1.96448573955270))
print("-----"*10)

print("solution de g2(x) = x pour f2 :")
print(PointFixe(g2,0.54,1e-4,1e4,0.5529448834034))
print("-----"*10)

print("solution de g3(x) = x pour f3 :")
print(PointFixe(g3,1.5,1e-4,1e4,1.5243449567561))
print("-----"*10)

print("solution de g4(x) = x pour f4 :")
print(PointFixe(g4,2.5,1e-4,1e4,2.5279632079786))
print("-----"*10)

print("solution de g5(x) = x pour f5 :")
print(PointFixe(g5,1.5,1e-4,1e4,1.2616323998446))
print("-----"*10)

print("solution de g6(x) = x pour f6 :")
print(PointFixe(g6,1.8,1e-4,1e4,1.8731224913332))
print("-----"*10)

print("solution de g7(x) = x pour f7 :")
print(PointFixe(g7,1.4,1e-4,1e4,1.9473946913293))
print("-----"*10)

print("solution de g8(x) = x pour f8 :")
print(PointFixe(g8,2,1e-4,1e4,2.034753263539))
print("-----"*10)"""

print("solution de g9(x) = x pour f9 :")
print(PointFixe(g9,2,1e-4,1e4,1.8607054167921))
print("-----"*10)

""""print("solution de g10(x) = x pour f10 :")
print(PointFixe(g10,1.6,1e-4,1e4,2.3287346158751))
print("-----"*10)

print("solution de g11(x) = x pour f11 :")
print(PointFixe(g11,0,1e-4,1e4,0.8878621503814))
print("-----"*10)"""