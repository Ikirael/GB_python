'''
1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
in
9

out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]
'''
import random

def CreateRandList(n: int):
    return [random.randrange(100) for i in range(n)]

def CreateMoreList(lst: list):
     return [lst[x] for x in range(1,len(lst)) if lst[x-1] < lst[x]]

lst = CreateRandList(int(input("Введите кол-во элементов: ")))
print(lst) 
lst = CreateMoreList(lst)
print(lst)  
