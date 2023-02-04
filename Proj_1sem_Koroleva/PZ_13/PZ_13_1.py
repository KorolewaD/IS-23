# В матрице найти сумму и произведение элементов строки N (N задать с клавиатуры).

import random
import numpy as np

m = random.randint(2, 5)
n = random.randint(2, 5)
lst = np.random.randint(-10, 15, (n, m))
print('Матрица:\n', lst)
N = int(input("Введите номер строки сумму и произведение элементов которой вы хотите найти: "))
print(f"Сумма элементов: {sum(lst[N-1])}")
s = 1
for i in lst[N-1]:
    s *= i
print(f"Произведение элементов:", s)
