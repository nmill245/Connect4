import board
import curses
import time


def initScreen() -> curses.window:
    stdscr: curses.window = curses.initscr()
    curses.start_color()
    stdscr.keypad(True)
    curses.nocbreak()
    curses.noecho()
    curses.use_default_colors()
    initColors()
    return stdscr
def initColors():
    curses.init_pair(curses.COLOR_WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(curses.COLOR_RED, curses.COLOR_RED, curses.COLOR_BLACK)

def destroyScreen(stdscr: curses.window) -> None:
    stdscr.keypad(False)
    curses.echo()
    curses.cbreak()
    curses.endwin()

def main():
    stdscr: curses.window =  initScreen()
    try:
        board1 = board.Board(stdscr)
        board1.printBoard()
        time.sleep(5)
        board1.addMove(1, True)
        board1.printBoard()
        time.sleep(5)
        board1.addMove(1, False)
        board1.printBoard()
        time.sleep(5)
    except:
        print('Error')
    finally:
        destroyScreen(stdscr)
    
if __name__ == '__main__':
    main()
