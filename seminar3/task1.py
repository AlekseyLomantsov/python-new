# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора 
# псевдослучайных чисел.
import time

# sec = str(time())
# count = 0
# num = sec[-1]
# print(num)

for i in range(1):
    a = time.time()
    print((int(a * 1000000))% 100)
