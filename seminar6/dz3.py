# Напишите программу, которая найдёт 
# произведение пар чисел списка. 
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

my_list = [2, 3, 4, 5, 6]

if (len(my_list) % 2) == 0:
    res = list(map(lambda x: my_list[x] * my_list[len(my_list)-1-x], range(len(my_list)//2)))
else:
    res = list(map(lambda x: my_list[x] * my_list[len(my_list)-1-x], range(len(my_list)//2+1)))

print(res)