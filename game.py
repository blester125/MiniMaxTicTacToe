"""The runner that facilitates a game of tick tack toe."""

# [ -Imports ]
# [ -Python ]
import argparse
# [ -Project ]
from board import blank_board, value_to_str, TOKENS, evaluate_board, print_board
from player import Player, ComputerPlayer


def play(game_board, x_player, o_player):
    """Play a game."""
    players = [x_player, o_player]
    active_player = 0

    winner = TOKENS.BLANK

    while winner is TOKENS.BLANK:
        print("~~~~~~~~~~Turn {}~~~~~~~~~~".format(active_player))
        print_board(game_board)
        game_board = players[active_player % len(players)].play(game_board)
        winner = evaluate_board(game_board)
        active_player += 1

    print("~~~~~~~~~GAME OVER~~~~~~~~~~")
    print_board(game_board)
    print("{}wins!".format(value_to_str(winner)))


def main():
    """Configure the game."""
    parser = argparse.ArgumentParser("Play tic-tac-toe against an AI powered by minimax search")
    parser.add_argument("--players", "-p", type=int, choices=[0, 1, 2], default=1, dest="players")
    parser.add_argument("--order", "-o", type=int, choices=[1, 2], default=1, dest="order")
    args = parser.parse_args()

    if args.players == 2:
        p1 = Player(TOKENS.X)
        p2 = Player(TOKENS.O)
    elif args.players == 1:
        if args.order == 1:
            p1 = Player(TOKENS.X)
            p2 = ComputerPlayer(TOKENS.O)
        else:
            p1 = ComputerPlayer(TOKENS.X)
            p2 = Player(TOKENS.O)
    else:
        p1 = ComputerPlayer(TOKENS.X)
        p2 = ComputerPlayer(TOKENS.O)

    board = blank_board()
    play(board, p1, p2)


if __name__ == "__main__":
    main()
