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
                screen.addch(y, x*2 + 1, str(int(self.board[y][x])))
                screen.addch(y, x*2, curses.ACS_VLINE)
        screen.refresh()

