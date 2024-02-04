from game import Game
from board import Board

screenSize = (800,800)
size = (16,16)
board = Board(size)

game = Game(board, screenSize)
game.run()