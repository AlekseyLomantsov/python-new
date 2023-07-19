import csv

def add_info():
    name = input("Имя: ")
    phone = input("Телефон: ")
    newLine = [name, phone]
    with open('data.csv', 'a', newline = '') as data:
        writer = csv.writer(data, delimiter = ';')
        writer.writerow(newLine)

def find_num():
    name = input("Имя: ")
    with open ('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            if name == row[0]:
                print(*row)

def show_all():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            print('{:<15} {:<15}'.format(*row))

def delete_item():
    name = input('Какую запись удалить? ')
    temp_list=[]
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            temp_list.append(row)
    for item in temp_list:
        if name in item:
            temp_list.remove(item)
            print('Запись удалена')
            break
    with open('data.csv', 'w') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(temp_list)

