# 2. Напишите программу, которая будет принимать на вход 
# дробь и показывать первую цифру дробной части числа.

# *Примеры:*

# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

number = float(input("Input number: "))
# print(number.split('.')[1][0])
number *= 10
number = int(number)
print(number % 10)
