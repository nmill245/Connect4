import numpy as np
from numpy._typing import NDArray

class Board(object):
    def __init__(self, screen):
        self.rows: int = 7
        self.cols: int = 7
        self.board: NDArray = np.zeros((self.rows, self.cols))
        self.screen = screen

