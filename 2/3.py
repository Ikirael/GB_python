'''
Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''
n = int(input("Введите целое число: "))
a = [round((1+1/x)**x) for x in range(1,n+1)]
print(a)

sum = 0
for x in range(n):
    sum+= a[x]
print(sum)