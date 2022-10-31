from player import HumanPlayer, ComputerPlayer
import random

class TicTacToe():
    def __init__(self):
        self.board = self.MakeBoard()
        self.CurrentWinner = None

    def MakeBoard(self):
        return [' ' for _ in range(10)]

    def PrintBoard(self):
        '''Print the game board'''
        print( f"|{self.board[1]}|{self.board[2]}|{self.board[3]}|\n"
               f"|{self.board[4]}|{self.board[5]}|{self.board[6]}|\n"
               f"|{self.board[7]}|{self.board[8]}|{self.board[9]}|\n")

    def MakeMove(self,position,symbol,name):
        '''Method for setting move'''
        if self.board[int(position)] not in {'X','O'}:
            self.board[int(position)]=symbol
            if self.hasContestantWon(symbol):
                self.CurrentWinner = name
            return True
        return False

    def AllAvailableMoves(self):
        '''Method for get array with all the positions that empty'''
        arr=[]
        for ind in range (1,10):
            if self.board[ind] == ' ':
                arr.append(ind)
        return arr

    def NumEmptyposition(self):
        '''Method to check the number of empty positions on the board'''
        return len(self.AllAvailableMoves())

    def Emptyposition(self):
        '''Method to check if game is complete'''
        return self.NumEmptyposition()!=0

    def isValidMove(self,position):
        '''Check if move is valid'''
        if not position.isdigit():
            print("That\'s not a valid number")
            return False
        if int(position)<1 or int(position)>9:
            print("That number is out of range")
            return False
        if not self.board[int(position)] in {'X','O'}:
            return True
        print("That position is already marked,")
        return False

    def hasContestantWon(self, symbol):
        '''Check for a win- row, col and diagonal'''
        if self.board[1]== self.board[2]== self.board[3]== symbol  or \
                self.board[1]== self.board[4]== self.board[7]== symbol  or \
                self.board[1]== self.board[5]== self.board[9]== symbol  or \
                self.board[2]== self.board[5]== self.board[8]== symbol  or \
                self.board[4]== self.board[5]== self.board[6]== symbol  or \
                self.board[3]== self.board[6]== self.board[9]== symbol  or \
                self.board[3]== self.board[5]== self.board[7]== symbol  or \
                self.board[7]== self.board[8]== self.board[9]== symbol :
            return True
        return False

    def ChooseFirstplayer(self):
        ''' Return a random first player 'X' or 'O' '''
        if random.randint(0, 1):
            return 'X'
        else:
            return 'O'

def play(game,x_player, o_player, print_game=True):
    '''Create a loop that keeps the game in play
       until it ends in a win (score 2 points) or tie (score 1 point)
    '''
    symbol= game.ChooseFirstplayer()
    game.PrintBoard()
    while game.Emptyposition():
        if symbol == 'O':
            position = o_player.GetMove(game)
            game.MakeMove(position, o_player.symbol,o_player.name)
        else:
            position = x_player.GetMove(game)
            game.MakeMove(position, x_player.symbol,x_player.name)

        if print_game:
            print(symbol + ' makes a move to square {}'.format(position))
            game.PrintBoard()

        if game.CurrentWinner:
            if print_game:
                print("\n"+game.CurrentWinner + ' wins!')
                if game.CurrentWinner== o_player.name:
                    o_player.score+=2
                else:
                    x_player.score+=2
            return

        if not game.Emptyposition():
            print("\nThe game ended in a tie!")
            o_player.score+=1
            x_player.score+=1
            return
        symbol = 'O' if symbol == 'X' else 'X'  # switches player

def showScores(x_player, o_player):
    '''Score for the game : win 2 points tie 1 point'''
    print('\nscore:')
    print(f"{x_player.name}"," : ",x_player.score)
    print(f"{o_player.name}"," : ",o_player.score)



if __name__ == '__main__':
    print('Welcome to Tic Tac Toe game!\n')
    print("       |1|2|3|\n       |4|5|6|\n       |7|8|9|\n")

    #----------part 1 & 3

    print('player VS player!\n')
    name_player1= input('Enter username for player 1: ')
    name_player2= input('Enter username for player 2: ')
    x_player = HumanPlayer('X',name_player1)
    o_player = HumanPlayer('O',name_player2)
    start=input('ready to start the game? Y/N ')
    while(start.upper()=='Y'):
        t = TicTacToe()
        play(t,x_player, o_player, print_game=True)
        start=input('play again? Y/N ')
    showScores(x_player, o_player)

####################################################################

    #----------part 2 & 3
    print('\nplayer VS computer!\n')
    name_player= input('Enter username for player: ')
    o_player = ComputerPlayer('O')
    x_player = HumanPlayer('X',name_player)
    start=input('ready to start the game? Y/N ')
    while(start.upper()=='Y'):
        t = TicTacToe()
        play(t,x_player, o_player, print_game=True)
        start=input('play again? Y/N ')
    showScores(x_player, o_player)
