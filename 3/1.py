'''
Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
in
5

out
[10, 2, 3, 8, 9]
22
'''

import random
n = int(input("Введите кол-во элементов: "))
arr = [random.randrange(10) for x in range(n)]
print (arr)
sum = 0
for x in range(0,n,2):
    sum+=arr[x]
print(sum)