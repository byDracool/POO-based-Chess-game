import unittest
import King
import Player
from Tabletop import *


class KingTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""

    def test_check_movement_to_empty_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        king_piece = King.King(0, 0, "blanco")
        tabletop.tabletop["00"] = king_piece

        #  Act
        result = king_piece.check_movement(tabletop, 0, 1)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        king_piece = King.King(0, 0, "blanco")
        king_piece2 = King.King(0, 1, "blanco")
        tabletop.tabletop["00"] = king_piece
        tabletop.tabletop["01"] = king_piece2

        #  Act
        result = king_piece.check_movement(tabletop, 0, 1)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        king_piece = King.King(0, 0, "blanco")
        king_piece2 = King.King(0, 1, "negro")
        tabletop.tabletop["00"] = king_piece
        tabletop.tabletop["01"] = king_piece2

        #  Act
        result = king_piece.check_movement(tabletop, 0, 1)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_diagonal_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        king_piece = King.King(1, 1, "blanco")
        tabletop.tabletop["11"] = king_piece

        #  Act
        result = king_piece.check_movement(tabletop, 2, 0)

        #  Assert
        self.assertEqual(result, True)
