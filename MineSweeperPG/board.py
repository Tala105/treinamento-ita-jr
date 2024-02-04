from piece import Piece
import random


class Board():
    def __init__(self, size):
        self.size = size
        self.lost = False
        self.won = False
        self.noBomb = 0
        self.numClicked = 0
        self.setBoard()
        
    
    def setBoard(self):
        self.board = []
        aux = []
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                hasbomb = (self.size[0]*row + col) <= 40
                if not hasbomb:
                    self.noBomb += 1
                piece = Piece(hasbomb)
                aux.append(piece)
        random.shuffle(aux)
        
            
        for j in range(self.size[1]):
            auxrow = []
            for i in range(self.size[0]):
                auxrow.append(aux[i+j*self.size[0]])
            self.board.append(auxrow)
            

        self.setSurrounding()
    
    def setSurrounding(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row,col))
                surrounding = self.getSurroundList((row,col))
                piece.setSurrounding(surrounding)
    
    def getSurroundList(self,index):
        surrounding = []
        for row in range(index[0]-1, index[0]+2):
            for col in range(index[1]-1, index[1]+2):
                outside = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if(same or outside):
                    continue
                else:
                    surrounding.append(self.getPiece((row,col)))
        return surrounding
    
    def getSize(self):
        return self.size
    
    def getPiece(self, index):
        return self.board[index[0]][index[1]]
    
    def handleClick(self, piece, flag, index):
        if (not flag and piece.getFlagged()):
            return
        
        surroundBomb = 0
        surroundFlaggedBomb = 0
        
        for p in self.getSurroundList():
            if p.getHasBomb:
                surroundBomb += 1
                
        for p in self.getSurroundList():
            if p.getHasBomb and p.getFlagged:
                surroundFlaggedBomb += 1 
        
        if piece.getClicked and surroundBomb == surroundFlaggedBomb:
            for p in self.getSurroundList():
                if not p.getHasBomb:
                    p.click()
        
        if flag:
            piece.toggleFlagged(index)
            return
        
        piece.click()
        if piece.getHasBomb():
            self.lost = True
            return
        
        self.numClicked += 1
        
        if(piece.getNumSurround() != 0):
            return
        
        for surrounding in piece.getSurrounding():
            if not surrounding.getHasBomb() and not surrounding.getClicked():
                self.handleClick(surrounding, False)
        
    def getLost(self):
        return self.lost
        
    def getWon(self):
        return self.noBomb == self.numClicked
    
    def getSurrounding(self):
        return self.surrounding