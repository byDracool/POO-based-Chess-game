from Tabletop import *
from Piece import *
from main import *
import Printer


class Pawn(Piece):
    def __init__(self, pos_x, pos_y, color):
        super().__init__(pos_x, pos_y, color)

    def piece_movement(self, tabletop, dest_x, dest_y):
        self.pos_x = dest_x
        self.pos_y = dest_y
        player_pawn = tabletop.tabletop[str(self.pos_x) + str(self.pos_y)]
        tabletop.tabletop[str(dest_x) + str(dest_y)] = player_pawn
        tabletop.tabletop[str(self.pos_x) + str(self.pos_y)] = None

    def check_movement(self, tabletop, dest_x, dest_y):
        # White pieces
        if self.color == "blanco":
            if dest_x == self.pos_x:
                if dest_y == self.pos_y + 2 and self.pos_y == 1:
                    if tabletop.tabletop[str(dest_x) + str(dest_y - 1)] is None and \
                            tabletop.tabletop[str(dest_x) + str(dest_y)] is None:
                        Printer.printer("Valid_movement")
                        return True
                elif dest_y == self.pos_y + 1 and tabletop.tabletop[str(dest_x) + str(dest_y)] is None:
                    Printer.printer("Valid_movement")
                    return True
                else:
                    Printer.printer("Destiny_key_error")
                    return False
            elif dest_x != self.pos_x and tabletop.tabletop[str(dest_x) + str(dest_y)] is not None and \
                    tabletop.tabletop[str(dest_x) + str(dest_y)].color != "blanco":
                if dest_x == self.pos_x - 1 and dest_y == self.pos_y + 1:
                    Printer.printer("Valid_movement")
                    return True
                elif dest_x == self.pos_x + 1 and dest_y == self.pos_y + 1:
                    Printer.printer("Valid_movement")
                    return True
                else:
                    Printer.printer("Destiny_key_error")
                    return False
            else:
                Printer.printer("Destiny_key_error")
                return False

        # Black pieces
        elif self.color == "negro":
            if dest_x == self.pos_x:
                if dest_y == self.pos_y - 2 and self.pos_y == 6:
                    if tabletop.tabletop[str(dest_x) + str(dest_y + 1)] is None and \
                            tabletop.tabletop[str(dest_x) + str(dest_y)] is None:
                        Printer.printer("Valid_movement")
                        return True
                elif dest_y == self.pos_y - 1 and tabletop.tabletop[str(dest_x) + str(dest_y)] is None:
                    Printer.printer("Valid_movement")
                    return True
                else:
                    Printer.printer("Destiny_key_error")
                    return False
            elif dest_x != self.pos_x and tabletop.tabletop[str(dest_x) + str(dest_y)] is not None and \
                    tabletop.tabletop[str(dest_x) + str(dest_y)].color != "negro":
                if dest_x == self.pos_x - 1 and dest_y == self.pos_y - 1:
                    Printer.printer("Valid_movement")
                    return True
                elif dest_x == self.pos_x + 1 and dest_y == self.pos_y - 1:
                    Printer.printer("Valid_movement")
                    return True
                else:
                    Printer.printer("Destiny_key_error")
                    return False
            else:
                Printer.printer("Destiny_key_error")
                return False
