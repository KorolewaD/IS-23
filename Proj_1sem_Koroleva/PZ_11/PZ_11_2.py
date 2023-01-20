#Из предложенного текстового файла (text18-11.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить строку
#наименьшей длины.
import string

t = 0
d = 0
for i in open('text18-11.txt', encoding='UTF-8'):
 print(i, end='')
 t += 1
 for j in i:
    if j in string.punctuation:
        d+=1
print(end='\n')
print('Количество строк: ', t, end='\n')
print('Количество знаков препинания : ', d, end='\n')

g1_1 = open('zadanie.txt', 'w')
file = open(file='text18-11.txt', mode='r', encoding='utf-8')
teff = file.readlines()
g1_1.writelines(min([i for i in teff]))
g1_1.close()

g1_1 = open('zadanie.txt', 'r')
print('Строка наименьшей длины: ' + g1_1.read())
g1_1.close()


