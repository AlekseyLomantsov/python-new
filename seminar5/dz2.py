# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""



##### Против игрока
from random import randint


def input_sweets(name):
    x = int(input(f'{name}, введите количество конфет, которое хотите взять(от 1 до 28) = '))
    while x < 1 or x > 28:
        x = int(input(f'{name}, введите корректное количество конфет(от 1 до 28) = '))
    return x

def draw_player(dice1,dice2):
    draw = True
    while draw:
        if dice1 > dice2:
            print(f'Игрок {player1}, ходит первый.')
            draw = False
        if dice1 < dice2:
            print(f'Игрок {player2}, ходит первый.')
            break
    return draw

def print_sw(player, input_sw, couters, sweets):
    print(f'{player}, взял {input_sw}, теперь у него {couters} конфет, а на столье осталось {sweets} конфет.')

player1 = input('Введите имя первого игрока и кидайте кости: ')
dice1 = randint(1,6)
print(dice1)

player2 = input('Введите имя второго игрока и кидайте кости: ')
dice2 = randint(1,6)
print(dice2)

draw = draw_player(dice1,dice2)
sweets = 2021

couters1 = 0
couters2 = 0

while sweets > 28:
    if draw:
        input_sw = input_sweets(player1)
        couters1 = input_sw
        sweets -= input_sw
        draw = False
        print_sw(player1, input_sw, couters1, sweets)
    else:
        input_sw = input_sweets(player2)
        couters2 = input_sw
        sweets -= input_sw
        draw = True
        print_sw(player2, input_sw, couters2, sweets)

if draw:
    print(f'{player1} выграл!')
else:
    print(f'{player2} выграл!')






