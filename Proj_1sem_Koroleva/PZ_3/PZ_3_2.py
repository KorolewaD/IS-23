i = int(input( "Введите число: " ))
for i in range(1, 999):
   if i%2 == 0:
       ans = "четное"
   else:
       ans = "нечетное"
   if len(str(i)) == 1:
       ans2 = "однозначное"
   elif len(str(i)) == 2:
       ans2 = "двухзначное"
   elif len(str(i)) == 3:
       ans2 = "трехзначное"
print(ans2, ans)
