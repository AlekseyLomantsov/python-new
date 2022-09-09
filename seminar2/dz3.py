# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input('Введите число: '))
list1 = []
sum = 0
for i in range(1, k + 1):
    list1.append((1+1/i)**i)
print(list1)
for i in range(len(list1)):
    sum = sum + list1[i]
print(sum)