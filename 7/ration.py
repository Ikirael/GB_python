from math import sqrt

def add():
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    return num1 + num2

def sub():
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    return num1 - num2

def mul():
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    return num1 * num2

def div():
    print("Operations:", "1 - /", "2 - //", "3 - %", sep='\n')
    i = int(input(": "))
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    if i == 1:
        return num1 / num2
    elif i == 2:
        return num1 // num2
    elif i == 3:
        return num1 % num2

def pow():
    num1 = float(input("num1: "))
    num2 = float(input("num2: "))
    return num1 ** num2

def sqrtt():
    num1 = float(input("num1: "))
    return sqrt(num1)
