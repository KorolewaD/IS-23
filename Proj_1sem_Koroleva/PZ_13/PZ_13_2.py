# В матрице найти сумму элементов второй половины матрицы.

import random
import numpy as np

m = random.randint(2, 4)
n = random.randint(2, 4)
lst = np.random.randint(-12, 21, (n, m))
print("Матрица:\n", lst)
count = sum(lst[i][j] for i in range(len(lst)//2, len(lst)) for j in range(len(lst[0])))
print("Сумма элементов второй половины матрицы:\n",  count)
