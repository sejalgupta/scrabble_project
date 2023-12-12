#!/usr/local/bin/python

"""
Models a bag of tiles for a scrabble game.
"""
import random

class Bag:

    def __init__(self, tile_to_count):
        """
        Bag class for a scrabble game.

        Parameters:
        - tile_to_count (dict): A mapping of the tile to the number of copies of each tile
        """
        self.tile_to_count = tile_to_count.copy()
        self.tile_to_pos = self.make_bag_to_tile_pos()


    def make_bag_to_tile_pos(self):

        l = self.get_all_tiles()

        tile_to_bag_pos = {} # maps tile and tile id to row_col

        for i in range(10):
            for j in range(10):
                if l == []:
                    break
                tile, tile_id = l.pop()
                tile_to_bag_pos[(tile, tile_id)] = (i, j)

        return tile_to_bag_pos


    def __str__(self):
        return str(self.tile_to_count)


    def is_empty(self):
        """
        Checks if the bag does not have any tiles left.

        Returns:
        - boolean: True if the bag is empty, false otherwise
        """
        return len(self.tile_to_count) == 0


    def remove_tile(self, tile):
        """
        Removes a single copy of the desired tile from the bag.

        Parameters:
        - tile (str): The tile to remove

        Returns:
        - int: The id of the tile that was removed
        """
        idx = self.tile_to_count[tile]
        self.tile_to_count[tile] -= 1
        if self.tile_to_count[tile] == 0:
            del self.tile_to_count[tile]
        return idx


    def draw_tile(self):
        """
        Randomly draws a tile out of the bag without replacement.

        Returns:
        - tuple: The tile (str) and tile id (int)
        """
        tiles = [tile for tile in self.tile_to_count for _ in range(self.tile_to_count[tile])]
        tile = random.choice(tiles)
        idx = self.remove_tile(tile)
        return tile, idx


    def get_all_tiles(self):
        """
        Gets all the tiles from the bag in a list format.

        Returns:
        - list: A list of tuples of the tiles along with their ids
        """
        return [(tile, idx) for tile in self.tile_to_count for idx in range(1, self.tile_to_count[tile] + 1)]


# note: not including blanks
tile_to_count_regular = { 'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12,
                    'f': 2, 'g': 3, 'h': 2, 'i': 9, 'j': 1, 
                    'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2, 
                    'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4,
                    'v': 2, 'w': 2, 'x': 1, 'y': 2, 'z': 1 }


tile_to_count_small = { 'w': 1, 'o': 1, 'r': 1, 'd': 1, 's': 1,
                    't': 1, 'n': 1, 'i': 1, 'm': 1, 'e': 1}


tile_to_count_medium = { 'a': 3, 'b': 1, 'c': 1, 'd': 1, 'e': 3,
                    'f': 1, 'g': 1, 'h': 1, 'i': 3, 'j': 1, 
                    'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 3, 'p': 1, 
                    'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 3,
                    'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1 }


tile_to_count_tiny = { 'a': 2, 't':1, "h":1, "n":1, "o":1 }