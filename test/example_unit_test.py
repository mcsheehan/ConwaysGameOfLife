import unittest
from typing import List

import numpy as np

from challenge.grid import Grid, Location


class MyTestCase(unittest.TestCase):

    def setUp(self) :
        x_grid_size = 10
        y_grid_size = 5
        grid_data = np.ndarray((x_grid_size,y_grid_size), dtype=bool)

        self.grid = Grid(grid_data)

    def test_grid_initialisation_returns_correctx(self):
        x_grid_size = 10
        y_grid_size = 5
        grid_data = np.ndarray((x_grid_size,y_grid_size), dtype=bool)

        grid = Grid(grid_data)

        self.assertEqual(x_grid_size, grid.grid_max_x)
        self.assertEqual(y_grid_size, grid.grid_max_y)

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    def test_live_cell_with_fewer_than_two_neighbours_returns_dead(self):
        x_grid_size = 10
        y_grid_size = 5
        grid_data = np.ndarray((x_grid_size,y_grid_size), dtype=bool)
        grid = Grid(grid_data)

        location = Location(1,1)
        new_cell_state = grid.evaluate_new_cell_state(location)

        self.assertFalse(new_cell_state)

    # Any live cell with two or three live neighbours lives on to the next generation.
    def test_live_cell_with_two_or_three_live_neighbours_returns_alive(self):
        location = Location(1,1)

        x_grid_size = 10
        y_grid_size = 5
        grid_data = np.ndarray((x_grid_size,y_grid_size), dtype=bool)
        grid_data[0,1] = True
        grid_data[1,2] = True

        grid = Grid(grid_data)

        new_cell_state = grid.evaluate_new_cell_state(location)

        self.assertTrue(new_cell_state)

    def test_neighbour_indices_for_postion_1_1_returns_8_neighbours(self):
        expected_number_of_neighbours = 8

        location = Location(1,1)
        neighbour_indices: List[Location] = self.grid.get_neighbour_indices(location)

        self.assertEqual(expected_number_of_neighbours, len(neighbour_indices))

    def test_neighbour_indices_for_position_1_1_with_manually_evaluated_neighbours(self):
        expected_neighbours: List[Location] = [Location(0,0), Location(1,0), Location(2,0),
                                               Location(0,1),                Location(2,1),
                                               Location(0,2), Location(1,2), Location(2,2)]

        location = Location(1,1)
        neighbour_indices: List[Location] = self.grid.get_neighbour_indices(location)

        self.assertCountEqual(expected_neighbours, neighbour_indices)

    def test_edge_cases_for_position_0_0(self):
        expected_neighbours: List[Location] = [               Location(1,0),
                                               Location(0,1), Location(1,1) ]
        location = Location(0,0)

        neighbour_indices: List[Location] = self.grid.get_neighbour_indices(location)

        self.assertCountEqual(expected_neighbours, neighbour_indices)

    def test_edge_cases_for_position_max_x_max_y(self):
        max_x = self.grid.grid_max_x -1
        max_y = self.grid.grid_max_y - 1

        location = Location(max_x, max_y)

        expected_neighbours: List[Location] = [Location(max_x-1, max_y-1), Location(max_x, max_y-1),
                                               Location(max_x-1, max_y)                             ]

        neighbour_indices: List[Location] = self.grid.get_neighbour_indices(location)
        self.assertCountEqual(expected_neighbours, neighbour_indices)




    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    def test_live_cell_with_more_than_three_neighbours_returns_dead(self):
        pass

    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    def test_live_cell_three_neighbours_returns_alive(self):
        pass

if __name__ == '__main__':
    unittest.main()
