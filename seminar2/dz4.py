# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.


my_list = []
n = int(input('Введите N: '))
i = -n
while i <= n:
    my_list.append(i)
    i = i + 1
print(my_list)

list_index = []
for element in input().split():
    list_index.append(int(element))

sum_num = 0
for item in my_list: #/ не работает
    if list_index in my_list:
        sum_num = sum_num + my_list[item]
print(sum_num)

