# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;




# print(eval('1+2*3'))

# string = '1 + 2 * 3'.split()

# for i in range(len(string)):
#     if string[i].isdigit():
#         string[i] = int(string[i])
# op_1 = {'+': lambda x, y: x + y,
#         '-': lambda x, y: x - y}
# op_2 = {'*': lambda x, y: x * y,
#         '/': lambda x, y: x / y}       

# index = 0
# while '*' in string or '/' in string:
#     if string[index] in op_2:
#         temp = op_2[string[index]](string[index - 1], string[index + 1])
#         del string[index - 1: index + 2]
#         string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1

# index = 0
# while '+' in string or '-' in string:
#     if string[index] in op_1:
#         temp = op_1[string[index]](string[index - 1], string[index + 1])
#         del string[index - 1: index + 2]
#         string.insert(index - 1, temp)
#         index = 0
#     else:
#         index += 1

# print(string)

string = '(1 + (2 * 3) + 8) / (1 + (2 + (2 + 4)))'
# a = '('
b = ')'
# print(string[string.find(a)+1 :string.rfind(b)])

# index_start = -1
# while True:
#     for i in range(len(string)):
#         if string[i] == '(':
#             index_start = 1
#     if index_start == -1:
#         break
#     else:
#         index_end = string.index(')', index_start)    

index_start = []
for i in range(len(string)):
    if string[i] == '(':
        index_start.append(i)
print(index_start)
print(string[31:string.find(b)])



# print(string)