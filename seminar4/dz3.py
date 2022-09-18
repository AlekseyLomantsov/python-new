# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


my_list = [1, 1, 2, 3, 4, 5, 5] # для данного списка решение подойдет, в другом случае - отсортировать
list_add_ = []
print(my_list)
# [list_add_.append(i) for i in my_list if i not in list_add_] # не то, оставлю для себя
i = 0
while i < len(my_list):
    if my_list[i-1] != my_list[i] != my_list[i+1]:
        list_add_.append(my_list[i])
    i +=1

print(list_add_)

