# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12





my_list = [2, 3, 5, 9, 3]

def min_index(my_list):
    min_sum = 0
    for i in range(1, len(my_list), 2):
        min_sum += my_list[i]
    return min_sum

print(min_index(my_list))

