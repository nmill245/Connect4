import board
import curses

def main():
    stdscr: curses.window = curses.initscr()
    board1 = board.Board(stdscr)
    print(board1.rows)
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    main()
