#  1. Напишите программу, которая принимает на вход число N и 
#  выдаёт последовательность из N членов.
    
#      *Пример:*
#      - Для N = 5: 1, -3, 9, -27, 81
    

from itertools import count


n = int(input('Введите число: '))
digit = -3
count = 0
while count < n:
    print(f'{count+1}: {digit ** count}')
    count = count + 1
   

