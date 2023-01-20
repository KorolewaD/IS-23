#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Количество положительных элементов в первой половине:


# Запишем в файл pops_1.txt структуру данных - список
l = ['-9 2 -12 -37 30 4 -130 1 8 42']
f3 = open('pops_1.txt', 'w')
f3.writelines(l)
f3.close()

# Дублируем список в новый файл pops_2.txt
f4 = open('pops_2.txt', 'w')
f4.write('Исходные данные: ')
f4.write('\n')
f4.writelines(l)
f4.close()

# разбиваем строку и ее значения преобразуем в числа
f3 = open('pops_1.txt')
k = f3.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
f3.close()

# Ищем минимальный элемент и количество положительных элементов в первой половине
# в файле pops_1.txt и записываем в файл pops_2.txt
f3 = open('pops_1.txt')
min, t = 0, 0
for i in range(len(k)):
 min = min if min < k[i] else k[i]
 if k[i] > 0:
     t += 1
f4 = open('pops_2.txt', 'a') # открываем файл для дозаписи
f4.write('\n')
pol = 0
for i in k[0:int(len(k)/2)]:
    if i>0:
       pol+=1
print('Количество элементов: ', len(k), 'Количество положительных элементов: ', pol, 'Минимальный элемент: ', min, file=f4)
f4.close()

