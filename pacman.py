#!/usr/bin/python3
from enum import Enum

class Type(Enum):
    COIN = 1
    WALL = 2
    PACMAN = 3
    EMPTY = 4

"""
The pacman function calculates the number of coins collected and the final position
of the pacman after navigating through a user specified map with user given instructions.
"""
__author__ = "Aditya Karia"

def pacman(input_file):
    # Parse arguments from file
    boardDim, initPos, movements, walls = getArgs(input_file)
    
    board_x, board_y = boardDim.split(" ")
    board_x, board_y = int(board_x), int(board_y)
    initPos_x, initPos_y = initPos.split(" ")
    initPos_x, initPos_y = int(initPos_x), int(initPos_y)

    # Check if arguments are valid
    if board_x <= 0 or board_y <= 0 or initPos_x < 0 or initPos_y < 0:
        return -1, -1, 0
    if initPos_x >= board_x or initPos_y >= board_y:
        return -1, -1, 0

    board = createBoard(board_x, board_y, initPos_x, initPos_y, walls)
    coinsCollected, final_pos_x, final_pos_y = makeMovements(board, movements, board_x, board_y, initPos_x, initPos_y)
    return final_pos_x, final_pos_y, coinsCollected

# This function parses the arguments
def getArgs(file):
    f = open(file, "r")
    boardDim = f.readline().rstrip()
    initPos = f.readline().rstrip()
    movements = f.readline().rstrip()
    
    walls = []
    for line in f:
        if line == "\n":
            break
        walls.append(line.rstrip())
    f.close()

    return boardDim, initPos, movements, walls

# This function creates the 2D matrix 
def createBoard(board_x, board_y, initPos_x, initPos_y, walls):
    board = [[Type.COIN for a in range(board_y)] for b in range(board_x)]
    board[board_y - initPos_y - 1][initPos_x] = Type.PACMAN
    
    for wall in walls:
        wall_x, wall_y = wall.split(" ")
        board[board_y - int(wall_y) - 1][int(wall_x)] = Type.WALL
    
    return board

# This function makes all the movements and counts the coins collected
def makeMovements(board, movements, board_x, board_y, initPos_x, initPos_y):
    movements = list(movements)
    coinsCollected = 0
    curr_x, curr_y = initPos_x, initPos_y
    
    for movement in movements:
        if movement == "N":
            if curr_y + 1 < board_y and board[board_y - curr_y - 2][curr_x] != Type.WALL:
                board[board_y - curr_y - 1][curr_x] = Type.EMPTY
                curr_y += 1
        elif movement == "E":
            if curr_x + 1 < board_x and board[board_y - curr_y - 1][curr_x + 1] != Type.WALL:
                board[board_y - curr_y - 1][curr_x] = Type.EMPTY
                curr_x += 1
        elif movement == "S":
            if curr_y - 1 >= 0 and board[board_y - curr_y][curr_x] != Type.WALL:
                board[board_y - curr_y - 1][curr_x] = Type.EMPTY
                curr_y -= 1
        elif movement == "W":
            if curr_x - 1 >= 0 and board[board_y - curr_y - 1][curr_x - 1] != Type.WALL:
                board[board_y - curr_y - 1][curr_x] = Type.EMPTY
                curr_x -= 1
        
        if board[board_y - curr_y - 1][curr_x] == Type.COIN:
            coinsCollected += 1
        board[board_y - curr_y - 1][curr_x] = Type.PACMAN
    
    return coinsCollected, curr_x, curr_y
