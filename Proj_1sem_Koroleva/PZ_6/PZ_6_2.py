#Дано число R и список A размера N. Найти элемент списка, который наиболее близок
#к числу R (то есть такой элемент AK, для которого величина |AK - R| является
#минимальной).
A = [1,3,4,2,6,8,22,40,35,9,7,68,90,55,32,15,93,100,102,145,298,244,385,678,978,1223]
print('Введите число: ')
R = int(input())
i = 0
z = []
while i < len(A)-1:
    B = abs(A[i]-R)
    z.append(B)
    i = i + 1
print(abs(min(z) - R))