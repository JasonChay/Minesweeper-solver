from random import randint
from copy import deepcopy

"""
board = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

hiddenboard = deepcopy(board)
"""
num_bombs = 40

board = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', ' ', ' ', 'B', 'B', ' ', ' '],
[' ', 'B', ' ', ' ', ' ', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B'],
['B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' '],
[' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', 'B', 'B', ' ', 'B', ' ', ' ', 'B', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' '],
[' ', ' ', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

hiddenboard = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ',  4 ,  2 ,  1 ,  2 , ' ',  2 ,  1 ,  1 ,  1 , ' ', ' '],
[' ', ' ',  2 ,  1 ,  1 ,  2 , ' ',  1 ,  0 ,  0 ,  2 , ' ',  2 ,  0 ,  0 ,  1 , ' ', ' '],
[' ', ' ',  2 ,  0 ,  0 ,  1 ,  1 ,  1 ,  0 ,  0 ,  1 ,  1 ,  1 ,  0 ,  0 ,  1 , ' ', ' '],
[' ', ' ',  3 ,  1 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  1 ,  2 ,  2 ],
[' ', ' ', ' ', ' ',  1 ,  0 ,  0 ,  1 ,  1 ,  1 ,  0 ,  0 ,  1 ,  1 ,  1 ,  0 ,  0 ,  0 ],
[' ', ' ', ' ', ' ',  1 ,  0 ,  1 ,  2 , ' ',  1 ,  0 ,  0 ,  1 , ' ',  1 ,  1 ,  1 ,  1 ],
[' ', ' ', ' ', ' ',  1 ,  1 ,  2 , ' ', ' ',  3 ,  2 ,  1 ,  2 , ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

def initialize(r, c):

    for i in range(num_bombs):
        while True:
            randr = randint(0, len(board)-1)
            randc = randint(0, len(board[0])-1)
            if randr != r and randc != c:
                if board[randr][randc] == ' ':
                    board[randr][randc] = 'B'
                    break

def print_board():
    for r in range(len(board)):
        print("-------------------------------------------------------------------------")
        print("|",end = " ")
        for c in range(len(board[0])-1):
            print(board[r][c], end = " ")
            print("|", end = " ")
        print(board[r][len(board[0])-1], end = " ")
        print("|")
    print("-------------------------------------------------------------------------")

def print_hidden():
    for r in range(len(hiddenboard)):
        print("-------------------------------------------------------------------------")
        print("|",end = " ")
        for c in range(len(hiddenboard[0])-1):
            if hiddenboard[r][c] == 0:
                print('.', end = " ")
            else:
                print(hiddenboard[r][c], end = " ")
            print("|", end = " ")
        print(hiddenboard[r][len(hiddenboard[0])-1], end = " ")
        print("|")
    print("-------------------------------------------------------------------------")

def look_around(r, c):
    dr = [-1,-1,-1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0,-1,-1]
    surrounding = []
    for i in range(8):
        surrounding.append((r + dr[i], c + dc[i]))
    return surrounding

def left_click(r, c):
    if board[r][c] == 'B':
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return 0
    #elif hiddenboard[r][r] == '#':
    #    return -1
    bombs = 0
    for t in look_around(r, c):
        if 0 <= t[0] <= len(board)-1:
            if 0 <= t[1] <= len(board[0])-1:
                if board[t[0]][t[1]] == 'B':
                    bombs += 1
    hiddenboard[r][c] = bombs

def right_click(r, c):
    if hiddenboard[r][c] == ' ':
        hiddenboard[r][c] = '#'
    elif hiddenboard[r][c] == '#':
        hiddenboard[r][c] = ' '

def check_solved():
    for r in range(len(hiddenboard)):
        for c in range(len(hiddenboard[0])):
            if board[r][c] == ' ':
                if hiddenboard[r][c] == ' ':
                    return False
    return True

# BOT FUNCTIONS ----------------------------------------------------------------

def count_clickable_around(r, c):
    clickable = 0
    for t in look_around(r, c):
        if 0 <= t[0] <= len(board)-1:
            if 0 <= t[1] <= len(board[0])-1:
                if hiddenboard[t[0]][t[1]] == ' ':
                    clickable += 1
    return clickable

def right_click_all():
    for r in range(len(hiddenboard)):
        for c in range(len(hiddenboard[0])):
            clickable = count_clickable_around(r, c)
            bombs = count_bombs_around(r, c)
            if hiddenboard[r][c] == bombs + clickable:
                for t in look_around(r,c):
                    if 0 <= t[0] <= len(board)-1:
                        if 0 <= t[1] <= len(board[0])-1:
                            if hiddenboard[t[0]][t[1]] == ' ':
                                right_click(t[0], t[1])

def count_bombs_around(r, c):
    bombs = 0
    for t in look_around(r, c):
        if 0 <= t[0] <= len(board)-1:
            if 0 <= t[1] <= len(board[0])-1:
                if hiddenboard[t[0]][t[1]] == '#':
                    bombs += 1
    return bombs

def left_click_all():
    for r in range(len(hiddenboard)):
        for c in range(len(hiddenboard[0])):
            if hiddenboard[r][c] == count_bombs_around(r, c):
                for t in look_around(r, c):
                    if 0 <= t[0] <= len(board)-1:
                        if 0 <= t[1] <= len(board[0])-1:
                            if hiddenboard[t[0]][t[1]] == ' ':
                                left_click(t[0], t[1])

def main():
    #r = randint(0, len(board)-1)
    #c = randint(0, len(board[0])-1)
    #initialize(r, c)
    #left_click(r, c)
    print_hidden()
    while True:
        right_click_all()
        print_hidden()
        left_click_all()
        print_hidden()
        if check_solved():
            break

main()
