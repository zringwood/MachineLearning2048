from random import *
#the 2048 board
board = [[0] * 4 for i in range(4)]
#method to help debug a little
def printboard() :
    for line in board:
        print(line)

#sets everything to none except two cells, which are either 2 or 4
def newgame() :
    global board
    board = [[0] * 4 for i in range(4)]
    firstnum = [randint(0,3),randint(0,3)]
    board[firstnum[0]][firstnum[1]] = 2
    secondnum = firstnum
    while secondnum == firstnum :
        secondnum = [randint(0,3),randint(0,3)]
    board[secondnum[0]][secondnum[1]] = 2
#updates the board to the left
def update(direction) :
    global board
    for i in range(len(board)) :
        for j in range(len(board[i])-1):
            if board[i][j] == board[i][j+1] :
                board[i][j+1] = board[i][j] + board[i][j+1]
                board[i][j] = 0
            elif board[i][j] != 0 and board[i][j+1] == 0:
                board[i][j+1] = board[i][j]
                board[i][j] = 0

newgame()
board[0] = [2,0,4,4]
printboard()

update("right")
printboard()
update("right")
printboard()
