#В последовательности на n целых чисел найти и вывести:
#1. минимальный среди положительных
#2. элементы кратные пяти
#3. их среднее арифметическое
a = [-1, 2, 6, 45, 87, 95, 9, -65, 5]
print("Минимальное среди положительных: ", min(filter(lambda val: val > 0, a)))
b = (list(filter(lambda x: x % 5 == 0, [-1, 2, 6, 45, 87, 95, 9, -65, 5])))
print("Элементы кратные пяти: ", b)
print("Среднее арифметическое чисел кратных пяти: ", sum(b)/len(b))