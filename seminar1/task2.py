# 2. Напишите программу, которая на вход принимает 5
# чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# range(5)  [0,1,2,3,4]
# range(6,16) [6,7,8,9, ... , 15]
my_list = []
for i in range(5):
    num = int(input('--> '))
    my_list.append(num)
maxx = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > maxx:
        maxx = my_list[i]
        maxx_i = i

# print(max(my_list))

# for item in my_list[1:]:
#     if item > maxx:
#         maxx = item
print(maxx, maxx_i)
