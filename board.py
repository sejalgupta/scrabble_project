#!/usr/local/bin/python

"""
Models a square board for a scrabble game.

Original: https://github.com/boringcactus/Appel-Jacobson-scrabble/blob/canon/board.py
"""

class Board:

    def __init__(self, size: int):
        """
        Board class for a scrabble game.

        Parameters:
        - size (int): The size of the board, must be odd
        """
        if size % 2 == 0:
            raise Exception("Board size must be odd!")
        elif size == 0 or size == 1:
            raise Exception("Board size must be at least 3!")
    
        self.size = size
        self._tiles = [[None for _ in range(size)] for _ in range(size)]


    def __str__(self):
        return '\n'.join(''.join(x if x is not None else '_' for x in row) for row in self._tiles)


    def all_positions(self):
        """
        Return all positions- empty and filled- of the board.

        Returns:
        - list: List of all the positions of the board
        """
        return [(row, col) for row in range(self.size) for col in range(self.size)]


    def get_tile(self, pos: tuple):
        """
        Get the tile located at the position.

        Parameters:
        - pos (tuple): The row and column of the tile

        Returns:
        - str: The tile located at the position; None if there is no tile.
        """
        row, col = pos
        return self._tiles[row][col]


    def set_tile(self, pos: tuple, tile: str):
        """
        Set a tile at the given position.

        Parameters:
        - pos (tuple): The row and column to place the tile
        - tile (str): The tile to place
        """
        row, col = pos
        self._tiles[row][col] = tile


    def in_bounds(self, pos: tuple):
        """
        Checks if the position is in bounds.

        Parameters:
        - pos (tuple): The position to check for

        Returns:
        - boolean: If the position is in bounds or not.
        """
        row, col = pos
        return row >= 0 and row < self.size and col >= 0 and col < self.size


    def is_empty(self, pos: tuple):
        """
        Returns true if a tile does NOT exist at the given position, 
        otherwise returns false.

        Parameters:
        - pos (tuple): The row and column of the potential tile

        Returns:
        - boolean: Whether a position is empty or not.
        """
        return self.in_bounds(pos) and self.get_tile(pos) is None


    def is_filled(self, pos: tuple):
        """
        Returns true if a tile exists at the given position, 
        otherwise returns false.

        Parameters:
        - pos (tuple): The row and column of the potential tile

        Returns:
        - boolean: Whether a position is filled or not.
        """
        return self.in_bounds(pos) and self.get_tile(pos) is not None


    def copy(self):
        """
        Makes a copy of the scrabble board.

        Returns:
        - Board: A new scrabble board.
        """
        result = Board(self.size)
        for pos in self.all_positions():
            result.set_tile(pos, self.get_tile(pos))
        return result


    def get_center_pos(self):
        """
        Gets the center position of the board.

        Returns:
        - tuple: The center position of the board.
        """
        return self.size // 2, self.size // 2


def sample_board():
    result = Board(7)
    result.set_tile((1, 1), 'o')
    result.set_tile((2, 1), 'f')
    result.set_tile((2, 5), 'r')
    return result