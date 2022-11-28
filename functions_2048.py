import random
import numpy as np

def start_game():
    # declaring an empty list then
    # appending 4 list each with four
    # elements as 0.
    mat = np.zeros((4,4), dtype=int)

    # printing controls for user
    print("2048 Game Start")
    print("press W or w or up arrow: Move Up")
    print("press S or s or down arrow: Move Down")
    print("press A or a or left arrow: Move Left")
    print("press D or d or right arrow: Move Right")

    # calling the function to add
    # a new 2 in grid after every step
    add_new_2(mat)
    add_new_2(mat)
    return mat


# function to add a new 2 in
# grid at any random empty cell
def add_new_2(mat):
    zerolist = []
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                zerolist.append((i, j))
    if len(zerolist) != 0:
        pick = random.choice(zerolist)
        mat[pick[0]][pick[1]] = 2
    return


def printmat(mat):
    print('|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n|{}|{}|{}|{}|\n'.format(mat[0][0], mat[0][1], mat[0][2], mat[0][3],
                                                                            mat[1][0], mat[1][1], mat[1][2], mat[1][3],
                                                                            mat[2][0], mat[2][1], mat[2][2], mat[2][3],
                                                                            mat[3][0], mat[3][1], mat[3][2], mat[3][3]))


# function to get the current
# state of game
def get_current_state(mat):
    # if any cell contains
    # 2048 we have won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 1

    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 2
            if i != 3 and j != 3:
                if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                    return 2
            elif i == 3:
                if mat[3][j] == mat[3][j + 1]:
                    return 2
            elif j == 3:
                if mat[i][3] == mat[i + 1][3]:
                    return 2
    return 0


def move_left(mat):
    for i in range(4):
        row = np.array([mat[i][0],0,0,0])
        pos = 0
        emp = int(row[0]!=0)
        for j in range(1,4):
            if mat[i][j]!=0:
                if mat[i][j] == row[pos]:
                    row[pos] = mat[i][j] * 2
                else:
                    row[emp] = mat[i][j]
                    pos = emp
                    emp += 1
        mat[i] = row
    return mat


def move_right(grid):
    return np.flip(move_left(np.flip(grid,1)),1)

def move_up(grid):
    return np.transpose(move_left(np.transpose(grid)))

def move_down(grid):
    return np.transpose(move_right(np.transpose(grid)))

