#Дано целое число N (>0). Найти произведение 1.1 • 1.2 • 1.3 •... (N сомножителей)
print('Введите число N: ') #Ввод числа
N = int(input())
s = 1.0 #Присваивание значения s
for i in range (1, N + 1): #Цикл от 1 до N+1
    s = s * (1.0 / i) #Нахождение произведения N сомножителей
print ("Произведение равно: ", s) #Вывод конечных значений