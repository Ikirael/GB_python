'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in -> out
- 6782 -> 23
- 0.67 -> 13
- 198.45 -> 27
'''
import math

a = float(input('Введите вещественное число: '))

while a-math.floor(a) > 0:
    a*=10
x = 0
while a > 0:
    x+=a%10
    a//=10
x = int(x)
print (x)