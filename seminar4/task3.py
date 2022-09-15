# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
#  этих двух чисел.
# Ответ записать в файл.


num1 = int(input('Введите число: '))
num2 = int(input('Введите число: '))

count = num1 * num2
while (num1 != num2):
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print(count / num2)