from random import *
#the 2048 board
board = [[0] * 4 for i in range(4)]
#method to help debug a little
def printboard() :
    for line in board:
        print(line)
#Adds the next new tile to the board.
#This code is quite inefficient but it works fine for a 4x4 grid.
def addnewtile():
    global board
    i = randint(0,3)
    j = randint(0,3)
    while board[i][j] != 0:
        i = randint(0,3)
        j = randint(0,3)
    if random() < 0.75:
        board[i][j] = 2
    else :
        board[i][j] = 4
    printboard()
#sets everything to none except two cells, which are either 2 or 4
def newgame() :
    global board
    board = [[0] * 4 for i in range(4)]
    addnewtile()
    addnewtile()
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
            #Because board[i] is changing size in this loop we need to check j
            if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
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
            if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
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
#to perform updates up or down, we just transpose the board and then update either left or right.
def updatedown():
    transposeboard()
    updateright()
    transposeboard()
def updateup():
    transposeboard()
    updateleft()
    transposeboard()
def haspossiblemoves():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            #It's possible to do these three if statements in one like but it looks very awkward.
            if board[i][j] == 0 :
                return True
            if j < len(board[i])-1 and board[i][j] == board[i][j+1] :
                return True
            if i < len(board)-1 and board[i][j] == board[i+1][j]:
                return True
    return False

 
            
newgame()
while(haspossiblemoves()):
    boardsave = board
    while(board == boardsave):
        nextmove = randint(0,3)
        if nextmove == 0 :
            updatedown()
        elif nextmove == 1:
            updateleft()
        elif nextmove == 2:
            updateright()
        elif nextmove == 3:
            updateup()
    addnewtile()
printboard()
print(haspossiblemoves())






    
