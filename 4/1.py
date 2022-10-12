'''
Вычислить число c заданной точностью d
in
Enter a real number: 9
Enter the required accuracy '0.0001': 0.000001

out
9.000000
'''

def AccuracyNumber(number, accuracy) -> float:
    i = 0
    while(accuracy != 1):
        i+=1
        accuracy *= 10
    print(format(number, f".{i}f"))

num = float(input("Enter a real number: " ))
acc = float(input("Enter the required accuracy '0.0001': "))
AccuracyNumber(num, acc)
