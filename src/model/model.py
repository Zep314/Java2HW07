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
        self._board = [[' ' for j in range(8)] for i in range(8)]

        # И устанавливаем начальную позицию для игры
        self._board[3][3] = 'X'
        self._board[3][4] = 'O'
        self._board[4][3] = 'O'
        self._board[4][4] = 'X'

    def getBoardCopy(self): # возвращаем текущую позицию на доске
        return self._board[:][:]

    def getValidMoves(self,tile):
        # Возвращаем список [x, y] - таких списков, куда возможно сходить
        validMoves = []

        for x in range(8):
            for y in range(8):
                if self.isValidMove(tile, x, y):
                    validMoves.append([x, y])
        return validMoves
#        return [[[x,y] for y in range(8) if self.isValidMove(tile, x, y)] for x in range(8)]

    def isValidMove(self, tile, xStart, yStart):
        # Возвращаем False, если ход неправильный
        # Если ход правильный - возвращаем список клеток, которые надо будет перевернуть
        if self._board[xStart][yStart] != ' ' or not self.isOnBoard(xStart, yStart):
            return False

        self._board[xStart][yStart] = tile  # временно ставим символ на доску

        if tile == 'X':
            otherTile = 'O'
        else:
            otherTile = 'X'

        tilesToFlip = []
        for xDirection, yDirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            # ходим во все стороны от текущей клетки доски
            x, y = xStart, yStart
            x += xDirection  # первый шаг
            y += yDirection
            if self.isOnBoard(x, y) and self._board[x][y] == otherTile:
                # Рядом с нашим ходом находится клетка, занятая противником.
                x += xDirection
                y += yDirection
                if not self.isOnBoard(x, y):
                    continue
                while self._board[x][y] == otherTile:
                    x += xDirection
                    y += yDirection
                    if not self.isOnBoard(x, y):
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self._board[x][y] == tile:
                    # Есть клетки, которые надо перевернуть. Идем назад, пока не достигнем исходной клетки,
                    # отмечая их по пути
                    while True:
                        x -= xDirection
                        y -= yDirection
                        if x == xStart and y == yStart:
                            break
                        tilesToFlip.append([x, y])

        self._board[xStart][yStart] = ' '  # возвращаем запомененное ранее место
        if len(tilesToFlip) == 0:  # если не нашли ничего, что можно перевернуть - то вернем False
            return False
        return tilesToFlip

    def isOnBoard(self, x, y):
        # True - если координаты находятся внутри доски
        return 0 <= x <= 7 and 0 <= y <= 7

    def isOnCorner(self, x, y):
        # True - если координаты принадлежат какому-либо из 4-х углов
        return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

    def getElement(self, x ,y):
        # возвращаем значение одной ячейки доски
        return self._board[x][y]

    def getScoreOfBoard(self):
        # Считаем текущий счет игры. Возвращаем словарь с ключами 'X' и 'O'.
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
        # Делаем ход на доске, переворачивая чужие клетки. Возвращаем False - если ход неверный

        tilesToFlip = self.isValidMove(tile, xStart, yStart)

        if tilesToFlip == False:
            return False

        self._board[xStart][yStart] = tile
        for x, y in tilesToFlip:
            self._board[x][y] = tile
        return True
