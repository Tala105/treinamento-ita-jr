import numpy as np
import random

class block:
    surround : int
    mine : bool
    shown : bool

def MakeBoard():
    count = 0
    arr = []
    for i in range(16*16):
        b = block()
        if i<40:
            b.mine = True
        else:
            b.mine = False
        b.shown = False
        b.surround = 0
        arr.append(b)
    random.shuffle(arr)
    board = np.array(arr).reshape(16,16)
    
    for i in range(16):
        for j in range(16):
            if i > 0:
                if board[i-1][j].mine:
                    count = count + 1
                if j > 0:
                    if board[i-1][j-1].mine:
                        count = count + 1
                if j < 15:
                    if board[i-1][j+1].mine:
                        count = count + 1
                              
            if i < 15:
                if board[i+1][j].mine:
                    count = count + 1
                if j > 0:
                    if board[i+1][j-1].mine:
                        count = count + 1
                if j < 15:
                    if board[i+1][j+1].mine:
                        count = count + 1 
                               
            if j > 0:
                if board[i][j-1].mine:
                    count = count + 1
            if j < 15:
                if board[i][j+1].mine:
                    count = count + 1
                    
                    
            if not board[i][j].mine:
                board[i][j].surround = count
            else:
                board[i][j].surround = -1
            count = 0
    return board

def Surrounding(i, j):
    around = []
    if i > 0:
        around.append([i-1,j])
        if j > 0:
            around.append([i-1,j-1])
        if j < 15:
            around.append([i-1,j+1])               
                
    if i < 15:
        around.append([i+1,j])
        if j > 0:
            around.append([i+1,j-1])
        if j < 15:
            around.append([i+1,j+1])
                
    if j > 0:
        around.append([i,j-1])
    if j < 15:
        around.append([i,j+1])
    return around

funci = True
matrix = []

for i in range(16):
    for j in range(16):
        matrix.append([i,j]) 
board = MakeBoard()

while funci:
    band = True
    x = int(input())
    y = int(input())
    board[x][y].shown = True
    
    if board[x][y].mine == True:
        game = False
        print("GAMEOVER")
    else:
        for coord in Surrounding(i = x, j = y):
            if not board[coord[0]][coord[1]].mine:
                board[coord[0]][coord[1]].shown = True
        while band:
            band = False
            for pair in matrix:
                if board[pair[0]][pair[1]].shown == True and board[pair[0]][pair[1]].surround == 0:
                    for coord in Surrounding(i = pair[0], j = pair[1]):
                        if board[coord[0]][coord[1]].shown == False:
                            board[coord[0]][coord[1]].shown = True
                            band = True
                    
        for i in range(16):
            for j in range(16):
                if board[i][j].shown and not board[i][j].mine:
                    print(board[i][j].surround, end = " ")
                else:
                    print("x", end = " ")
            print()
