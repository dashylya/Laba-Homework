m = input("введите количество команд ")
import math
a = ( math.factorial(int(m)) )
b = ( math.factorial((int(m) - 3)) )
f = a / b
print("Вариантов распредлеления команд на первые 3 места = " + str(f))
print("Bсего возможных комбинаций распределения команд по всем местам = " + str(a))
