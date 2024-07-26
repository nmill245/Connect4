"""
The main function to operate the Connect4 Game
"""
import random as rand
import sys
import time
import curses
import board
import screen

def min_max(maximizing_player: bool, alpha: int, beta: int, max_depth: int, gameboard: board.Board) -> (int, int):
    if max_depth == 0:
        return (0, gameboard.score_board(maximizing_player))
    return (0, 0)


def main():
    """
    A main function to operate the game loop
    """
    stdscr: curses.window =  screen.init_screen()
    try:
        names = screen.init_game(stdscr)
        while len(names) != 0:
            game_board = board.Board(stdscr, names)
            player1_turn : bool = rand.randint(0, 100) < 50
            while len(game_board.get_moves()) != 0 and not game_board.check_win():
                if player1_turn or len(names) == 2:
                    game_board.print_board(player1_turn)
                    move_col = screen.get_user_move(stdscr, game_board)
                    if move_col == 'q':
                        screen.destroy_screen(stdscr)
                        sys.exit()
                    game_board.add_move(int(move_col), player1_turn)
                    player1_turn = not player1_turn
                else:
                    move_col, _ = min_max(player1_turn, 0, 0, 5, game_board)
            game_board.print_board(not player1_turn)
            time.sleep(1)
            names = screen.init_game(stdscr)
    except:
        print('Error')
    finally:
        screen.destroy_screen(stdscr)

if __name__ == '__main__':
    main()
