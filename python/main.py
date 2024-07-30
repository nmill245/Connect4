"""
The main function to operate the Connect4 Game
"""
import random as rand
import math
import sys
import time
import curses
import board
import screen

def min_max(maximizing_player: bool, alpha: float, beta: float, max_depth: int, gameboard: board.Board) \
    -> tuple[int, float]:
    """
    An algorithm to return the best move to make at a given board position, looking 5 moves in advance
    """
    if gameboard.check_win() or max_depth == 0:
        return (-1, gameboard.score_board())
    if maximizing_player:
        score:float = -math.inf
        commited_move: int = -1
        move_list: list[int] = gameboard.get_moves()
        commited_move:int = -1
        for move in move_list:
            gameboard.add_move(move + 1, maximizing_player)
            _, new_score = min_max(not maximizing_player, alpha, beta, max_depth - 1, gameboard)
            if new_score > score:
                score = new_score
                commited_move = move
            alpha = max(alpha, new_score)
            if alpha >= beta:
                break
        return commited_move, score
    score:float = math.inf
    move_list: list[int] = gameboard.get_moves()
    commited_move: int = -1
    for move in move_list:
        commited_move = move
        gameboard.add_move(move + 1, maximizing_player)
        _, new_score = min_max(not maximizing_player, alpha, beta, max_depth - 1, gameboard)
        gameboard.remove_move(move + 1, maximizing_player)
        if new_score < score:
            score = new_score
            commited_move = move
        beta = min(beta, score)
        if alpha >= beta:
            break
    return commited_move, score


def main():
    """
    A main function to operate the game loop
    """
    stdscr: curses.window =  screen.init_screen()
    try:
        names = screen.init_game(stdscr)
        while len(names) != 0:
            game_board = board.Board(stdscr, names.copy())
            player1_turn : bool = rand.randint(0, 100) < 50
            while len(game_board.get_moves()) != 0 and not game_board.check_win():
                if player1_turn or len(names) == 2:
                    game_board.print_board(player1_turn)
                    stdscr.addstr(0, 0, f"{len(names)}: {names}")
                    move_col = screen.get_user_move(stdscr, game_board)
                    if move_col == 'q':
                        screen.destroy_screen(stdscr)
                        sys.exit()
                    game_board.add_move(int(move_col), player1_turn)
                    player1_turn = not player1_turn
                else:
                    game_board.print_board(player1_turn)
                    move_col, score = min_max(player1_turn, -math.inf, math.inf, 5, game_board.copy())
                    game_board.add_move(move_col + 1, player1_turn)
                    stdscr.addstr(21, 20, f"The move was placed in {move_col} with a score of {score}")
                    stdscr.refresh()
                    time.sleep(2)
                    player1_turn = not player1_turn
            game_board.print_board(not player1_turn)
            time.sleep(1)
            names = screen.init_game(stdscr)
    except:
        print('Error')
    finally:
        screen.destroy_screen(stdscr)

if __name__ == '__main__':
    main()
