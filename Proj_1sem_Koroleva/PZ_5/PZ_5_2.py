import random #Импортирование библиотеки рандом
def SortInc3(A,B,C): #Создание функции
    L = []
    if A > B: #Условие
        A,B = B,A
    if B > C: #Условие
        B,C = C,B
    if A > B: #Условие
        A,B = B,A
    L.append(A)  #Добавление в конец списка значения поодиночке
    L.append(B)
    L.append(C)
    return L
A = random.randrange(-10,10) #Выбор различного числа из диапазона
B = random.randrange(-10,10) #Выбор различного числа из диапазона
C = random.randrange(-10,10) #Выбор различного числа из диапазона
print("{0}, {1}, {2}".format(A,B,C)) #Вывод значений 1-го ряда
A,B,C = SortInc3(A,B,C)
print("{0}, {1}, {2}".format(A,B,C)) #Вывод значений 2-го ряда
A = random.randrange(-10,10) #Выбор различного числа из диапазона
B = random.randrange(-10,10) #Выбор различного числа из диапазона
C = random.randrange(-10,10) #Выбор различного числа из диапазона
print("{0}, {1}, {2}".format(A,B,C)) #Вывод значений 3-го ряда
A,B,C = SortInc3(A,B,C)
print("{0}, {1}, {2}".format(A,B,C)) #Вывод значений 4-го ряда