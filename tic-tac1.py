import random

def display(board):
    print(f'''
{board[7]}|{board[8]}|{board[9]}                     7 | 8 | 9
---+---+---                ---+---+---
{board[4]}|{board[5]}|{board[6]}     Positions->     4 | 5 | 6
---+---+---                ---+---+---
{board[1]}|{board[2]}|{board[3]}                     1 | 2 | 3
''')

def valid_input():
    while True:
        pos = input("Enter Position: ")
        if pos != '  ':
            if int(pos) in range(1, 10):
                pos = int(pos)
                break
            print('Not valid position\n')
        else:
            print("Thankyou for playing...!!! ")
            exit()
    return int(pos)

def valid_pos(turn, board):
    print(f'{turn} chance')
    pos = valid_input()
    while True:
        if board[pos] == '   ':
            board[pos] = turn
            break
        else:
            print('Cannot overwrite, plz select new location')
            pos = valid_input()

def userInput(board, symbol):
    sym1, sym2 = symbol[random.randint(0,1)]
    print(f'{sym1} is going first\n\n')
    display(board)
    for i in range(9):
        if i%2==0:
            turn = ' '+sym1+' '
            valid_pos(turn,board)
        else:
            turn = ' '+sym2+' '
            valid_pos(turn,board)
        display(board)
        if i>=4:
            if check(board):
                display(board)
                print(f" '{turn}' WON")
                break
        if i == 8:
            print("NONE IS WON .. IT'S A TIE")

def check(board):
    check = 0
    #row
    if board[1] == board[2] == board[3] != '   ' or\
     board[4] == board[5] == board[6] != '   ' or\
      board[7] == board[8] == board[9] != '  ':
        check = 1
    #col
    elif board[1] == board[4] == board[7] != '   ' or\
     board[2] == board[5] == board[8] != '   ' or\
      board[3] == board[6] == board[9] != '  ':
        check = 1
    #diag
    elif board[1] == board[5] == board[9] != '   ' or\
     board[3] == board[5] == board[7] != '   ':
        check = 1

    return check

def game():
    board = ["Just to adjust loc :)", '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ','   ']
    symbol = [('X', 'O'), ('O', 'X')]
    while True:
        marker = input('\n Enter your marker: ').upper()
        if marker == 'X' or marker == 'O':
            userInput(board, symbol)
            break
        else:
            print('Wrong Marker(X, O) please enter again.\n')
    display(board)

def main():
    again = 'Y'
    while again == 'Y':
        print('Press [space] for input whenver you want to stop')
        game()
        again = input("Press to play again:").upper()

main()


'''
know what's the game
make the board (try to print it in the board format too)

take input from user for which symbol he wants to use (x/o)

make logic for selecting which symbol goes first (x)(o)

take position from user (1-9)[check some conditions]

check whether the position is empty {if empty: fill it with the symbol || or print some error text and ask the position again}

we know the basic thing that win of 4 steps required to win
if step>=4:
    will check the board state
    if board[row/col/diag] has same value(x/o) = > print(won)
    else continue

add option to play again
'''
