#Дан список A размера N (N — четное число). Вывести его элементы с четными
#номерами в порядке возрастания номеров: A2, A4, A6, ..., AN. Условный оператор не
#использовать
import random
print('Введите размер списка: ')
N= int(input())
list_1 = [random.randint(1, N) for i in range(1, N + 1)]
list_2 = list_1[0:len(list_1):2] #Перечисление четных элементов
list_2.sort()
print('Готово: ', list_2)
