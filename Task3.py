from colorama import init
from colorama import Fore, Back, Style
print( Back.GREEN )
N = input("ведите количесвтво людей в стране ")
N1 = int(N)
L = 0								#В коде присутствует модуль Colorama 
M = 0								#Код скомпилирован в одноимённое приложение 
F = 0
if (int(N) % 2) == 0:                           
    print(N)
else:
    N=int(N) - 1
while int(N) > 0:
    import random
    r = random.randint(0, 1)
    if r == 0:
        F = F + 1
        L = L + 1
        print( Back.MAGENTA)
        print("детей рождено: " + str(L) + " | Из них мальчиков: " + str(M))
    else:
        M = M + 1
        N = int(N) - 2
        L = L + 1
        print("Детей рождено: " + str(L) + " | Из них мальчиков: " + str(M))
N1 = N1 + L
if (N1 % 2) == 0:
    N2 = N1 / 2
else:
    N2 = (N1 - 1) / 2
print( Back.WHITE )
print( Fore.BLACK )
print("Численность населения после = " + str(N1))
G = (F + N2) / (M + N2)
Z = F + N2
X = M + N2
print("отношение количества женщин(" + str(Z) +") к мужчинам (" + str(X) +") = " + str(G))
input( )