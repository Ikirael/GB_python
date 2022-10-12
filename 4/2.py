'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Простые делители числа

in
54

out
[2, 3, 3, 3]
'''

def PrimeList(num):
    i = 2
    lst = []
    while(i != num):
        if (num % i == 0):
            lst.append(i)
            num /= i
        else:
            i+=1
    lst.append(i)
    return lst

num = int(input("Natural number: "))
lst = PrimeList(num)
print(lst)

