'''
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
in
4

out
[2, 5, 8, 10]
[20, 40]
'''

import random
n = int(input("Введите кол-во элементов: "))
arr = [random.randrange(10) for x in range(n)]
print (arr)

mul = []
for x in range(n//2):
    
    mul.append(arr[x]*arr[n-x-1])
if n%2 == 1:
    mul.append(arr[n//2]**2)
print(mul)