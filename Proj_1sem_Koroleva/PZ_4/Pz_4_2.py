print('Введите число: ') #Ввод числа
N = int(input())
k = 0 #Присваивание значения
p = 1 #Присваивание значения
while p <= N: #Цикл
    p *= 3 #Перемножает значения обеих сторон, затем присваивает правое левому
    k += 1 #Присваивание выражению слева суммированное значение обеих сторон
print("k = {0}, 3^k = {1}, 3^(k-1) = {2}".format(k,3**k,3**(k-1))) #Вывод конечных значений и форматирование строк