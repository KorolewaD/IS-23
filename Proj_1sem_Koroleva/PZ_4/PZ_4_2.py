print('Введите число: ')
N = int(input())
k = 0
p = 1
while p <= N:
    p *= 3
    k += 1
print("k = {0}, 3^k = {1}, 3^(k-1) = {2}".format(k,3**k,3**(k-1)))