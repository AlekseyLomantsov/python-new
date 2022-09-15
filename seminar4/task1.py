# 1. Задайте строку из набора чисел. Напишите программу, 
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.




def list_add(ourstr):
    num = []
    # for i in range(len(ourstr)):
    #     num.append(int(ourstr[i]))
    for i in ourstr:
        num.append(int(i))
    
    return num


ourstr = input('Введите цифры через пробел: ').split(' ')
num = list_add(ourstr)
print(num)
print(f'Минимальное значние: {min(num)};\nМаксимальное значение: {max(num)}')