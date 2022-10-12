"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
a = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (not (x or y or z) == (not x and not y and not z)):
                a = False
if a:
    print("Утверждение истинно для всех значений предикат")
else:
    print("Утверждение истинно не для всех значений предикат")