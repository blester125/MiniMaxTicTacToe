"""The MiniMax Serach."""

# [ -Imports ]
# [ -Project ]
from board import (
    evaluate_board, update_board, possible_moves, get_opponent, get_value
)


def minimax_search(board, token):
    """Start call of the minimax search."""
    opp_token = get_opponent(token)
    best_move, _ = max_search(board, token, opp_token)
    return best_move


def max_search(board, token, opp_token):
    """Search for the best move you can do."""
    best_value = None
    best_move = None
    for move in possible_moves(board):
        temp_board = update_board(board, move, token)
        winner = evaluate_board(temp_board)
        if winner != TOKENS.BLANK:
            value = get_value(winner, token, opp_token)
        else:
            _, value = mini_search(temp_board, token, opp_token)
        if best_value is None or value > best_value:
            best_value = value
            best_move = move
    return best_move, best_value


def mini_search(board, token, opp_token):
    """Search for the best move your opponent can make."""
    best_value = None
    best_move = None
    for move in possible_moves(board):
        temp_board = update_board(board, move, opp_token)
        winner = evaluate_board(temp_board)
        if winner != TOKENS.BLANK:
            value = get_value(winner, token, opp_token)
        else:
            _, value = max_search(temp_board, token, opp_token)
        if best_value is None or value < best_value:
            best_value = value
            best_move = move
    return best_move, best_value


def mp_minimax_search(board, token, pool):
    """Entry point for minimax search where the initial moves are done in different processes."""
    opp_token = get_opponent(token)
    moves = possible_moves(board)
    inputs = list(zip([board]*len(moves), moves, [token] * len(moves), [opp_token] * len(moves)))
    results = pool.map(mp_max_search, inputs)
    return sorted(results, key=lambda x: x[1], reverse=True)[0][0]


def mp_max_search(inputs):
    """Special case of the first move for multiprocessing."""
    board = inputs[0]
    move = inputs[1]
    token = inputs[2]
    opp_token = inputs[3]
    temp_board = update_board(board, move, token)
    winner = evaluate_board(temp_board)
    if winner != TOKENS.BLANK:
        value = get_value(winner, token, opp_token)
    else:
        _, value = mini_search(temp_board, token, opp_token)
    return move, value


def get_value(winner, token, opp_token):
    """Get the value for a win. lose, draw."""
    if winner == token:
        return 1
    elif winner == opp_token:
        return -1
    else:
        return 0
