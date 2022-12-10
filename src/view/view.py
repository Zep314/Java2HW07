class View:
    def __init__(self):
        self.showHints = False

    def enterPlayerTile(self):
        # Lets the player type which tile they want to be.
        # Returns a list with the player's tile as the first item, and the computer's tile as the second.
        tile = ''
        while not (tile == 'X' or tile == 'O'):
            print('Do you want to be X or O?')
            tile = input().upper()

        # the first element in the list is the player's tile, the second is the computer's tile.
        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def printFirstTurn(self,turn):
        print('The ' + turn + ' will go first.')

    def drawBoard(self, board, validMoves = None):
        # This function prints out the board that it was passed. Returns None.
        if validMoves is None:
            validMoves = []
        HLINE = '  +---+---+---+---+---+---+---+---+'
        print('    1   2   3   4   5   6   7   8')
        print(HLINE)
        for y in range(8):
            print(y + 1, end=' ')
            for x in range(8):
                if [x, y] not in validMoves:
                    print('| %s' % (board.getElement(x, y)), end=' ')
                else:
                    print('| .', end = ' ')
            print('|')
            print(HLINE)

    def showPoints(self, board, playerTile, computerTile):
        # Prints out the current score.
        scores = board.getScoreOfBoard()
        print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))

    def getPlayerMove(self,board, playerTile):
        # Let the player type in their move.
        # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')
        DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
        while True:
            print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
            move = input().lower()
            if move == 'quit':
                return 'quit'
            if move == 'hints':
                return 'hints'

            if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if board.isValidMove(playerTile, x, y) == False:
                    continue
                else:
                    break
            else:
                print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
                print('For example, 81 will be the top-right corner.')

        return [x, y]

    def hi(self):
        print('Реверси приветствует тебя!')

    def buy(self):
        print('Пока, пока!')

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def drawFinelResults(self, board, playerTile, computerTile):
        scores = board.getScoreOfBoard()

        print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
        if scores[playerTile] > scores[computerTile]:
            print('You beat the computer by %s points! Congratulations!' % (
                        scores[playerTile] - scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
        else:
            print('The game was a tie!')