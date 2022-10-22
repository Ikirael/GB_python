'''
2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
'''

def ListMult(N: int):
    return [x for x in range(20,N) if x%20 == 0 or x%21 == 0]

lst = ListMult(int(input("Введите N: ")))
print(lst)
