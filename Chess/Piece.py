from __future__ import annotations
from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, pos_x, pos_y, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color

    def piece_location(self) -> str:
        real_x_position = ["A", "B", "C", "D", "E", "F", "G", "H"]
        real_y_position = [0, 1, 2, 3, 4, 5, 6, 7]
        coord_x = real_x_position[self.pos_x]
        coord_y = real_y_position[self.pos_y]
        object_key = coord_x + str(coord_y)
        return object_key

    @abstractmethod
    def piece_movement(self, tabletop, dest_x, dest_y):
        pass

    @abstractmethod
    def check_movement(self, tabletop, dest_x, dest_y):
        pass
