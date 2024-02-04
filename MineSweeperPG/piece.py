class Piece():
    def __init__(self,hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        
    def getHasBomb(self):
        return self.hasBomb
    
    def getClicked(self):
        return self.clicked
    
    def getFlagged(self):
        return self.flagged
    
    def setSurrounding(self, surrounding):
        self.surrounding = surrounding
        self.setNumSurround()
    
    def getSurrounding(self):
        return self.surrounding
        
    def setNumSurround(self):
        self.numSurround = 0
        for piece in self.surrounding:
            if piece.getHasBomb():
                self.numSurround += 1
    
    def getNumSurround(self):
        return self.numSurround
    
    def toggleFlagged(self):
        self.flagged = not self.flagged
                
    def click(self):
        self.clicked = True