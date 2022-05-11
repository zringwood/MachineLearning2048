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
#Helper method, clears the 0s from the board
def removezeros():
    global board
    for line in board:
        while line.count(0) != 0:
            line.remove(0)
def updateleft():
    global board
    #first, we remove all the zeros.
    removezeros()
    #this allows us to add adjacent cells without worrying about zeros in between
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j] == board[i][j+1]:
                board[i][j] = board[i][j] + board[i][j+1]
                board[i].pop(j+1)
    #then we add back the zeros
    for line in board:
        while len(line) < 4 :
            line.append(0)
def updateright():
    global board
    #first, we remove all the zeros.
    removezeros()
    #this allows us to add adjacent cells without worrying about zeros in between
    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j] == board[i][j+1]:
                board[i][j] = board[i][j] + board[i][j+1]
                board[i].pop(j+1)
    
    #then we add back the zeros
    for i in range(len(board)):
        while len(board[i]) < 4 :
            board[i] = [0] + board[i]

def transposeboard():
    global board
    newboard = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            newboard[i][j] = board[j][i]
    board = newboard
#to perform updates up or down, we just rotate the board and then update either left or right.
def updatedown():
    transposeboard()
    updateright()
    transposeboard()
def updateup():
    transposeboard()
    updateleft()
    transposeboard()
newgame()
board[0] = [2,4,4,0]
board[1] = [0,4,0,2]
test = [0,0,0,2]
##for j in range(len(test)):
##    for k in range(len(test)-1):
##        if test[k] == 0 :
##            save = test[k]
##            test[k] = test[k+1]
##            test[k+1] = save
##print(test)
printboard()
print()
updateup()
printboard()
