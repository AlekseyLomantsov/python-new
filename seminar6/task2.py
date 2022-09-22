# 2. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

# *Пример:*
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# a = ['5545', '*', '5656', '654']
# print(a)
# # a = list(map(int, a))
# # a = [int(item) for item in a if item.isdigit()]
# a = list(map(lambda x: int(x) if x.isdigit() else x, a))
# print(a)

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# res_list = [i for i in my_list if my_list.count(i) == 1]
res_list = list(filter(lambda x: my_list.count(x) == 1, my_list))
print(res_list)
