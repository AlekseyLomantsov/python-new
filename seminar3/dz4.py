# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное (без встроенных функций).

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = 45
def bin_num(num):
    if num == 0: return [0]
    result = []
    while num:
        result.append(num%2)
        num //= 2
    return result[::-1]

def print_num(num):
    for i in num:
        print(i, end = '')
    
res = bin_num(num)
print_num(res)



