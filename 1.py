"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
- 6 -> да
- 7 -> да
- 1 -> нет
"""

a = int(input('Введите день недели: '))
if (a == 6 or a == 7):
    print("День является выходным")
elif (a <= 0 or a >= 8):
    print("Такого дня недели не существует")
else:
    print("День не является выходным")