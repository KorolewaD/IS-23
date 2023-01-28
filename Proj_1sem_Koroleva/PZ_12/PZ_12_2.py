#Из заданной строки отобразить только символы пунктуации. Использовать
#библиотеку string.
#Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"
u = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'
import string
for i in u:
   if i in string.punctuation:
     print(i, end = "")