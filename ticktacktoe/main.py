gameBord = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '
            }


def full_game_board():
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')


def print_board(board):
    print(board['7'] + '|' + board['8'] + '| ' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


board_keys = []

for key in gameBord:
    board_keys.append(key)


# print_board(gameBord)


def game():

    print('####### Welcome to CodeZone Development ####### ')
    print("#######  Let's Play  Tic tac toe ####### ")

    fplayer = input('Player one Please Enter Your name : ')
    splayer = input('Player two Please Enter Your name : ')

    print('####### Welcome ' + fplayer + ' & ' + splayer + ' to the game #######')
    print(fplayer + ' You will be the X  & ' + splayer + ' You will be the O ')
    print()

    full_game_board()

    print()
    print("####### Let's play #######")
    print()

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(gameBord)

        move = input('Your ' + turn + ' Move to which place?')

        if move == 'quit':
            print('Thank for Playing!')
            return

        if gameBord[move] == ' ':
            gameBord[move] = turn
            count += 1
        else:
            print('This Place Already Filled Try again!')
            continue

        if count >= 5:
            if gameBord['7'] == gameBord['8'] == gameBord['9'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['4'] == gameBord['5'] == gameBord['6'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['1'] == gameBord['2'] == gameBord['3'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['7'] == gameBord['4'] == gameBord['1'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['8'] == gameBord['5'] == gameBord['2'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['9'] == gameBord['6'] == gameBord['3'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['7'] == gameBord['5'] == gameBord['3'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break
            elif gameBord['9'] == gameBord['5'] == gameBord['1'] != ' ':
                print('Game over')
                print(turn + ' Won')
                break

        if count == 9:
            print('Game over')
            print('Game Tied')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input('Do you want to play again ? (y/n)')

    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            gameBord[key] = ' '

        game()
    else:
        print('Thank for Playing!')


game()
