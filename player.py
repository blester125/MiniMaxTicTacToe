import numpy as np
import multiprocessing as mp
from board import update_board, value_to_str, TOKENS
from ai import minimax_search, mp_minimax_search


class BasePlayer(object):

    def __init__(self, token):
        self.token = token

    def play(self, pos, board):
        board = update_board(board, pos, self.token)
        return board


class Player(BasePlayer):

    def play(self, board):
        played = False
        while not played:
            try:
                row = int(input("Enter {}'s row: ".format(value_to_str(self.token))))
                col = int(input("Enter {}'s col: ".format(value_to_str(self.token))))
                row -= 1
                col -= 1
                board = super().play((row, col), board)
                played = True
            except ValueError as e:
                print(e)
        return board


class ComputerPlayer(BasePlayer):

    def __init__(self, token):
        super().__init__(token)
        self.pool = mp.Pool(processes=mp.cpu_count())

    # def play(self, board):
    #     if np.all(board == TOKENS.BLANK):
    #         move = (np.random.randint(0, 3), np.random.randint(0, 3))
    #     else:
    #         move = minimax_search(board, self.token)
    #     return super().play(move, board)

    def play(self, board):
        if np.all(board == TOKENS.BLANK):
            move = (np.random.randint(0, 3), np.random.randint(0, 3))
        else:
            move = mp_minimax_search(board, self.token, self.pool)
        return super().play(move, board)
