from Piece import *
from main import *
import Printer
from Tabletop import *


class Rook(Piece):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def piece_movement(self, tabletop, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y
        player_rook = tabletop.tabletop[str(self.pos_x) + str(self.pos_y)]
        tabletop.tabletop[str(dest_x) + str(dest_y)] = player_rook
        tabletop.tabletop[str(self.pos_x) + str(self.pos_y)] = None

    def check_movement(self, tabletop, dest_x, dest_y):
        # x== y+
        if dest_x == self.pos_x and dest_y > self.pos_y:
            n = True
            while n:
                for valor in range(self.pos_y, dest_y + 1):
                    temp_y = valor + 1
                    if dest_y == temp_y:
                        if tabletop.tabletop[str(dest_x) + str(dest_y)] is not None and \
                                tabletop.tabletop[str(dest_x) + str(dest_y)].color == self.color:
                            n = False
                            Printer.printer("Same_color_piece_error")
                            return False
                        else:
                            n = False
                            Printer.printer("Valid_movement")
                            return True

                    elif tabletop.tabletop[str(self.pos_x) + str(temp_y)] is None:
                        n = True
                    else:
                        n = False
                        Printer.printer("Path_blocked")
                        return False
        # x== y-
        elif dest_x == self.pos_x and dest_y < self.pos_y:
            n = True
            while n:
                for valor in range(dest_y, self.pos_y + 1):
                    temp_y = valor - 1
                    if dest_y == temp_y:
                        if tabletop.tabletop[str(dest_x) + str(dest_y)]is not None and\
                                tabletop.tabletop[str(dest_x) + str(dest_y)].color == self.color:
                            n = False
                            Printer.printer("Same_color_piece_error")
                            return False
                        else:
                            n = False
                            Printer.printer("Valid_movement")
                            return True

                    elif tabletop.tabletop[str(self.pos_x) + str(temp_y)] is None:
                        n = True
                    else:
                        n = False
                        Printer.printer("Path_blocked")
                        return False
        # x+ y==
        elif dest_x > self.pos_x and dest_y == self.pos_y:
            n = True
            while n:
                for valor in range(self.pos_x, dest_x + 1):
                    temp_x = valor + 1
                    if dest_x == temp_x:
                        if tabletop.tabletop[str(dest_x) + str(dest_y)]is not None and\
                                tabletop.tabletop[str(dest_x) + str(dest_y)].color == self.color:
                            n = False
                            Printer.printer("Same_color_piece_error")
                            return False
                        else:
                            n = False
                            Printer.printer("Valid_movement")
                            return True

                    elif tabletop.tabletop[str(temp_x) + str(self.pos_y)] is None:
                        n = True
                    else:
                        n = False
                        Printer.printer("Path_blocked")
                        return False
        # x- y==
        elif dest_x < self.pos_x and dest_y == self.pos_y:
            n = True
            while n:
                for valor in range(dest_x, self.pos_x + 1):
                    temp_x = valor - 1
                    if dest_x == temp_x:
                        if tabletop.tabletop[str(dest_x) + str(dest_y)] is not None and\
                                tabletop.tabletop[str(dest_x) + str(dest_y)].color == self.color:
                            n = False
                            Printer.printer("Same_color_piece_error")
                            return False
                        else:
                            n = False
                            Printer.printer("Valid_movement")
                            return True

                    elif tabletop.tabletop[str(temp_x) + str(self.pos_y)] is None:
                        n = True
                    else:
                        n = False
                        Printer.printer("Path_blocked")
                        return False
        else:
            Printer.printer("Destiny_key_error")
            return False
