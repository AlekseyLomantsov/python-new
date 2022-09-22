# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import count

def rle(stringg):
    count = 1
    temp = ''
    result = ''

    for item in stringg:
        if item != temp:
            if temp:
                result += str(count) + temp
            count = 1
            temp = item
        else:
            count += 1
    result += str(count) + temp
    return result

def rle_decode(read_str):
    count = ''
    result = ''
    for item in range(len(read_str)):
        if read_str[item].isdigit():
            count += read_str[item]
        else:
            result += read_str[item] * int(count)
            count = ''
    return result


with open('dz4_read.txt', 'r') as stringg: # прочитал для rle
    read_str = stringg.read()

with open('dz4_write.txt', 'w') as read_str_file: # записал rle
    read_str_file.write(rle(read_str))

with open('dz4_write.txt', 'r') as r_str: # прочитал для rle_decode
    dec_str = r_str.read()

print(rle(read_str))
print(rle_decode(dec_str))


         
