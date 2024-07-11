import board
import curses
import time


def initScreen() -> curses.window:
    stdscr: curses.window = curses.initscr()
    stdscr.keypad(True)
    curses.nocbreak()
    curses.noecho()
    return stdscr

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
        time.sleep(3)
    except:
        print('Error')
    finally:
        destroyScreen(stdscr)
    
if __name__ == '__main__':
    main()
