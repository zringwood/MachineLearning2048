from random import *
class Game:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.newgame(boardsize)
    #method to help debug a little
    def __str__(self) :
        tostr = ""
        for line in self.board:
            tostr += str(line) + "\n"
        return tostr.strip()
    #Adds the next new tile to the board.
    def addnewtile(self):
        #Iterate over the board, add all zeros to an array, then pick two randomly.
        zeroes = []
        #print(self.board)
        for i in range(len(self.board)) :
            for j in range(len(self.board)) :
                if self.board[i][j] == 0:
                    zeroes.append((i,j))
        #We now have an array of all zero coordinates on the board.
        #TODO sometimes this should be two
        if len(zeroes) > 0 :
            index = randint(0,len(zeroes)-1)
            self.board[zeroes[index][0]][zeroes[index][1]] = 2 

    #sets everything to none except two cells, which are either 2 or 4
    def newgame(self, boardsize) :
        self.board = [[0] * boardsize for i in range(boardsize)]
        self.addnewtile()
        self.addnewtile()
    #Helper method, clears the 0s from the board
    def __removezeros(self,currboard):
        board = [row[:] for row in currboard]
        for line in board:
            while line.count(0) != 0:
                line.remove(0)
        return board
    #Update methods return an updated boardstate, they don't actually update the internal board
    def updateleft(self):
        board = [row[:] for row in self.board]
        #first, we remove all the zeros.
        board = self.__removezeros(board)
        #this allows us to add adjacent cells without worrying about zeros in between
        for i in range(len(board)):
            for j in range(len(board[i])-1):
                #Because board[i] is changing size in this loop we need to check j
                if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
                    board[i][j] = board[i][j] + board[i][j+1]
                    board[i].pop(j+1)
                    
        #then we add back the zeros
        for line in board:
            while len(line) < self.boardsize :
                line.append(0)
        return board
    def updateright(self):
        board = [row[:] for row in self.board]
        #first, we remove all the zeros.
        board = self.__removezeros(board)
        #this allows us to add adjacent cells without worrying about zeros in between
        for i in range(len(board)):
            for j in range(len(board[i])-1):
                if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
                    board[i][j] = board[i][j] + board[i][j+1]
                    board[i].pop(j+1)
        
        #then we add back the zeros
        for i in range(len(board)):
            while len(board[i]) < self.boardsize :
                board[i] = [0] + board[i]
        return board
    #Helper Method
    def __transposeboard(self, currboard):
        newboard = [[0] * self.boardsize for i in range(self.boardsize)]
        for i in range(self.boardsize):
            for j in range(self.boardsize):
                newboard[i][j] = currboard[j][i]
        return newboard
    #to perform updates up or down, we just transpose the board and then update either left or right.
    def updatedown(self):
        board = self.__transposeboard(self.board)
        #first, we remove all the zeros.
        board = self.__removezeros(board)
        #this allows us to add adjacent cells without worrying about zeros in between
        for i in range(len(board)):
            for j in range(len(board[i])-1):
                if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
                    board[i][j] = board[i][j] + board[i][j+1]
                    board[i].pop(j+1)
        
        #then we add back the zeros
        for i in range(len(board)):
            while len(board[i]) < self.boardsize :
                board[i] = [0] + board[i]
        return self.__transposeboard(board)
    def updateup(self):
        board = self.__transposeboard(self.board)
        #first, we remove all the zeros.
        board = self.__removezeros(board)
        #this allows us to add adjacent cells without worrying about zeros in between
        for i in range(len(board)):
            for j in range(len(board[i])-1):
                #Because board[i] is changing size in this loop we need to check j
                if j < len(board[i])-1 and board[i][j] == board[i][j+1]:
                    board[i][j] = board[i][j] + board[i][j+1]
                    board[i].pop(j+1)
                    
        #then we add back the zeros
        for line in board:
            while len(line) < self.boardsize :
                line.append(0)
        return self.__transposeboard(board)
    def haspossiblemoves(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                #It's possible to do these three if statements in one but it looks very awkward.
                if self.board[i][j] == 0 :
                    return True
                if j < len(self.board[i])-1 and self.board[i][j] == self.board[i][j+1] :
                    return True
                if i < len(self.board)-1 and self.board[i][j] == self.board[i+1][j]:
                    return True
        return False
#Tests the game by inputting random movements
def __testgame(boardsize):         
    game = Game(boardsize)
    while(game.haspossiblemoves()):
        print(str(game))
        boardsave = game.board
        while(game.board == boardsave):
            nextmove = random()
            if nextmove < 0.4 :
                boardsave = game.updatedown()
            elif nextmove < 0.8:
                boardsave = game.updateleft()
            elif nextmove < 0.9:
                boardsave = game.updateright()
            else:
                boardsave = game.updateup()
        game.board = boardsave
        game.addnewtile()
    print(str(game))
    
