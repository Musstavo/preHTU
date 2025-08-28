import random
import time

board = ['| 0 |', ' 1 |', ' 2 |\n',
         '| 3 |', ' 4 |', ' 5 |\n',
         '| 6 |', ' 7 |', ' 8 |\n']

empty_board = ['|  |', '  |', '  |\n',
         '|  |', '  |', '  |\n',
         '|  |', '  |', '  |\n']

board = "".join(board)
empty_board = "".join(empty_board)

print(board)
while True:
    X_input = int(input("X's turn. Input move (0-8): "))
    print((f"X makes a move to square {X_input}"))
    empty_board = empty_board[:X_input+2] + 'X' + empty_board[X_input+3:]
    print(empty_board)
    break

