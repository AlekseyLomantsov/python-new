# Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11


from turtle import right


num = input('Введите число: ')
sep = num.split('.')
left_ = int(sep[0])
right_ = int(sep[1])
sum = 0

while (left_ != 0):
    sum = sum + left_ % 10
    left_ = left_ // 10
while (right_ != 0):
    sum = sum + right_ % 10
    right_ = right_ // 10
print(f'Сумма цифр = {sum}')


