import unittest
import Knight
import Player
from Tabletop import *


class knightTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""

    def test_check_movement_to_empty_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        knight_piece = Knight.Knight(2, 3, "blanco")
        tabletop.tabletop["23"] = knight_piece

        #  Act
        result = knight_piece.check_movement(tabletop, 3, 5)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        knight_piece = Knight.Knight(2, 3, "blanco")
        knight_piece2 = Knight.Knight(3, 5, "blanco")
        tabletop.tabletop["23"] = knight_piece
        tabletop.tabletop["35"] = knight_piece2

        #  Act
        result = knight_piece.check_movement(tabletop, 3, 5)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_diagonal_cell_occupied_by_different_color_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        knight_piece = Knight.Knight(2, 3, "blanco")
        knight_piece2 = Knight.Knight(3, 5, "negro")
        tabletop.tabletop["23"] = knight_piece
        tabletop.tabletop["35"] = knight_piece2

        #  Act
        result = knight_piece.check_movement(tabletop, 3, 5)

        #  Assert
        self.assertEqual(result, True)

