"""
The main function to operate the Connect4 Game
"""
import random as rand
import sys
import time
import curses
import board

def init_screen() -> curses.window:
    """
    This function is called to initalize the curses screen.
    This sets it up to be able to print colors and interact with the user.
    @returns: curses.window : the current screen
    """
    stdscr: curses.window = curses.initscr()
    curses.start_color()
    stdscr.keypad(True)
    curses.cbreak()
    curses.noecho()
    curses.use_default_colors()
    init_colors()
    return stdscr

def init_colors() -> None:
    """
    This function creates the color pairs used in the board:
    White - White on Black
    Blue - Blue on Black
    Red - Red on Black
    """
    curses.init_pair(curses.COLOR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)

def destroy_screen(stdscr: curses.window) -> None:
    """
    This function deinits the curses screen, allowing the terminal to resume operation as normal
    @params: stdscr - The current curses.window
    """
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def init_game(stdscr: curses.window) -> list[str]:
    """
    The function to start the game
    """
    stdscr.clear()
    stdscr.addstr(0, 10, "Welcome to Connect4")
    stdscr.addstr(1, 10, "Will you have (1) or (2) Players? (q)uit")
    stdscr.refresh()
    c = stdscr.getch()
    while c != ord('1') and c != ord('2') and c != ord('q'):
        stdscr.addstr(2, 10, "Please enter a valid key")
        stdscr.refresh()
        c = stdscr.getch()
    stdscr.clear()
    stdscr.addstr(2, 10, "You have entered a valid key")
    stdscr.refresh()
    if c == ord('1'):
        return get_name(stdscr, 1)
    if c == ord('2'):
        return get_name(stdscr, 2)
    if c == ord('q'):
        return []
    stdscr.refresh()
    return []

def get_name(stdscr: curses.window, playeramt: int) -> list[str]:
    """
    Get the player's names
    """
    i = 0
    names = []
    while i < playeramt:
        curses.echo()
        curses.nocbreak()
        stdscr.clear()
        stdscr.addstr(0, 10, f"Please enter player {i + 1}'s Name:\n")
        name = stdscr.getstr().decode(encoding='utf-8')
        names.append(name)
        i += 1
    curses.noecho()
    curses.cbreak()
    return names

def get_user_move(stdscr: curses.window, game_board: board.Board) -> str:
    """
    A function to retrieve the next user move
    """
    valid_move_list = game_board.get_move_chrs()
    valid_move_list.append(ord('q'))
    stdscr.refresh()
    c = stdscr.getch()
    while c not in valid_move_list:
        stdscr.addstr(20, 20, "Please enter a valid move. For example (1), (2), ...")
        stdscr.refresh()
        c = stdscr.getch()
    return chr(c)



def main():
    """
    A main function to operate the game loop
    """
    stdscr: curses.window =  init_screen()
    try:
        names = init_game(stdscr)
        while len(names) != 0:
            game_board = board.Board(stdscr, names)
            player1_turn : bool = rand.randint(0, 100) < 50
            while len(game_board.get_moves()) != 0 and not game_board.check_win():
                game_board.print_board(player1_turn)
                move_col = get_user_move(stdscr, game_board)
                if move_col == 'q':
                    destroy_screen(stdscr)
                    sys.exit()
                    break
                game_board.add_move(int(move_col), player1_turn)
                player1_turn = not player1_turn
            game_board.print_board(not player1_turn)
            time.sleep(1)
            names = init_game(stdscr)
    except:
        print('Error')
    finally:
        destroy_screen(stdscr)

if __name__ == '__main__':
    main()
