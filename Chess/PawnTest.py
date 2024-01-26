import unittest
import Pawn
import Player
from Tabletop import *


class PawnTest(unittest.TestCase):
    """def test_check_movement_to_empty_cell(self):
        self.assertEqual(True, True)"""
    # White Pawns
    def test_check_initial_movement_for_white_pawns(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 1, "blanco")
        tabletop.tabletop["01"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 3)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_empty_cell_for_white_pawns(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 0, "blanco")
        tabletop.tabletop["00"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 1)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_for_white_pawns(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 0, "blanco")
        pawn_piece2 = Pawn.Pawn(0, 1, "blanco")
        tabletop.tabletop["00"] = pawn_piece
        tabletop.tabletop["01"] = pawn_piece2

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 1)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_diagonal_cell_occupied_by_different_color_cell_for_white_pawns(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 3, "blanco")
        pawn_piece2 = Pawn.Pawn(1, 4, "negro")
        tabletop.tabletop["03"] = pawn_piece
        tabletop.tabletop["14"] = pawn_piece2

        #  Act
        result = pawn_piece.check_movement(tabletop, 1, 4)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_diagonal_cell_for_white_pawns(self):
        #  Arrange
        player1 = Player.Player("Pepe", "blanco")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 1, "blanco")
        tabletop.tabletop["01"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 1, 2)

        #  Assert
        self.assertEqual(result, False)

    # Black Pawns
    def test_check_initial_movement_for_black_pawns(self):
        #  Arrange
        player1 = Player.Player("Luis", "negro")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 6, "negro")
        tabletop.tabletop["06"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 4)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_empty_cell_for_black_pawns(self):
        #  Arrange
        player1 = Player.Player("Luis", "negro")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 7, "negro")
        tabletop.tabletop["07"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 6)

        #  Assert
        self.assertEqual(result, True)

    def test_check_movement_to_occupied_by_same_color_cell_for_black_pawns(self):
        #  Arrange
        player1 = Player.Player("Luis", "negro")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 7, "negro")
        pawn_piece2 = Pawn.Pawn(0, 6, "negro")
        tabletop.tabletop["07"] = pawn_piece
        tabletop.tabletop["06"] = pawn_piece2

        #  Act
        result = pawn_piece.check_movement(tabletop, 0, 6)

        #  Assert
        self.assertEqual(result, False)

    def test_check_movement_to_diagonal_cell_occupied_by_different_color_cell_for_black_pawns(self):
        #  Arrange
        player1 = Player.Player("Luis", "negro")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 4, "negro")
        pawn_piece2 = Pawn.Pawn(1, 3, "blanco")
        tabletop.tabletop["04"] = pawn_piece
        tabletop.tabletop["13"] = pawn_piece2

        #  Act
        result = pawn_piece.check_movement(tabletop, 1, 3)

        #  Assert
        self.assertEqual(result, True)

    def black_test_check_movement_to_diagonal_cell_for_black_pawns(self):
        #  Arrange
        player1 = Player.Player("Luis", "negro")
        tabletop = Tabletop()
        pawn_piece = Pawn.Pawn(0, 6, "negro")
        tabletop.tabletop["06"] = pawn_piece

        #  Act
        result = pawn_piece.check_movement(tabletop, 1, 5)

        #  Assert
        self.assertEqual(result, False)
