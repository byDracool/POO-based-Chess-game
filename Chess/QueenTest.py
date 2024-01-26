import unittest
import Queen
import Player
from Tabletop import *


class QueenTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""

    def test_check_movement_to_empty_cell_orthogonal(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(3, 3, "blanco")
        tabletop.tabletop["33"] = queen_piece

        #  Act
        result = queen_piece.check_movement(tabletop, 7, 3)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_empty_cell_diagonal(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(3, 3, "blanco")
        tabletop.tabletop["33"] = queen_piece

        #  Act
        result = queen_piece.check_movement(tabletop, 6, 6)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(2, 0, "blanco")
        queen_piece2 = Queen.Queen(3, 1, "blanco")
        tabletop.tabletop["20"] = queen_piece
        tabletop.tabletop["31"] = queen_piece2

        #  Act
        result = queen_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(2, 0, "blanco")
        queen_piece2 = Queen.Queen(3, 1, "negro")
        tabletop.tabletop["20"] = queen_piece
        tabletop.tabletop["31"] = queen_piece2

        #  Act
        result = queen_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(2, 0, "blanco")
        queen_piece2 = Queen.Queen(4, 2, "negro")
        tabletop.tabletop["20"] = queen_piece
        tabletop.tabletop["42"] = queen_piece2

        #  Act
        result = queen_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        queen_piece = Queen.Queen(2, 0, "blanco")
        queen_piece2 = Queen.Queen(4, 2, "blanco")
        tabletop.tabletop["20"] = queen_piece
        tabletop.tabletop["42"] = queen_piece2

        #  Act
        result = queen_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)
