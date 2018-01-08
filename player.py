"""Player objects."""

# [ -Imports ]
# [ -Python ]
import multiprocessing as mp
# [ -Third Party ]
import numpy as np
# [ -Project ]
from board import empty_board, update_board, value_to_str
from ai import mp_minimax_search


class BasePlayer(object):
    """Base palyer, saves token and makes a move."""

    def __init__(self, token):
        """Initialize the object."""
        self.token = token

    def play(self, pos, board):
        """Make the move at pos."""
        board = update_board(board, pos, self.token)
        return board


class Player(BasePlayer):
    """Human Player."""

    def play(self, board):
        """Make a move and keep running it when they try to play on a full square."""
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
    """Computer Player."""

    def __init__(self, token):
        """Initialize the object."""
        super().__init__(token)
        self.pool = mp.Pool(processes=mp.cpu_count())

    def play(self, board):
        """Make a move."""
        move = mp_minimax_search(board, self.token, self.pool)
        return super().play(move, board)
