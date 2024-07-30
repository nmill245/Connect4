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
    def __init__(self, screen, names):
        self._player1piece: int = 1
        self._player2piece: int = 2
        self._winning_1_piece: int = 3
        self._winning_2_piece: int = 4
        self._haswon: bool = False
        self._player_1_win: bool = False
        self._rows: int = 7
        self._cols: int = 7
        self._board: NDArray = np.zeros((self._rows, self._cols))
        self._screen: curses.window = screen
        if len(names) == 1:
            names.append('Computer')
        self._names = names

    def copy(self):
        """
        A function to generate a copy of the instance
        """
        board_copy = Board(self._screen, self._names.copy())
        board_copy._board = self._board.copy()
        return board_copy
    def _get_char(self, val: int) -> str:
        if val == 0:
            return ' '
        return 'O'

    def _get_color(self, val: int) -> int:
        if val == self._player1piece:
            return curses.color_pair(curses.COLOR_BLUE)
        if val == self._player2piece:
            return curses.color_pair(curses.COLOR_RED)
        if val >= self._winning_1_piece:
            return curses.color_pair(curses.COLOR_YELLOW)
        return curses.color_pair(curses.COLOR_WHITE)

    def score_board(self) -> float:
        """
        A function to score the board at a given state
        """
        if self._haswon:
            if self._player_1_win:
                return -100_000
            if not self._player_1_win:
                return 100_000
        if len(self.get_moves()) == 0:
            return 0
        player1score: int = 0
        player2score: int = 0
        return player1score - player2score
    def print_board(self, player1_turn):
        """
        Prints the current board state to the terminal
        """
        screen: curses.window = self._screen
        screen.clear()
        for y in range(self._cols):
            for x in range(self._rows):
                xval = ((84 - self._rows * 2 + 1 ) // 2) + x*2 + 1
                yval = ((19 - self._cols * 2 + 1 ) // 2) + y*2 + 1
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
        yval = ((19 - self._cols * 2 + 1 ) // 2) + self._cols*2 + 1
        for x in range(self._rows):
            xval = ((84 - self._rows * 2 + 1 ) // 2) + x*2 + 1
            screen.addch(yval, xval, str(x + 1))
        if self._haswon:
            screen.addstr(19, 10, f"{self._names[0] if player1_turn else self._names[1]} has won!!", \
                      self._get_color(int(player1_turn) + 2 - 2 * int(player1_turn)))
        elif len(self.get_moves()) == 0:
            screen.addstr(19, 10, "It's a tie!!")
        elif not self._haswon:
            screen.addstr(19, 10, f"{self._names[0] if player1_turn else self._names[1]}'s turn", \
                      self._get_color(int(player1_turn) + 2 - 2 * int(player1_turn)))
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

    def remove_move(self, col: int, player1: bool) -> bool:
        """
        Adds the move to the board.
        @params:
        col - the column is the labeled column to add the piece at (1 indexed).
        player1 - true if it is the first player, false otherwise
        """
        movecol = col - 1
        move_removed = False
        for i in range(self._rows):
            if (self._board[i][movecol] == self._player1piece and player1) \
                or (self._board[i][movecol] == self._player2piece and not player1):
                self._board[i][movecol] = 0
                move_removed = True
                break
        return move_removed
    def check_win(self) -> bool:
        """
        Returns true if the board has a winning position, false otherwise
        """

        board = self._board
        #check every col
        for col in range(self._cols):
            for row in range(self._rows-3):
                if(board[col][row] == board[col][row+1] and board[col][row+1] == board[col][row+2] \
                       and board[col][row+2] == board[col][row+3] and board[col][row] != 0):
                    piece = board[col][row]
                    board[col][row] = piece + 2
                    board[col][row+1] = piece + 2
                    board[col][row+2] = piece + 2
                    board[col][row+3] = piece + 2
                    self._haswon = True
                    self._player_1_win = piece == self._player1piece
                    return True
        #check every row
        for row in range(self._rows):
            for col in range(self._cols-3):
                if(board[col][row] != 0 and board[col][row] != 0 and board[col][row] == board[col+1][row] \
                   and board[col+1][row] == board[col+2][row] and board[col+2][row] == board[col+3][row]):
                    piece = board[col][row]
                    board[col][row] = piece + 2
                    board[col+1][row] = piece + 2
                    board[col+2][row] = piece + 2
                    board[col+3][row] = piece + 2
                    self._haswon = True
                    self._player_1_win = piece == self._player1piece
                    return True
        #check postive diagonal
        for col in range(self._cols-3):
            for row in range(self._rows-3):
                if(board[col][row] != 0 and board[col][row] == board[col+1][row+1] \
                   and board[col+1][row+1] == board[col+2][row+2] and board[col+2][row+2] == board[col+3][row+3]):
                    piece = board[col][row]
                    board[col][row] = piece + 2
                    board[col+1][row+1] = piece + 2
                    board[col+2][row+2] = piece + 2
                    board[col+3][row+3] = piece + 2
                    self._haswon = True
                    self._player_1_win = piece == self._player1piece
                    return True
        #check negative diagonal
        for col in range(3, self._cols):
            for row in range(self._rows-3):
                if(board[col][row] != 0 and board[col][row] == board[col-1][row+1] \
                   and board[col-1][row+1] == board[col-2][row+2] and board[col-2][row+2] == board[col-3][row+3]):
                    piece = board[col][row]
                    board[col][row] = piece + 2
                    board[col-1][row+1] = piece + 2
                    board[col-2][row+2] = piece + 2
                    board[col-3][row+3] = piece + 2
                    self._haswon = True
                    self._player_1_win = piece == self._player1piece
                    return True
        self._haswon = False
        return False
    def get_moves(self) -> list[int]:
        """
        A function to return the list of columns that have moves possible
        """
        move_list = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._board[col][row] == 0:
                    move_list.append(row)
                    break
        return move_list

    def get_move_chrs(self) -> list[int]:
        """
        A function to return what character values as ints are valid moves
        """
        move_list = self.get_moves()
        final_list = []
        for move in move_list:
            final_list.append(ord(str(move + 1)))
        return final_list
