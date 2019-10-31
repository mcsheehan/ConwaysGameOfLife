from enum import Enum
from typing import List

import numpy as np


class Location():
    def __hash__(self):
        return self.x + self.y

    def __eq__(self, other):
        x_equal: bool = self.x == other.x
        y_equal: bool = self.y == other.y
        return  x_equal and y_equal

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Alive(Enum):
    alive = True,
    dead = False,


class Grid:
    def __init__(self, grid_data: np.ndarray):
        """
        :param grid_data: must be of type ndarray dtype='bool'
        """
        self.__grid = grid_data
        self.grid_max_x = self.__grid.shape[0]
        self.grid_max_y = self.__grid.shape[1]

    def get_neighbour_indices(self, location: Location) -> (List[Location]):
        x_ranges = range(location.x - 1, location.x + 2)
        y_ranges = range(location.y - 1, location.y + 2)

        neighbour_indices = []
        for x in x_ranges:
            if x < 0 or x >= self.grid_max_x :
                continue

            for y in y_ranges:
                if y < 0 or y >= self.grid_max_y:
                    continue

                if location.x == x and location.y == y:
                    continue

                new_location = Location(x,y)
                neighbour_indices.append(new_location)

        return neighbour_indices

    def get_number_of_live_neighbours(self, location: Location) -> int:
        self.get_neighbour_indices(location)
        pass

    def evaluate_new_cell_state(self, location: Location) -> bool :
        number_of_neighbours = self.get_number_of_live_neighbours(location)


# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
