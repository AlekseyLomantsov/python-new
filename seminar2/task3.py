# 3. Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.

# *Пример:*
# 'Я люблю Питон!'
# 'лю'

# первый вариант
# a = input("Введите строку: ")
# b = input("Введите искомую подстроку: ")
# count = 0
# for i in range(0, len(a)-1):
#     if a[i] + a[i+1] == b:
#         count += 1
# print(f"{count} раз")

# второй вариант
# for i in range(0, len(a) - len(b)):
#     if b == a[i:i + len(b)]:
#         count += 1
# print(f"{count} раз")

# третий вариант
a = input("Введите строку: ")
b = input("Введите искомую подстроку: ")

res = a.count(b)
print(res)