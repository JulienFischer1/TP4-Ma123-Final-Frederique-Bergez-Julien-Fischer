""" Julie Fischer Frederique Bergez Ma123
    Methode de la Sécante"""

import math as m
import matplotlib.pyplot as plt
import numpy as np

"""def f1(x):
    return (x**4)+3*x-9

def f7(x):
    return (3*x)+(4*(m.log(x)))-7"""

def f9(x):
    return (m.exp(x))-(2*m.sin(x))-7

"""def f11(x):
    return 2*x-(1+m.sin(x))"""

def Secante(f, x0, x1, epsilon,Nitermax,alpha):
    x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
    erreur = x2 - x1
    n = 0
    liste_n = []
    liste_ern = []
    liste_x = []
    while abs(erreur) > epsilon and n < Nitermax:
        x2 = (x0*f(x1)-x1*f(x0))/(f(x1)-f(x0))
        erreur = x2 - x1
        x0 = x1
        x1 = x2
        n += 1
        ern = abs(x2 - alpha)
        liste_n.append(n)
        liste_ern.append(ern)
        liste_x.append(x2)
    x = np.array(liste_n)
    y = np.array(liste_ern)
    plt.semilogy(x, y)
    plt.xlabel("valeur de n")
    plt.ylabel("valeur de ern")
    plt.title("Evolution des erreurs (Secante)")
    plt.grid()
    plt.show()   
    return liste_n, liste_ern, liste_x

"""print("-----"*10)
print("un solution de l'equation f1(x) = 0 est :")
print(Secante(f1,1,1.3,1e-6,1000,1.46491770894120))
print("-----"*10)

print("une solution de l'equation f7(x) = 0 est :")
print(Secante(f7,1,2,1e-6,1000,1.9473946913293))
print("-----"*10)"""

print("une solution de l'equation f9(x) = 0 est :")
print(Secante(f9,2,3,1e-6,1000,1.8607054167921))
print("-----"*10)

"""print("une solution de l'equation f11(x) = 0 est :")
print(Secante(f11,0,1,1e-6,1000,0.8878621503814))
print("-----"*10)"""