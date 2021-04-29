""" Julie Fischer Frederique Bergez Ma123
    Methode de la dichotomie"""
    
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

def Dichotomie(f, a0, b0, epsilon, Nitermax,alpha):
    c = 0
    a = a0
    b = b0
    n = 0
    liste_n = []
    liste_ern = []
    liste_x = []
    while abs(b-a)>epsilon and n<= Nitermax:
        c = (a + b)/2
        n = n + 1
        ern = abs(c - alpha)
        if (f(a)*f(c) <= 0) :
            b = c
        else:
            a = c
        liste_n.append(n)
        liste_ern.append(ern)
        liste_x.append(c)
    x = np.array(liste_n)
    y = np.array(liste_ern)
    plt.semilogy(x, y)
    plt.xlabel("valeur de n")
    plt.ylabel("valeur de ern")
    plt.title("Evolution des erreurs (dicho)")
    plt.grid()
    plt.show()
    return liste_n, liste_ern, liste_x

"""print("-----"*10)
print("une solution de l'équation f1(x) = 0 est :")
print(Dichotomie(f1,1,2,1e-6,1000,1.46491770894120))
print("-----"*10)

print("une solution de l'équation f7(x) = 0 est :")
print(Dichotomie(f7,1,2,1e-6,1000,1.9473946913293))
print("-----"*10)"""

print("une solution de l'équation f9(x) = 0 est :")
print(Dichotomie(f9,2,3,1e-6,1000,1.8607054167921))
print("-----"*10)

"""print("une solution de l'équation f11(x) = 0 est :")
print(Dichotomie(f11,0,1,1e-6,1000,0.8878621503814))
print("-----"*10)"""