import random

from src.model.model import Board

class Ai:
    # Простой класс для решения, куда сходить на текущем ходе на доске
    def __init__(self):
        pass

    def getComputerMove(self, board, computerTile):
        # Берем доску и то, чем ходит компьютер X или O, определяем, куда идем
        # и возвращаем ход списком [x, y]

        # получаем список возможных ходов
        possibleMoves = board.getValidMoves(computerTile)

        # перемешиваем возможные ходы
        random.shuffle(possibleMoves)

        # всегда занимаем углы, если есть такая возможность
        for x, y in possibleMoves:
            if board.isOnCorner(x, y):
                return [x, y]

        # Проверяем все возможные ходы - запоминаем тот, который принесет больше очков
        bestScore = -1
        for x, y in possibleMoves:
            dupeBoard = Board(board=board.getBoardCopy()) # делаем дубликат нашей доски
                                                          # с текущей позицией
            dupeBoard.makeMove(computerTile, x, y)              # тренируемся с копией доски
            score = dupeBoard.getScoreOfBoard()[computerTile]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return bestMove
