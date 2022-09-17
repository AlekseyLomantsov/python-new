# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]


# пока число четное делить на 2



def check(num):
    if num % 2 == 0 or num % 3 == 0:
        return num
    else:
        print('Это простое число!')

def add_list_int(num):
    list_int = []
    count_ = 0
    while num > 1:
        if num % 2 == 0:
            num /= 2
            count_ = 2
            list_int.append(count_)
        elif num % 3 == 0:
            num /= 3
            count_ = 3
            list_int.append(count_)
        else:
            list_int.append(int(num))
            num /= num
    return list_int


num = int(input('Введите натуральное число: '))
check_num = check(num)
print(add_list_int(check_num))

