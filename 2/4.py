'''
Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
-> 15
'''
x1 = int(input("Position one: "))
x2 = int(input("Position two: "))
n = int(input("Number of elements:"))
arr = [x for x in range(-n,n+1)]
print (arr)
res = arr[x1-1]*arr[x2-1]
print(res)