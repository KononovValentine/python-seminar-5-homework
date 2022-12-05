from random import randint


# Задача 1 Напишите программу, удаляющую из текста все слова, содержащие "" абв "".

def ProgramOne():
    print()
    string = 'Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.' \
             'Первый абв ход определяется жеребьёвкой. За один абводин ход можно забрать не более чем 28 конфет.' \
             'Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взяабвть взять ' \
             'первому игроку, чтобы забрать все конфеты у абвсвоего своего конкурента?'

    finalString = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, string.split()))

    print(f'Изначальный текст: {string}')
    print(f'Текст в результате: {" ".join(finalString)}')
    MainProgram()


# Задача 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота "" интеллектом ""

def ProgramTwo():
    while True:
        p2p = int(input('Введите 1, чтобы играть против другого игрока или 2, чтобы играть против бота: '))
        if p2p == 1 or p2p == 2:
            break

    def getValueCandys():
        while True:
            value = int(input('Введите количество конфет которые хотите взять, но не более 28: '))
            if value <= 28:
                print('Введите меньше 28')
                break
        return value

    def printInfo(player, value, all, steelHave):
        print(f'Сходил игрок {player}, он взял {value}, теперь у него {all}, на столе осталось {steelHave}')

    player = True
    candys = 2021
    playerOneCount = 0
    playerTwoCount = 0

    while candys > 28:
        if player == True:
            print('Ходит игрок 1')
            value = getValueCandys()
            playerOneCount += value
            candys -= value
            printInfo(1, value, playerOneCount, candys)
            player = False
        else:
            print('Ходит игрок 2')
            if p2p == 1:
                value = getValueCandys()
                playerTwoCount += value
                candys -= value
                printInfo(2, value, playerTwoCount, candys)
                player = True
            elif p2p == 2:
                move = candys % 29
                if move == 0:
                    move = randint(1, 29) if candys >= 28 else candys
                playerTwoCount += move
                candys -= move
                printInfo(2, move, playerTwoCount, candys)
                player = True

    if player == True:
        print('Победил игрок 1')
    else:
        print('Победил игрок 2')
    MainProgram()


# Задача 3 Создайте программу для игры в""Крестики - нолики"".

