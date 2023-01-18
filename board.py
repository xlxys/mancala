class MancalaBoard:
    def __init__(self):
        self.board ={
            "A" : 4,
            "B" : 4,
            "C" : 4,
            "D" : 4,
            "E" : 4,
            "F" : 4,
            "1" : 0,
            "L" : 4,
            "K" : 4,
            "J" : 4,
            "I" : 4,
            "H" : 4,
            "G" : 4,
            "2" : 0,
                }
        
        self.P1=("A","B","C","D","E","F")
        self.P2=("L","K","J","I","H","G")

        self.FausseOp ={
            "A" : "G",
            "B" : "H",
            "C" : "I",
            "D" : "J",
            "E" : "K",
            "F" : "L",
            "1" : "2",
            "L" : "F",
            "K" : "E",
            "J" : "D",
            "I" : "C",
            "H" : "B",
            "G" : "A",
            "2" : "1",
                }
        
        self.FausseSuiv ={
            "A" : "B",
            "B" : "C",
            "C" : "D",
            "D" : "E",
            "E" : "F",
            "F" : "1",
            "1" : "L",
            "L" : "K",
            "K" : "J",
            "J" : "I",
            "I" : "H",
            "H" : "G",
            "G" : "2",
            "2" : "A",
                }
    

    #TODO can be used to highlight the Possible moves
    def PossibleMoves(self,player):
        moves = []
        
        fosses =self.P2
        if player == 1:
            fosses = self.P1
            
        for fosse in fosses:
            if self.board[fosse] > 0:
                moves.append(fosse)
        return moves

    # update the board 
    def DoMove(self,player,fosse):
        graines=self.board[fosse]
        self.board[fosse]=0
        current= fosse
        sum=0

        while graines>0:
            if player == 1:
                current=self.FausseSuiv[current]
                if current != "2":
                    self.board[current]+=1
                    graines-=1
            else:
                current=self.FausseSuiv[current]
                if current != "1":
                    self.board[current]+=1
                    graines-=1
  
        if player == 1:
            if current == "1":
                return 1
            else:
                if current in self.P1:
                    if self.board[current] == 1:
                        sum=self.board[self.FausseOp[current]]+1
                        self.board[self.FausseOp[current]]=0
                        self.board[current]=0
                        self.board["1"]+=sum
                
                return 2
        else:
            if current == "2":
                return 2
            else:
                if current in self.P2:
                    if self.board[current] == 1:
                        sum=self.board[self.FausseOp[current]]+1
                        self.board[self.FausseOp[current]]=0
                        self.board[current]=0
                        self.board["2"]+=sum
                return 1


        
        