#Дан список размера N. Осуществить сдвиг элементов списка влево на одну позицию
#(при этом AN перейдет в AN-1, AN-1 — в AN-2, .., A2 — в A1, a исходное значение
#первого элемента будет потеряно). Последний элемент полученного списка
#положить равным 0
import random
N = random.randrange(3,21)
print("N = ", N)
a = [i for i in range(N)]
print("Array:\n", a)
print("Modified Array 1:\n", a[1:] + [0])
for i in range(0,N-1):
    a[i] = a[i+1]
a[N-1] = 0
print("Modified Array 2:\n", a)