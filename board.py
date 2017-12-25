"""Function to manipulate the board."""

# [ -Imports ]
# [ -Python ]
from enum import Enum
# [ -Third Party ]
import numpy as np


BOARD_SIZE = 3
TOKENS = Enum('TOKENS', 'X O BLANK DRAW')


def value_to_str(value):
    """Convert the enum values to string."""
    if value is TOKENS.X:
        return " X "
    if value is TOKENS.O:
        return " O "
    if value is TOKENS.BLANK:
        return " _ "
    if value is TOKENS.DRAW:
        return " No one "


def blank_board(size=BOARD_SIZE):
    """Get a blank board."""
    return np.full((size, size), TOKENS.BLANK)


def print_board(board):
    """Print out the board."""
    rows = []
    for row in board:
        string = ['[']
        for col in row:
            string.append(value_to_str(col))
        string.append(']')
        rows.append("".join(string))
    print("\n".join(rows))


def update_board(board, pos, value):
    """Make a move on the board."""
    new_board = board.copy()
    row, col = pos
    if new_board[row][col] != TOKENS.BLANK:
        raise ValueError("({}, {}) is already taken by{}".format(
            row + 1,
            col + 1,
            value_to_str(new_board[row][col]))
        )
    new_board[row][col] = value
    return new_board


def possible_moves(board):
    """Get all avaiable moves on the board."""
    moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == TOKENS.BLANK:
                moves.append((i, j))
    return moves


def empty_board(board):
    return not np.any(board == TOKENS.BLANK)

def evaluate_board(board):
    """Chack for the winner on the board."""
    # Check rows
    for row in board:
        if np.all(row == TOKENS.X):
            return TOKENS.X
        elif np.all(row == TOKENS.O):
            return TOKENS.O

    # Check Columns
    for i in range(board.shape[1]):
        col = board[:, i]
        if np.all(col == TOKENS.X):
            return TOKENS.X
        if np.all(col == TOKENS.O):
            return TOKENS.O

    # Check diagonals
    diag1 = np.diagonal(board)
    diag2 = np.diagonal(np.flip(board, axis=0))
    if np.all(diag1 == TOKENS.X) or np.all(diag2 == TOKENS.X):
        return TOKENS.X
    if np.all(diag1 == TOKENS.O) or np.all(diag2 == TOKENS.O):
        return TOKENS.O

    # Check for a Draw
    if not np.any((board == TOKENS.BLANK)):
        return TOKENS.DRAW

    return TOKENS.BLANK


def get_opponent(token):
    """Get the opponent enum value."""
    if token == TOKENS.X:
        return TOKENS.O
    return TOKENS.X
