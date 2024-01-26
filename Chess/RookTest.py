import unittest
import Rook
import Player
from Tabletop import *


class RookTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""

    def test_check_movement_to_empty_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        tabletop.tabletop["00"] = rook_piece

        #  Act
        result = rook_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        rook_piece2 = Rook.Rook(0, 2, "blanco")
        tabletop.tabletop["00"] = rook_piece
        tabletop.tabletop["02"] = rook_piece2

        #  Act
        result = rook_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_along_the_path(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        rook_piece2 = Rook.Rook(0, 2, "negro")
        tabletop.tabletop["00"] = rook_piece
        tabletop.tabletop["02"] = rook_piece2

        #  Act
        result = rook_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_occupied_by_different_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        rook_piece2 = Rook.Rook(0, 4, "negro")
        tabletop.tabletop["00"] = rook_piece
        tabletop.tabletop["04"] = rook_piece2

        #  Act
        result = rook_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_in_destiny(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        rook_piece2 = Rook.Rook(0, 4, "blanco")
        tabletop.tabletop["00"] = rook_piece
        tabletop.tabletop["04"] = rook_piece2

        #  Act
        result = rook_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_diagonal_cell(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        rook_piece = Rook.Rook(0, 0, "blanco")
        tabletop.tabletop["00"] = rook_piece

        #  Act
        result = rook_piece.check_movement(tabletop, 1, 1)

        #  Assert
        self.assertEqual(result, False)

