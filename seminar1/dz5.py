# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

from re import X


xyz = []
for i in range(3):
    xyz.append(input('Введите число: '))

if not(xyz[0] and xyz[1] and xyz[2]) == (not xyz[0] and not xyz[1] and not xyz[2] ):
    print(True)
else:
    print(False)