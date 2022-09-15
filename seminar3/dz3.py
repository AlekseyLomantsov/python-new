# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным 
# значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19



my_list = [1.1, 1.2, 3.1, 10.01]

def min_max(my_list):
    min = 1
    max = 0
    for i in my_list:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)  
    return (max - min)
    
res = min_max(my_list)
print('%.2f'% (res))
