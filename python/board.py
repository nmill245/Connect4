import numpy as np
from numpy._typing import NDArray
import curses

class Board(object):
    
    def __init__(self, screen):
        self._player1piece: int = 1
        self._player2piece: int = 2
        self._rows: int = 7
        self._cols: int = 7
        self._board: NDArray = np.zeros((self._rows, self._cols))
        self._screen: curses.window = screen

    def _getChar(self, val: int) -> str:
        if(val == 0):
            return 'X'
        else:
            return 'O'

    def _getColor(self, val: int) -> int:
        if val == self._player1piece:
            return curses.color_pair(curses.COLOR_BLUE)
        if val == self._player2piece:
            return curses.color_pair(curses.COLOR_RED)
        return curses.color_pair(curses.COLOR_WHITE)


    def printBoard(self):
        screen: curses.window = self._screen
        screen.clear()
        for y in range(self._cols):
            for x in range(self._rows):
                xval = ((84 - self._rows * 2 + 1 ) // 2) + x*2 + 1
                yval = ((21 - self._cols * 2 + 1 ) // 2) + y*2 + 1
                screen.addch(yval, xval, self._getChar(int(self._board[y][x])), self._getColor(self._board[y][x]))

                screen.addch(yval, xval-1, curses.ACS_VLINE)
                screen.addch(yval, xval+1, curses.ACS_VLINE)

                screen.addch(yval-1, xval, curses.ACS_HLINE)
                screen.addch(yval+1, xval, curses.ACS_HLINE)

                screen.addch(yval-1, xval-1, curses.ACS_PLUS)
                screen.addch(yval-1, xval+1, curses.ACS_PLUS)
                screen.addch(yval+1, xval-1, curses.ACS_PLUS)
                screen.addch(yval+1, xval+1, curses.ACS_PLUS)
        yval = ((21 - self._cols * 2 + 1 ) // 2) + self._cols*2 + 1
        for x in range(self._rows):
            xval = ((84 - self._rows * 2 + 1 ) // 2) + x*2 + 1
            screen.addch(yval, xval, str(x + 1))
        screen.refresh()
    def addMove(self, col: int, player1: bool) -> bool:
        movecol = col - 1
        moveTaken = False
        for i in range(self._rows - 1, -1, -1):
            if(self._board[i][movecol] == 0):
                self._board[i][movecol] = self._player1piece if player1 else self._player2piece
                moveTaken = True
                break
        return moveTaken

