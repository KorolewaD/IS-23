print('Введите число N: ')
N = int(input())
s = 1.0
for i in range (1, N + 1):
    s = s * (1.0 / i)
print ("Произведение равно: ", s)