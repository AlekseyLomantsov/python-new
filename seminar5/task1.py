# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 4 5


# n = [1, 2, 4, 5]

# data = open('1task.txt', 'r')
# my_list = data.split('')




f1 = open('1task.txt', 'r')
output1 = f1.read()
nlist = output1.split(' ')
# print(nlist)

# for i in range(1, len(nlist)):
#     if int(nlist[i]) - 1 != int(nlist[i-1]):
#         num = int(nlist[i]) - 1
# print(num)


mylist = [int(nlist[i])-1 for i in range(1,len(nlist)) if int(nlist[i]) - 1 != int(nlist[i-1])]
print(mylist)