def ProgramThree():
    player = 'X'

    def printBoard(winner):
        if winner == 0:
            print(board[0])
            print(board[1])
            print(board[2])
        elif winner == 1 or winner == 9:
            print(f"[\033[92m'{board[0][0]}'\033[0m, \033[92m'{board[0][1]}'\033[0m, \033[92m'{board[0][2]}'\033[0m]")
            print(f"['{board[1][0]}', '{board[1][1]}', '{board[1][2]}']")
            print(f"['{board[2][0]}', '{board[0][1]}', '{board[2][2]}']")
        elif winner == 2 or winner == 10:
            print(f"['{board[0][0]}', '{board[0][1]}', '{board[0][2]}']")
            print(f"[\033[92m'{board[1][0]}'\033[0m, \033[92m'{board[1][1]}'\033[0m, \033[92m'{board[1][2]}'\033[0m]")
            print(f"['{board[2][0]}', '{board[0][1]}', '{board[2][2]}']")
        elif winner == 3 or winner == 11:
            print(f"['{board[0][0]}', '{board[0][1]}', '{board[0][2]}']")
            print(f"['{board[1][0]}', '{board[1][1]}', '{board[1][2]}']")
            print(f"[\033[92m'{board[2][0]}'\033[0m, \033[92m'{board[2][1]}'\033[0m, \033[92m'{board[2][2]}'\033[0m]")
        elif winner == 4 or winner == 12:
            print(f"[\033[92m'{board[0][0]}'\033[0m, '{board[0][1]}', '{board[0][2]}']")
            print(f"[\033[92m'{board[1][0]}'\033[0m, '{board[1][1]}', '{board[1][2]}']")
            print(f"[\033[92m'{board[2][0]}'\033[0m, '{board[0][1]}', '{board[2][2]}']")
        elif winner == 5 or winner == 13:
            print(f"['{board[0][0]}', \033[92m'{board[0][1]}'\033[0m, '{board[0][2]}']")
            print(f"['{board[1][0]}', \033[92m'{board[1][1]}'\033[0m, '{board[1][2]}']")
            print(f"['{board[2][0]}', \033[92m'{board[0][1]}'\033[0m, '{board[2][2]}']")
        elif winner == 6 or winner == 14:
            print(f"['{board[0][0]}', '{board[0][1]}', \033[92m'{board[0][2]}'\033[0m]")
            print(f"['{board[1][0]}', '{board[1][1]}', \033[92m'{board[1][2]}'\033[0m]")
            print(f"['{board[2][0]}', '{board[0][1]}', \033[92m'{board[2][2]}'\033[0m]")
        elif winner == 7 or winner == 15:
            print(f"[\033[92m'{board[0][0]}'\033[0m, '{board[0][1]}', '{board[0][2]}']")
            print(f"['{board[1][0]}', \033[92m'{board[1][1]}'\033[0m, '{board[1][2]}']")
            print(f"['{board[2][0]}', '{board[0][1]}', \033[92m'{board[2][2]}'\033[0m]")
        elif winner == 8 or winner == 16:
            print(f"['{board[0][0]}', '{board[0][1]}', \033[92m'{board[0][2]}'\033[0m]")
            print(f"['{board[1][0]}', \033[92m'{board[1][1]}'\033[0m, '{board[1][2]}']")
            print(f"[\033[92m'{board[2][0]}'\033[0m, '{board[0][1]}', '{board[2][2]}']")
        elif winner == 17:
            print(f"[\033[92m'{board[0][0]}'\033[0m, '{board[0][1]}', \033[92m'{board[0][2]}'\033[0m]")
            print(f"[\033[92m'{board[1][0]}'\033[0m, \033[92m'{board[1][1]}'\033[0m, \033[92m'{board[1][2]}'\033[0m]")
            print(f"[\033[92m'{board[2][0]}'\033[0m, '{board[0][1]}', \033[92m'{board[2][2]}'\033[0m]")

    def changePlayer(player):
        if player.lower() == 'x':
            return '0'
        else:
            return 'X'

    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def exception(n):
        if n == 1:
            print('Позиция уже занята')
        elif n == 2:
            print('Выбрана неверная позиция')

    def playerChoice(choice):

        if choice == 1:
            if board[0][0] == '-':
                board[0][0] = player
            else:
                exception(1)
        elif choice == 2:
            if board[0][1] == '-':
                board[0][1] = player
            else:
                exception(1)
        elif choice == 3:
            if board[0][2] == '-':
                board[0][2] = player
            else:
                exception(1)
        elif choice == 4:
            if board[1][0] == '-':
                board[1][0] = player
            else:
                exception(1)
        elif choice == 5:
            if board[1][1] == '-':
                board[1][1] = player
            else:
                exception(1)
        elif choice == 6:
            if board[1][2] == '-':
                board[1][2] = player
            else:
                exception(1)
        elif choice == 7:
            if board[2][0] == '-':
                board[2][0] = player
            else:
                exception(1)
        elif choice == 8:
            if board[2][1] == '-':
                board[2][1] = player
            else:
                exception(1)
        elif choice == 9:
            if board[2][2] == '-':
                board[2][2] = player
            else:
                exception(1)
        else:
            exception(2)

    def checkWin():
        if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
            return 'Победил игрок X', 1
        elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
            return 'Победил игрок X', 2
        elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
            return 'Победил игрок X', 3
        elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
            return 'Победил игрок X', 4
        elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
            return 'Победил игрок X', 5
        elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
            return 'Победил игрок X', 6
        elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
            return 'Победил игрок X', 7
        elif board[2][2] == 'X' and board[1][1] == 'X' and board[0][0] == 'X':
            return 'Победил игрок X', 8
        elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
            return 'Победил игрок 0', 9
        elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
            return 'Победил игрок 0', 10
        elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
            return 'Победил игрок 0', 11
        elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
            return 'Победил игрок 0', 12
        elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
            return 'Победил игрок 0', 13
        elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
            return 'Победил игрок 0', 14
        elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
            return 'Победил игрок 0', 15
        elif board[2][2] == '0' and board[1][1] == '0' and board[0][0] == '0':
            return 'Победил игрок 0', 16
        elif '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
            return 'Ничья', 17
        else:
            return '', 0

    while True:
        printBoard(0)
        print('Ход игрока', player)
        choice = int(input('Введите выбранное свободное место (1-9): '))
        playerChoice(choice)

        winner = str(checkWin()[0])
        if winner == 'Победил игрок X' or winner == 'Победил игрок 0' or winner == 'Ничья':
            print('\033[92m', winner, '\033[0m')
            printBoard(checkWin()[1])
            break

        player = changePlayer(player)
    MainProgram()


# Задача 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def ProgramFour():

    def encoding(string):
        result = ''
        prevChar = ''
        count = 1
        if not string:
            return 'Nothing to encode'

        for char in string:
            if char != prevChar:
                if prevChar:
                    result += str(count) + prevChar
                count = 1
                prevChar = char
            else:
                count += 1
        else:
            result += str(count) + prevChar
            return result

    def decoding(string):
        result = ''
        count = 0
        for char in string:
            if str(char).isdigit():
                count = int(char)
            else:
                result += char * count
                count = 0
        return result


    fileToEncoding = open('encoding.txt', 'r').readline()
    filetoDecoding = open('decoding.txt', 'r')
    print(f'Изначальный текст для кодирования: {fileToEncoding}')
    print(f'Кодированный текст: {encoding(fileToEncoding)}')

    print(f'Изначальный текст для декодирования:')
    for i in filetoDecoding:
        if i == '':
            break
        print(i)
    filetoDecoding.seek(0, 0)
    print('Декодированный файл:')
    for i in filetoDecoding:
        if i == '':
            break
        print(decoding(str(i)))

    # print(f'Декодированный текст: {decoding(filetoDecoding)}')
    MainProgram()


# Основная программа
def MainProgram():
    print('Введите номер программы (1-4), либо введите "Q" для выхода.')
    program = input('Программа № = ')
    if program.lower() == 'q':
        print('До свидания!')
    elif program.isdigit():
        if int(program) == 1:
            ProgramOne()
        elif int(program) == 2:
            ProgramTwo()
        elif int(program) == 3:
            ProgramThree()
        elif int(program) == 4:
            ProgramFour()
        else:
            print('Введен некорректный номер, попробуйте еще раз.')
            MainProgram()
    else:
        print('Ввод некорректен, пожалуйста, попробуйте еще раз.')
        MainProgram()


print('Здравствуйте!')
MainProgram()
