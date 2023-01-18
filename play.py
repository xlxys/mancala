import math
import copy


class Play:
    def NegaMaxAlphaBetaPruning(self, game, player, depth, alpha, beta, heristique = 2):
        if game.gameOver() or depth == 1:
            bestValue = game.evaluate(heristique)
            bestPit = None
            if player == -1: # player = min = human
                bestValue = -1 * bestValue
            return bestValue, bestPit
        
        bestValue = - math.inf
        bestPit = None

        for pit in game.state.PossibleMoves(game.playerSide):
            child_game = copy.deepcopy(game)
            player_turn = child_game.state.DoMove(game.playerSide, pit)
            
            if player_turn == player:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, player, depth-1, -beta, -alpha) 
            else:
                value, _ = self.NegaMaxAlphaBetaPruning (child_game, -player, depth-1, -beta, -alpha) 
            value = - value
            if value > bestValue:
                bestValue = value
                bestPit = pit
            if bestValue > alpha:
                alpha = bestValue
            if beta <= alpha:
                return bestValue, bestPit
        
        return bestValue, bestPit

    # def NegaMaxAlphaBetaPruning (self, game, player, depth, alpha, beta):
    #     #game est une instance de la classe Game et player = COMPUTER ou HUMAN
    #     if game.gameOver() or depth == 1:
    #         bestValue = game.evaluate()
    #         bestPit = None
    #         if player == 1:
    #             bestValue = - bestValue
    #         return bestValue, bestPit
        
    #     bestValue = -inf
    #     bestPit = None
    #     for pit in game.state.possibleMoves(player):
            
    #         child_game = deepcopy(game)
    #         player_turn =  child_game.state.doMove(player, pit)
    #         # print(game.state.board['A'])

    #         if player_turn == player:
    #             value, _ = self.NegaMaxAlphaBetaPruning (child_game, player, depth-1, -beta, -alpha) 
    #         else:
    #             value, _ = self.NegaMaxAlphaBetaPruning (child_game, -player, depth-1, -beta, -alpha) 
                
    #         value = - value
    #         if value > bestValue :
    #             bestValue = value
    #             bestPit =pit

    #         if bestValue > alpha :
    #             alpha = bestValue

    #         if beta <= alpha :
    #             return bestValue, bestPit
                
    #     return bestValue, bestPit
    
    def humanTurn(self,pit,game):
        pits = game.state.PossibleMoves(game.playerSide)
        if pit in pits :
            return game.state.DoMove(game.playerSide,pit)

    def computerTrun(self, game, heristique):
        _, pit = self.NegaMaxAlphaBetaPruning(game,1, 5, -math.inf, math.inf, heristique)
        if pit != None :
            return game.state.DoMove(game.playerSide,pit)

            
        