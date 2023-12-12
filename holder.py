#!/usr/local/bin/python

"""
Models a holder that stores a player's tiles for a scrabble game.
"""

class Holder:

    def __init__(self, tiles_in_holder):
        """
        Holder class for a scrabble player.

        Parameters:
        - tiles_in_holder (int): Maximum number of tiles if the holder was full
        """
        self.size = tiles_in_holder
        self.tiles = [None for _ in range(self.size)]


    def __str__(self):
        result = []
        for tup in self.tiles:
            if tup:
                tile, tile_idx = tup
                result.append(f"{tile}{tile_idx}")
            else:
                result.append(None)
        return str(result)


    def is_vacant(self, idx):
        """
        Checks if a certain location of the holder is vacant / has no tile.

        Parameters:
        - idx (int): The index/location in the holder to check
        
        Returns:
        - boolean: True if the location is vacant, False otherwise.
        """
        return self.tiles[idx] is None


    def get_empty_positions(self):
        """
        Gets the locations in the holder that are vacant.

        Returns:
        - list: A list of the indices of the holder that have no tile.
        """
        return [i for i in range(self.size) if self.is_vacant(i)]


    def get_filled_positions(self):
        """
        Gets the locations in the holder that are filled / have a tile.

        Returns:
        - list: A list of the indices of the holder that have a tile.
        """
        return [i for i in range(self.size) if not self.is_vacant(i)]


    def is_full(self):
        """
        Checks if the holder is full.

        Returns:
        - boolean: True if the holder is full, False otherwise.
        """
        return len(self.get_filled_positions()) == self.size


    def get_just_tiles(self):
        """
        Gets just the tiles, for SolveState.

        Returns:
        - list: A list of the current tiles in the holder.
        """
        return [tup[0] for tup in self.tiles if tup]


    def get_tile(self, idx):
        """
        Gets the tile at the given location.

        Parameters:
        - idx (int): The index/location of the tile.

        Returns:
        - str: The tile at the location.
        """
        return self.tiles[idx]


    def get_tile_position(self, tile):
        """
        Gets the location of the tile given the tile, if the tile exists in the holder.

        Parameters:
        - tile (str): The tile to get the index/location of

        Returns:
        - tuple: The index/location (int) and tile id (int). If the tile does not exist, returns None.

        """
        for i, tup in enumerate(self.tiles):
            if tup:
                (holder_tile, holder_tile_id) = tup
                if tile == holder_tile:
                    return i, holder_tile_id
        return None


    def is_empty(self):
        """
        Checks if the holder is empty / has no tiles at all.

        Returns:
        - boolean: True if the holder is empty, otherwise False.
        """
        return len(self.get_empty_positions()) == self.size


    def set_tile(self, tile, tile_id, idx):
        """
        Sets the tile at the given location.

        Parameters:
        - tile (str): The tile to place in the holder
        - tile_id (int): The id of the tile
        - idx (int): The exact index/location to place the new tile in
        """
        self.tiles[idx] = (tile, tile_id)


    def delete_tile(self, idx):
        """
        Deletes the tile at the given location.

        Parameters:
        - idx (int): The index/location of the tile to remove
        """
        self.tiles[idx] = None