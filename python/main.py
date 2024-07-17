"""
The main function to operate the Connect4 Game
"""
import sys
import curses
import time
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

def init_colors():
    """
    This function creates the color pairs used in the board:
    White - White on Black
    Blue - Blue on Black
    Red - Red on Black
    """
    curses.init_pair(curses.COLOR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)

def destroy_screen(stdscr: curses.window) -> None:
    """
    This function deinits the curses screen, allowing the terminal to resume operation as normal
    @params: stdscr - The current curses.window
    """
    stdscr.keypad(False)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

def init_game(stdscr: curses.window):
    """
    The function to start the game
    """
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
        return 0
    stdscr.refresh()
    return -1

def get_name(stdscr: curses.window, playeramt: int):
    """
    Get the player's names
    """
    i = 0
    names = []
    while i < playeramt:
        curses.echo()
        curses.cbreak()
        stdscr.clear()
        stdscr.addstr(0, 10, f"Please enter player {i + 1}'s Name:\n")
        name = stdscr.getstr().decode(encoding='utf-8')
        names.append(name)
        i += 1
    return names

def main():
    """
    A main function to operate the game loop
    """
    stdscr: curses.window =  init_screen()
    try:
        names = init_game(stdscr)
        if names in (0, -1):
            destroy_screen(stdscr)
            sys.exit()
        board1 = board.Board(stdscr, names)
        board1.print_board(True)
        time.sleep(5)
        board1.add_move(1, True)
        board1.print_board(False)
        time.sleep(5)
        board1.add_move(1, False)
        board1.print_board(True)
        time.sleep(5)
    except:
        print('Error')
    finally:
        destroy_screen(stdscr)

if __name__ == '__main__':
    main()
