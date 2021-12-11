import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui as pyag
from random import randint

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


def get_frame():
    x = 682
    y = 316
    box = ImageGrab.grab(bbox = (x, y, x+540, y+480))
    box_np = np.array(box)
    frame = cv2.cvtColor(box_np, cv2.COLOR_BGR2RGB)
    return frame


def terminal_print_board():
    for r in range(len(board)):
        print("-------------------------------------------------------------------------")
        print("|",end = " ")
        for c in range(len(board[0])-1):
            print(board[r][c], end = " ")
            print("|", end = " ")
        print(board[r][len(board[0])-1], end = " ")
        print("|")
    print("-------------------------------------------------------------------------")


def click_box(r, c, button):
    x = 682
    y = 316
    pyag.moveTo(x + 30*c + 19, y + 60 + 30*r + 19)
    if button == "l":
        pyag.click(button='left')
    elif button == "r":
        pyag.click(button='right')
    pyag.moveTo(x, y)


#          BGR VALUES 8,14
#dark green top:        [ 44 117  74]
#background tile #1:    [159 194 229]
#background tile #2:    [153 184 215]
#green background #1:   [ 81 215 170]
#green background #2:   [ 73 209 162]
#blue 1:                [210 118  25]
#green 2:               [ 67 146  70] [ 67 145  69]
#red 3:                 [ 59  63 213] [ 58  61 212]
#purple 4:              [157 125 180] [160 131 188]
#orange 5:              [  0 143 255]
#[ 61  63 213] [173 136 186] [ 69 147  71] [ 61  64 214] [ 69 147  70]
#[197 127  38]






def read_box(frame, r, c):
    color = frame[60 + 30*r + 8][30*c + 14]
    if color[0] == 159 and color[1] == 194 and color[2] == 229:
        board[r][c] = '.'
    elif color[0] == 153 and color[1] == 184 and color[2] == 215:
        board[r][c] = '.'
    elif color[0] == 210 and color[1] == 118 and color[2] == 25:
        board[r][c] = 1
    elif color[0] == 67 and color[1] == 146 and color[2] == 70:
        board[r][c] = 2
    elif color[0] == 67 and color[1] == 145 and color[2] == 69:
        board[r][c] = 2
    elif color[0] == 59 and color[1] == 63 and color[2] == 213:
        board[r][c] = 3
    elif color[0] == 58 and color[1] == 61 and color[2] == 212:
        board[r][c] = 3
    elif color[0] == 157 and color[1] == 125 and color[2] == 180:
        board[r][c] = 4
    elif color[0] == 160 and color[1] == 131 and color[2] == 188:
        board[r][c] = 4
    elif color[0] == 0 and color[1] == 143 and color[2] == 255:
        board[r][c] = 5
    elif color[0] == 7 and color[1] == 54 and color[2] == 242:
        board[r][c] = '#'
    else:
        if color[0] != 81 and color[1] != 215 and color[2] != 170:
            if color[0] != 73 and color[1] != 209 and color[2] != 162:
                board[r][c] = '?'
                print(color)


def look_around(r, c):
    dr = [-1,-1,-1, 0, 1, 1, 1, 0]
    dc = [-1, 0, 1, 1, 1, 0,-1,-1]
    surrounding = []
    for i in range(8):
        surrounding.append((r + dr[i], c + dc[i]))
    return surrounding


def count_clickable_around(r, c):
    clickable = 0
    for t in look_around(r, c):
        if 0 <= t[0] <= len(board)-1:
            if 0 <= t[1] <= len(board[0])-1:
                if board[t[0]][t[1]] == ' ':
                    clickable += 1
    return clickable


def count_bombs_around(r, c):
    bombs = 0
    for t in look_around(r, c):
        if 0 <= t[0] <= len(board)-1:
            if 0 <= t[1] <= len(board[0])-1:
                if board[t[0]][t[1]] == '#':
                    bombs += 1
    return bombs


def right_click_all():
    for r in range(len(board)):
        for c in range(len(board[0])):
            clickable = count_clickable_around(r, c)
            bombs = count_bombs_around(r, c)
            if board[r][c] == bombs + clickable:
                for t in look_around(r,c):
                    if 0 <= t[0] <= len(board)-1:
                        if 0 <= t[1] <= len(board[0])-1:
                            #frame = get_frame()
                            #read_box(frame, t[0], t[1])
                            if board[t[0]][t[1]] == ' ':
                                click_box(t[0], t[1], "r")
                                cv2.waitKey(400)
                                frame = get_frame()
                                for r in range(14):
                                    for c in range(18):
                                        read_box(frame, r, c)
                                terminal_print_board()


def left_click_all():
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == count_bombs_around(r, c):
                for t in look_around(r, c):
                    if 0 <= t[0] <= len(board)-1:
                        if 0 <= t[1] <= len(board[0])-1:
                            #frame = get_frame()
                            #read_box(frame, t[0], t[1])
                            if board[t[0]][t[1]] == ' ':
                                click_box(t[0], t[1], "l")
                                cv2.waitKey(400)
                                frame = get_frame()
                                for r in range(14):
                                    for c in range(18):
                                        read_box(frame, r, c)
                                terminal_print_board()


def first_click():
    r = randint(0, len(board)-1)
    c = randint(0, len(board[0])-1)
    click_box(r, c, "l")


def main():
    if all(x == [' ']*18 for x in board):
        first_click()
    cv2.waitKey(2500)
    frame = get_frame()
    for r in range(14):
        for c in range(18):
            read_box(frame, r, c)
    while True:
        frame = get_frame()
        right_click_all()
        #cv2.waitKey(500)
        left_click_all()
        #cv2.waitKey(500)

main()
