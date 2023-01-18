import copy

class Game:
    def __init__(self,MoncalaBoard,player):
        self.state=MoncalaBoard
        self.playerSide=player
    

    def gameOver(self):
        board=self.state.board
        fausses=self.state.P1
        GameOverP1=True
        GameOverP2=True

        for p in fausses:
                for key in board.keys():
                    if p == key and board[key] != 0:
                        GameOverP1= False

        fausses=self.state.P2
        
        for p in fausses:
                for key in board.keys():
                    if p == key and board[key] != 0:
                        GameOverP2= False

        if GameOverP1==True:
            fausses=self.state.P2
            sum=0
            for p in fausses:
                for key in board.keys():
                    if p == key:
                        sum+=board[key]
                        board[key]=0
            
            # self.state.board["2"]=0
            self.state.board["2"]+=sum
            
            return True
        
        if GameOverP2==True:
            fausses=self.state.P1
            sum=0
            for p in fausses:
                for key in board.keys():
                    if p == key:
                        sum+=board[key]
                        board[key]=0
            
            # self.state.board["1"]=0
            self.state.board["1"]+=sum
            return True
        
        return False


    def findWinner(self):
        MagasinP1=self.state.board["1"]
        MagasinP2=self.state.board["2"]

        if MagasinP1>MagasinP2:
            return 1,MagasinP1
        elif MagasinP1<MagasinP2:
            return 2,MagasinP2
        elif MagasinP1 == MagasinP2:
            return 3,MagasinP1

    def evaluate(self,heuristic):
        # return self.state.board["1"] - self.state.board["2"]
        global val

        if heuristic ==1:
            return 1
        
        if heuristic ==2:

            if self.playerSide==1:
                MagasinP1=self.state.board["1"]
                MagasinP2=self.state.board["2"]
            if self.playerSide==2:
                MagasinP1=self.state.board["2"]
                MagasinP2=self.state.board["1"]
            val = MagasinP1 - MagasinP2
            return val
            
        if heuristic ==3:

            if self.playerSide==1: 
                val = self.state.board["1"]
            if self.playerSide==2:
                val = self.state.board["2"]

            for pit in self.state.PossibleMoves(self.playerSide):
                child_game = copy.deepcopy(self)
                repeter=child_game.state.DoMove(self.playerSide, pit)
                if repeter == self.playerSide:
                    return 0.2*val+1
            
        
            return 0.2*val