import random
def n():
    list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', '1', '2', '3', '4', '7', '8', '5', '6', '9', 'm', 'z', 'x', 'c', 'a', 's', 'w', 'q', 'l', 'n', 'o', 'p', 'r', 's', 't', '+', '_', ')', '-', '*', '^', '%', '$','@', '!']
    i = 0
    while i <= 40:
        number = []
        a = len(list_2)
        number.append(list_2[random.randint(0, (a-1))])
        i += 1
        print(*number)

n()