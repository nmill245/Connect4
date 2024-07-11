import numpy as np
from numpy._typing import NDArray
import curses

class Board(object):
    
    def __init__(self, screen):
        self.rows: int = 7
        self.cols: int = 7
        self.board: NDArray = np.zeros((self.rows, self.cols))
        self.screen: curses.window = screen

    def printBoard(self):
        screen: curses.window = self.screen
        screen.clear()
        for y in range(self.cols):
            for x in range(self.rows):
                xval = ((84 - self.rows * 2 + 1 ) // 2) + x*2 + 1
                yval = ((21 - self.cols * 2 + 1 ) // 2) + y*2 + 1
                screen.addch(yval, xval, str(int(self.board[y][x])))

                screen.addch(yval, xval-1, curses.ACS_VLINE)
                screen.addch(yval, xval+1, curses.ACS_VLINE)

                screen.addch(yval-1, xval, curses.ACS_HLINE)
                screen.addch(yval+1, xval, curses.ACS_HLINE)

                screen.addch(yval-1, xval-1, curses.ACS_PLUS)
                screen.addch(yval-1, xval+1, curses.ACS_PLUS)
                screen.addch(yval+1, xval-1, curses.ACS_PLUS)
                screen.addch(yval+1, xval+1, curses.ACS_PLUS)
        screen.refresh()

