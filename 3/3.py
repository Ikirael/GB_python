'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Без использования встроенной функции преобразования, без строк.
in
88
out
1011000
'''

a = int(input("Введите десятичное число: "))
arr = []
while a > 0:
    arr.append(a%2)
    a//=2
print (arr)
b = 0

for x in range (len(arr)-1, 0, -1):
    b += arr[x]
    b*=10
print(b)
    

