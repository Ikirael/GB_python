'''
 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
in
7

out
[4, 5, 3, 3, 4, 1, 2]
[5, 1, 2]
'''
import random

def RandList(num):
    lst = []
    for x in range(num):
        lst.append(random.randint(0,10))
    return lst

def UnicList(lst):
    unlst = []
    for x in range(len(lst)):
        i = 1
        for y in range(len(lst)):
            if x == y:
                continue
            if lst[x] == lst[y]:
                i = 0
                break
        if i:
            unlst.append(lst[x])
    return unlst


num = int(input("Введите кол-во элементов списка: "))
lst = RandList(num)
print(lst)
unlst = UnicList(lst)
print(unlst)

