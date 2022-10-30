import math
import random

class player():
    def __init__(self,symbol):
        self.symbol=symbol
        self.score=0

    def setscore(self,num):
        self.score+=num

    def GetMove(self,board):
        '''Create a loop that keeps asking the current player for
        their input until a valid choice is made.
        '''
        pass

class HumanPlayer(player):
    def __init__(self,symbol,name="Human"):
        super().__init__(symbol)
        self.name=name

    def GetMove(self,game):
        position=input(f"{self.name}"+", type a number from 1-9 to select a position: ")
        while not game.isValidMove(position):
            position=input(f"try again: ")
        return position

class ComputerPlayer(player):
    def __init__(self,symbol,name ="Computer"):
        super().__init__(symbol)
        self.name=name

    def GetMove(self,game):
        if game.NumEmptyposition() == 9:
            position=random.randint(1,9)
        else:
            position=self.MaxMin(game,self.symbol,self.symbol)['position']
        return position

    def MaxMin(self, game, player ,name):
        MaxPlayer = self.symbol
        OtherPlayer = 'O' if player == 'X' else 'X'

        # check if the previous move is a winner
        if game.CurrentWinner == OtherPlayer:
            return {'position': None, 'score': 1 * (game.NumEmptyposition() + 1) if OtherPlayer == MaxPlayer else -1 * (
                    game.NumEmptyposition() + 1)}
        elif not game.Emptyposition():
            return {'position': None, 'score': 0}

        if player == MaxPlayer:
            best = {'position': None, 'score': -math.inf} #Maximize
        else:
            best = {'position': None, 'score': math.inf} #Minimize

        for PossibleMove in game.AllAvailableMoves():
            game.MakeMove(PossibleMove, player,player)
            score = self.MaxMin(game, OtherPlayer,OtherPlayer)

            # undo move
            game.board[PossibleMove] = ' '
            game.CurrentWinner = None
            score['position'] = PossibleMove

            if player == MaxPlayer:  # X is max player
                if score['score'] > best['score']:
                    best = score
            else:
                if score['score'] < best['score']:
                    best = score
        return best