# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


print('Введите день недели цифрой, что бы узнать выходно ли это?')
num = int(input())
if num == 1:
    print('Нет, понеделник это рабочий день')
elif num == 2:
    print('Нет, вторник это рабочий день')
elif num == 3:
    print('Нет, среда это рабочий день')
elif num == 4:
    print('Нет, четверг это рабочий день')
elif num == 5:
    print('Нет, пятница это рабочий день')
elif num == 6:
    print('Да, суббота это выходной день день')
elif num == 7:
    print('Да, воскресенье это выходной день')
else:
    print('Нужно вводить число от 1 до 7')


