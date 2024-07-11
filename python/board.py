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
        screen = self.screen
        screen.clear()
        screen.addstr(0, 0, "Hello World")
        screen.refresh()

