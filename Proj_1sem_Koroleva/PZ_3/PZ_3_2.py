#Дано целое число, лежащее в диапазоне 1-999. Вывести его строку- описание вида
#«четное двузначное число», «нечетное трехзначное число» и т. д.
i = int(input('Введите число: ')) #Введение числа
if i % 2 == 0: #Если число делится без остатка на 2, то
    ans = "четное" #вывод
else:  #Если число не делится без остатка на 2, то
    ans = "нечетное" #вывод
if len(str(i)) == 1: #Если длина числа 1, то
    ans2 = "однозначное" #вывод
elif len(str(i)) == 2: #Если длина числа 2, то
    ans2 = "двухзначное" #вывод
elif len(str(i)) == 3: #Если длина числа 3, то
    ans2 = "трехзначное" #вывод
print(ans2, ans) #Вывод конечных значений