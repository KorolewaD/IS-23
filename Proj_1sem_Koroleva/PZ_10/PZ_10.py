#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр.
#Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента
#– печенье, молоко, сыр.
#Определить:
#1. в каких магазинах нельзя приобрести соль.
#2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
#3. в каких магазинах можно приобрести мясо и молоко.

Magnit = {'Молоко', 'Соль', 'Сахар', 'Печенье', 'Сыр'}
Pyaterochka = {'Мясо', 'Молоко', 'Сыр'}
Perecrestok = {'Молоко', 'Творог', 'Сыр', 'Сахар', 'Печенье'}
Lenta = {'Печенье', 'Молоко', 'Сыр'}
#1
print("Задача №1")
Salt = "Соль"
if Salt not in Magnit:
    print("В магазине Magnit отсутствует соль")
if Salt not in Pyaterochka:
    print("В магазине Pyaterochka отсутствует соль")
if Salt not in Perecrestok:
    print("В магазине Perecrestok отсутствует соль")
if Salt not in Lenta:
    print("В магазине Lenta отсутствует соль")
else:
    print("Везде есть соль")
#2
print("Задача №2")
M = "Молоко"
P = "Печенье"
S = "Сыр"
if M in Magnit and P in Magnit and S in Magnit:
    print("В магазине Magnit есть молоко, печенье и сыр")
if M in Pyaterochka and P in Pyaterochka and S in Pyaterochka:
    print("В магазине Pyaterochka есть молоко, печенье и сыр")
if M in Perecrestok and P in Perecrestok and S in Perecrestok:
    print("В магазине Perecrestok есть молоко, печенье и сыр")
if M in Lenta and P in Lenta and S in Lenta:
    print("В магазине Lenta есть молоко, печенье и сыр")
else:
    print("Нигде нет молока, печенья и сыра одновременно")
#3
print("Задача №3")
M = "Мясо"
M2 = "Молоко"
if M and M2 in Magnit:
    print("В магазине Magnit есть Мясо и Молоко")
if M and M2 in Pyaterochka:
    print("В магазине Pyaterochka есть Мясо и Молоко")
if M and M2 in Perecrestok:
    print("В магазине Perecrestok есть Мясо и Молоко")
if M and M2 in Lenta:
    print("В магазине Lenta есть Мясо и Молоко")
else:
    print("соли нет")