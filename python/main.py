"""
The main function to operate the Connect4 Game
"""
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
    curses.nocbreak()
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
    curses.cbreak()
    curses.endwin()

def main():
    """
    A main function to operate the game loop
    """
    stdscr: curses.window =  init_screen()
    try:
        board1 = board.Board(stdscr)
        board1.print_board()
        time.sleep(5)
        board1.add_move(1, True)
        board1.print_board()
        time.sleep(5)
        board1.add_move(1, False)
        board1.print_board()
        time.sleep(5)
    except:
        print('Error')
    finally:
        destroy_screen(stdscr)

if __name__ == '__main__':
    main()
     
