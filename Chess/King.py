from Piece import *
from main import *
import Printer
from Tabletop import *


class King(Piece):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def piece_movement(self, tabletop, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y
        player_king = tabletop.tabletop[str(self.pos_x) + str(self.pos_y)]
        tabletop.tabletop[str(dest_x) + str(dest_y)] = player_king
        tabletop.tabletop[str(self.pos_x) + str(self.pos_y)] = None

    def check_movement(self, tabletop, dest_x, dest_y):
        if tabletop.tabletop[str(dest_x) + str(dest_y)] is not None and \
                tabletop.tabletop[str(dest_x) + str(dest_y)].color == self.color:
            Printer.printer("Same_color_piece_error")
            return False
        elif dest_x == self.pos_x and dest_y == self.pos_y + 1 or dest_x == self.pos_x and dest_y == self.pos_y - 1:
            Printer.printer("Valid_movement")
            return True
        elif dest_x == self.pos_x - 1 and dest_y == self.pos_y or \
                dest_x == self.pos_x - 1 and dest_y == self.pos_y - 1 or \
                dest_x == self.pos_x - 1 and dest_y == self.pos_y + 1:
            Printer.printer("Valid_movement")
            return True
        elif dest_x == self.pos_x + 1 and dest_y == self.pos_y or \
                dest_x == self.pos_x + 1 and dest_y == self.pos_y - 1 or \
                dest_x == self.pos_x + 1 and dest_y == self.pos_y + 1:
            Printer.printer("Valid_movement")
            return True
        else:
            Printer.printer("Destiny_key_error")
            return False
