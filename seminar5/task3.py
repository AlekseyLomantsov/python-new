# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавабв'
# 'Мы очень любим Питон'


from re import sub


my_str = 'Мы неабв очень любим Питон иабв Джавабв'
sub_str = 'абв'

my_list = my_str.split()
print(my_list)

# i = 0
# while i in range(len(my_list)):
#     if sub_str in my_list[i]:
#         my_list.remove(my_list[i])
#     else:      
#         i += 1
# print(my_list)

list3 = [item for item in my_list if sub_str not in item]    
print(list3)
