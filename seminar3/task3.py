# 3. Напишите программу, которая определит 
# позицию второго вхождения строки в списке либо 
# сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


# my_list = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# n = 'qwe'
# my_list = ['йцу', 'фыв', 'ячс', 'цук', 'йцукен', 'йцу']
# n = 'йцу'
my_list = ["123", "234", 123, "567"]
n = "123"
count_ = 0
for i in range(0, len(my_list)):
    if my_list[i] == n:
        count_ += 1
        if count_ == 2:
            print(i)
            break
if count_ < 2:
    print('-1')
