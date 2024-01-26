import unittest
import Bishop
import Player
from Tabletop import *


class BishopTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""

    def test_check_movement_to_empty_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        tabletop.tabletop["20"] = bishop_piece

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        bishop_piece2 = Bishop.Bishop(3, 1, "blanco")
        tabletop.tabletop["20"] = bishop_piece
        tabletop.tabletop["31"] = bishop_piece2

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        bishop_piece2 = Bishop.Bishop(3, 1, "negro")
        tabletop.tabletop["20"] = bishop_piece
        tabletop.tabletop["31"] = bishop_piece2

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        bishop_piece2 = Bishop.Bishop(4, 2, "negro")
        tabletop.tabletop["20"] = bishop_piece
        tabletop.tabletop["42"] = bishop_piece2

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        bishop_piece2 = Bishop.Bishop(4, 2, "blanco")
        tabletop.tabletop["20"] = bishop_piece
        tabletop.tabletop["42"] = bishop_piece2

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 2)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_orthogonal_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        bishop_piece = Bishop.Bishop(2, 0, "blanco")
        tabletop.tabletop["20"] = bishop_piece

        #  Act
        result = bishop_piece.check_movement(tabletop, 4, 0)

        #  Assert
        self.assertEqual(result, False)
