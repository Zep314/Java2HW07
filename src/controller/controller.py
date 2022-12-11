import random

from src.model.model import Board
from src.view.view import View
from src.ai.ai import Ai


class Controller:
    # Контроллер - тут все происходит

    def __init__(self):  # Конструктор
        self._viewer = View()
        self._ai = Ai()

    def whoGoesFirst(self): # Выбор, кто будет ходить первым
        if random.randint(0, 1) == 0: # Выбор - рандомный
            return 'computer'
        else:
            return 'player'

    def run(self):  # Основной метод контроллера
        self._viewer.hi()
        ex = False
        while not ex:
            mainBoard = Board()
            mainBoard.resetBoard()  # это если вдруг играем не первый раз -
                                    # надо очистить доску от предыдущей игры
            playerTile, computerTile = self._viewer.enterPlayerTile() # Выбор, кто за кого будет играть
            turn = self.whoGoesFirst() # Тут рандом!
            self._viewer.printFirstTurn(turn)
            endGame = False
            while not endGame:
                if turn == 'player':
                    # Ходит человек
                    if self._viewer.showHints:
                        validMoves = mainBoard.getValidMoves(playerTile) # Включаем подсказки
                        self._viewer.drawBoard(mainBoard, validMoves)
                    else:
                        self._viewer.drawBoard(mainBoard)
                    self._viewer.showPoints(mainBoard, playerTile, computerTile) # счет игры
                    move = self._viewer.getPlayerMove(mainBoard, playerTile)
                    if move == 'quit':
                        endGame = True
                        ex = True
                        self._viewer.buy()
                        continue
                    elif move == 'hints':
                        self._viewer.showHints = not self._viewer.showHints
                        continue
                    else:
                        mainBoard.makeMove(playerTile, move[0], move[1]) # Записываем ход игрока на доску
                    if mainBoard.getValidMoves(computerTile) == []: # Если ходы кончились
                        endGame = True
                    else:
                        turn = 'computer'
                else:  # Ход компьютера
                    self._viewer.drawBoard(mainBoard)
                    self._viewer.showPoints(mainBoard, playerTile, computerTile)
                    input('Нажмите Enter чтобы увидеть ход компьютера.') # просто - пауза
                    x, y = self._ai.getComputerMove(mainBoard, computerTile) # Тут ИИ нам выдаст мощный ход!
                    mainBoard.makeMove(computerTile, x, y)  # записываем ход на доску
                    if mainBoard.getValidMoves(computerTile) == []: # Если ходы кончились
                        endGame = True
                    else:
                        turn = 'player'

            # Показываем результат игры.
            self._viewer.drawBoard(mainBoard)
            self._viewer.drawFinalResults(mainBoard, playerTile, computerTile)
            if not self._viewer.playAgain():
                ex = True
        self._viewer.buy()
