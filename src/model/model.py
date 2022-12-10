class Board:

    # Класс - доска для игры РЕВЕРСИ

    def __init__(self,board = None):
        self._board = []        # пустая доска
        if board is None:
            for i in range(8):
                self._board.append([' '] * 8)
        else:                   # устанавливаем заданную позицию на доске
            self._board = [[' ' for j in range(8)] for i in range(8)]
            for x in range(8):
                for y in range(8):
                    self._board[x][y] = board[x][y]

    def resetBoard(self):
        # Очищаем доску
        for x in range(8):
            for y in range(8):
                self._board[x][y] = ' '

        # И устанавливаем начальную позицию для игры
        self._board[3][3] = 'X'
        self._board[3][4] = 'O'
        self._board[4][3] = 'O'
        self._board[4][4] = 'X'

    def getBoardCopy(self): # возвращаем текущую позицию на доске
        return self._board[:][:]

    def getValidMoves(self,tile):
        # Returns a list of [x,y] lists of valid moves for the given player on the given board.
        # Возвращаем список [x, y] - таких списков, куда возможно сходить
        validMoves = []

        for x in range(8):
            for y in range(8):
                if self.isValidMove(tile, x, y) != False:
                    validMoves.append([x, y])
        return validMoves

    def isValidMove(self, tile, xStart, yStart):
        # Returns False if the player's move on space xstart, ystart is invalid.
        # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
        # Возвращаем False, если ход неравильный
        # Если ход правильный - возвращаем !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self._board[xStart][yStart] != ' ' or not self.isOnBoard(xStart, yStart):
            return False

        self._board[xStart][yStart] = tile  # temporarily set the tile on the board.

        if tile == 'X':
            otherTile = 'O'
        else:
            otherTile = 'X'

        tilesToFlip = []
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = xStart, yStart
            x += xdirection  # first step in the direction
            y += ydirection  # first step in the direction
            if self.isOnBoard(x, y) and self._board[x][y] == otherTile:
                # There is a piece belonging to the other player next to our piece.
                x += xdirection
                y += ydirection
                if not self.isOnBoard(x, y):
                    continue
                while self._board[x][y] == otherTile:
                    x += xdirection
                    y += ydirection
                    if not self.isOnBoard(x, y):  # break out of while loop, then continue in for loop
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self._board[x][y] == tile:
                    # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        x -= xdirection
                        y -= ydirection
                        if x == xStart and y == yStart:
                            break
                        tilesToFlip.append([x, y])

        self._board[xStart][yStart] = ' '  # restore the empty space
        if len(tilesToFlip) == 0:  # If no tiles were flipped, this is not a valid move.
            return False
        return tilesToFlip

    def isOnBoard(self, x, y):
        # Returns True if the coordinates are located on the board.
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def isOnCorner(self, x, y):
        # Returns True if the position is in one of the four corners.
        return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

    def getElement(self, x ,y):
        return self._board[x][y]

    def getScoreOfBoard(self):
        # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
        xScore = 0
        oScore = 0
        for x in range(8):
            for y in range(8):
                if self._board[x][y] == 'X':
                    xScore += 1
                if self._board[x][y] == 'O':
                    oScore += 1
        return {'X': xScore, 'O': oScore}

    def makeMove(self, tile, xStart, yStart):
        # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
        # Returns False if this is an invalid move, True if it is valid.

        tilesToFlip = self.isValidMove(tile, xStart, yStart)

        if tilesToFlip == False:
            return False

        self._board[xStart][yStart] = tile
        for x, y in tilesToFlip:
            self._board[x][y] = tile
        return True
