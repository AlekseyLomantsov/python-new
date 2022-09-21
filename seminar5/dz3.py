# 3. Создайте программу для игры в ""Крестики-нолики"".



from collections import OrderedDict


def board_print(board):
    print('-------------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-------------')  

def input_player(player_item):
    flag = False
    while not flag:
        input_item = input(f'Куда ставть {player_item}?')
        try:
            input_item = int(input_item)
        except:
            print(f'Введите цифру от 1 до 9')
            continue
        if input_item >= 1 and input_item <= 9:
            if str(board[input_item - 1]) not in 'XO':
                board[input_item - 1] = player_item
                flag = True
            else:
                print('Эта клетка занята')
    
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for item in win_coord:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False

def game_base(board):
    count_ = 0
    win = False
    while not win:
        board_print(board)
        if count_ % 2 == 0:
            input_player('X')
        else:
            input_player('O')
        count_ += 1
        if count_ > 4:
            temp = check_win(board)
            if temp:
                print(f'{temp} Выграл!')
                win = True
                break
        if count_ == 9:
            print('Ничья')
            break
    board_print(board)


board = list(range(1, 10))
game_base(board)


