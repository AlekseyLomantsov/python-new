# 2. Задайте список. Напишите программу, 
# которая определит, присутствует ли в заданном 
# списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"


# my_list = ['65h34q', 'sdg634d', '147jnbv']
# n = '7'
# for i in my_list:
#     if i.find(n) >= 0:
#         print(i)
#     else:
#         print('none')

# listt = ["65h34q", "sdg634d", "147jnbv"]

# result = [i for i in listt if '7' in i]
# print(result)
# if len(result) > 0:
#     print(True)
# else:
#     print(False)

n = 'h'
mylist = ['jh', 'sdhfogf', 'kjahsd', '24', 'dpo', '7']
def find_number(n, lst):
    res = []
    for i in lst:
        if n in i:
            res.append(i)
    return res
print(find_number(n, mylist))