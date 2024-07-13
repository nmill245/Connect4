"""
This module is used for the Board class.
This is an object that is the basis for the Connect4 Game
"""
import curses
import numpy as np
from numpy._typing import NDArray

class Board():
    """
    A class dedicated to the board object.
    This object is where the pieces live and how moves are done in Connect4
    """
    def __init__(self, screen):
        self._player1piece: int = 1
        self._player2piece: int = 2
        self._rows: int = 7
        self._cols: int = 7
        self._board: NDArray = np.zeros((self._rows, self._cols))
        self._screen: curses.window = screen

    def _get_char(self, val: int) -> str:
        if val == 0:
            return 'X'
        return 'O'

    def _get_color(self, val: int) -> int:
        if val == self._player1piece:
            return curses.color_pair(curses.COLOR_BLUE)
        if val == self._player2piece:
            return curses.color_pair(curses.COLOR_RED)
        return curses.color_pair(curses.COLOR_WHITE)


    def print_board(self):
        """
        Prints the current board state to the terminal
        """
        screen: curses.window = self._screen
        screen.clear()
        for y in range(self._cols):
            for x in range(self._rows):
                xval = ((84 - self._rows * 2 + 1 ) // 2) + x*2 + 1
                yval = ((21 - self._cols * 2 + 1 ) // 2) + y*2 + 1
                screen.addch(yval, xval, \
                             self._get_char(int(self._board[y][x])), self._get_color(self._board[y][x]))

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
    def add_move(self, col: int, player1: bool) -> bool:
        """
        Adds the move to the board.
        @params:
        col - the column is the labeled column to add the piece at (1 indexed).
        player1 - true if it is the first player, false otherwise
        """
        movecol = col - 1
        move_taken = False
        for i in range(self._rows - 1, -1, -1):
            if self._board[i][movecol] == 0:
                self._board[i][movecol] = self._player1piece if player1 else self._player2piece
                move_taken = True
                break
        return move_taken
    def get_moves(self) -> list[int]:
        """
        A function to return the list of columns that have moves possible
        """
        move_list = []
        for col in range(self._cols):
            for cell in self._board[col]:
                if int(cell) == 0:
                    move_list.append(col)
                    break
        return move_list
