import time

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]

def print_board():
    print(board[:3])
    print(board[3:6])
    print(board[6:])

def win_check(board: list, sign: str) -> bool:
    """
    Проверка победы

    Эта функция принимает игровое поле, метку и проверяет есть ли победитель.
    Победой является равенство 3ех ячеек и метки: по вертикали, по горизонтали и диагонали.

    :param board: Проверяемое игровое поле
    :param sign: Метка игрока, сделавшего ход.
    :return: True если есть победная комбинация, False если её нет.
    """
    for i in range(3): #по горизонтали
        if board[(i-1)*3] == board[1+(i-1)*3] == board[2+(i-1)*3] == sign:
            return True
    for j in range(3): #по вертикали
        if board[j-1] == board[j+2] == board[j+5] == sign:
            return True
    if board[::4].count(sign) == 3: #по диагонали
        return True
    elif board[2:7:2].count(sign) == 3: #по диагонали
        return True
    else:
        return False

def play_time(func):
    """Декоратор замеряющий продолжительность игры."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Длительность игры: {int(end - start)} секунд")
        return result
    return wrapper

@play_time
def main_loop():
    turns = 0
    player = 'Первый'
    sign = 'X'
    while True:
        print_board()
        print()
        try:
            turn = int(input(f'{player} игрок введите порядковый номер ячейки("0" для выхода из игры): '))
            print()
            if turn == 0:
                print('Игра завершена.')
                break
            if turn < 0:
                print('Ошибка: некорректный ввод')
                continue
            if board[turn-1] != '-':
                print('Ячейка уже занята. Выберете другую.')
                continue
            else:
                turns += 1
                board[turn-1] = sign
            if win_check(board, sign):
                print_board()
                print(f'Игра закончена: {player} игрок победил!')
                break
            if turns == 9:
                print_board()
                print('Игра закончена: ничья')
                break
            sign = 'O' if turns % 2 != 0 else 'X'
            player = 'Первый' if turns % 2 == 0 else 'Второй'
        except (ValueError, IndexError): #проверка ввода: тип данных и выход за пределы границы(индекс >9)
            print('Ошибка: некорректный ввод')
            continue

print('''
Добро пожаловать в игру "Крестики-нолики"
Ячейки пронумерованы по порядку как показано ниже:
['1', '2', '3']
['4', '5', '6']
['7', '8', '9']
Первый игрок = X 
Второй игрок = O \n''')

time.sleep(1)

main_loop()