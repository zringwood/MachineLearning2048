from random import *
#the 2048 board
board = [[0] * 4 for i in range(4)]
#method to help debug a little
def printboard() :
    for line in board:
        print(line)
#Adds the next new tile to the board.
def addnewtile():
    global board
    #Iterate over the board, add all zeros to an array, then pick two randomly.
    zeroes = []
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[i][j] == 0:
                zeroes.append([i,j])
    #We now have an array of all zero coordinates on the board.
    index = randint(0,len(zeroes)-1)
    board[zeroes[index][0]][zeroes[index][1]] = 2
#sets everything to none except two cells, which are either 2 or 4
def newgame() :
    global board
    board = [[0] * 4 for i in range(4)]
    addnewtile()
    addnewtile()
#Helper method, clears the 0s from the board
def removezeros(currboard):
    board = [row[:] for row in currboard]
    for line in board:
        while line.count(0) != 0:
            line.remove(0)
    return board
def updateleft(currboard):
    board = [row[:] for row in currboard]
    #first, we remove all the zeros.
    removezeros(board)
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
    return board
def updateright(currboard):
    board = [row[:] for row in currboard]
    #first, we remove all the zeros.
    removezeros(board)
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
    return board
def transposeboard(currboard):
    newboard = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            newboard[i][j] = currboard[j][i]
    return newboard
    
#to perform updates up or down, we just transpose the board and then update either left or right.
def updatedown(currboard):
    board = transposeboard(currboard)
    board = updateright(board)
    return transposeboard(board)
def updateup(currboard):
    board = transposeboard(currboard)
    board = updateleft(board)
    return transposeboard(currboard)
def haspossiblemoves(board):
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
while(haspossiblemoves(board)):
    boardsave = board
    while(board == boardsave):
        nextmove = random()
        if nextmove < 0.4 :
            board = updatedown(board)
        elif nextmove < 0.8:
            board = updateleft(board)
        elif nextmove < 0.9:
            board = updateright(board)
        else:
            board = updateup(board)
    addnewtile()
printboard()





    
