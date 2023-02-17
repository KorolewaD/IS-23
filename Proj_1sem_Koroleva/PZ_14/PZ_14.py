# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857
# год и поместить ее в новый текстовый файл.
import re #Импорт библиотеки

a = open(file='Dostoevsky.txt', mode='r', encoding='utf-8') #Открытие файла
text = a.read()
p = re.findall(r"[1][8][5][7]\D+", text) #Поиск необходимых данных
print("Загляните в файл NewFile!)")
a.close()
f = open('NewFile', 'w') #Открытие файла для записи
f.writelines(p) #Добавление в файл необходимой информации
f.close()