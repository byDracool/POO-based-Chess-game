from Player import *
from Tabletop import *
import InitialPiecesCreator
from Gameplay import *
import Printer


def create_players():
    player1 = Player(input("Nombre del jugador 1: "), "blanco")
    player2 = Player(input("Nombre del jugador 2: "), "negro")
    return player1, player2


def gets_source_and_destiny_keys(player_name):
    source_key = get_coordinates("origen", player_name)
    destiny_key = get_coordinates("destino", player_name)
    return source_key, destiny_key


def get_coordinates(coord_type, player_name):
    player_input_coord_x = ["A", "B", "C", "D", "E", "F", "G", "H"]
    player_input_coord_y = [1, 2, 3, 4, 5, 6, 7, 8]
    key = False
    while not key:
        key = input("{}: Introduzca la casilla {}: ".format(player_name, coord_type))
        if len(key) == 2:
            value1 = key[0]
            value2 = int(key[1])
            if value1 in player_input_coord_x and value2 in player_input_coord_y:
                key = key
            else:
                print("Valor introducido fuera de rango")
                key = False
        else:
            print("Valor introducido fuera de rango")
            key = False
    return key


def player_key_and_coords_extractor(player_name):
    # Gets legal player source and destiny keys
    source_key, destiny_key = gets_source_and_destiny_keys(player_name)

    # Gets x and y position for source key
    source_x, source_y = coords_translator_with_key(source_key)

    # Gets x and y position for destiny key
    dest_x, dest_y = coords_translator_with_key(destiny_key)

    player_coords = (source_x, source_y, dest_x, dest_y)

    return player_coords


def coords_translator_with_key(key):
    x = key[0]
    y = int(key[1])
    word_x_position = ["A", "B", "C", "D", "E", "F", "G", "H"]

    counter = 0
    for n in word_x_position:
        if n == x:
            break
        else:
            counter += 1

    coord_y = y - 1
    coord_x = counter

    return coord_x, coord_y


def check_endgame(tabletop, color):
    # Check if exists any enemy piece in tabletop
    coords_range = ["0", "1", "2", "3", "4", "5", "6", "7"]
    endgame = None
    for i in coords_range:
        for j in coords_range:
            if tabletop[i + j] is not None:
                if tabletop[i + j].color != color:
                    endgame = False
                    break
                else:
                    endgame = True
                    continue
    return endgame


def check_winner(tabletop):
    coords_range = ["0", "1", "2", "3", "4", "5", "6", "7"]
    winner_color = ""
    for i in coords_range:
        for j in coords_range:
            if tabletop[i + j] is not None:
                if tabletop[i + j].color != "":
                    winner_color = str(tabletop[i + j].color)

    print("Partida finalizada, ganan las fichas: {}".format(winner_color))
    input("Enter para salir: ")
    exit()


if __name__ == '__main__':
    Printer.printer("Create_players")
    player1, player2 = create_players()
    print(f"{player1.name}: fichas de color {player1.player_color}\n"
          f"{player2.name}: fichas de color {player2.player_color}")
    players = [player1, player2]
    Printer.printer("Create_tabletop")
    tabletop = Tabletop()
    Printer.printer("Create initial pieces")
    InitialPiecesCreator.initial_pieces_creator(tabletop)
    # print(tabletop.tabletop)

    endgame = False
    while not endgame:
        for player in players:
            valid_movement = False
            while not valid_movement:
                player_coords = player_key_and_coords_extractor(player.name)
                source_key = str(player_coords[0]) + str(player_coords[1])
                player_gameplay = Gameplay(source_key, player_coords[2], player_coords[3])
                # Checks if player color is the same of source key piece color
                if tabletop.tabletop[source_key] is not None and \
                        player.player_color == tabletop.tabletop[source_key].color:
                    player_piece = tabletop.tabletop[source_key]
                    valid_movement = player_piece.check_movement(tabletop, player_gameplay.dest_x,
                                                                 player_gameplay.dest_y)
                    if valid_movement:
                        player_piece.piece_movement(tabletop, player_gameplay.dest_x, player_gameplay.dest_y)
                        Printer.printer("Piece_movement")

                    endgame = check_endgame(tabletop.tabletop, player.player_color)

                elif tabletop.tabletop[source_key] is not None and \
                        player.player_color != tabletop.tabletop[source_key].color:
                    Printer.printer("Other_player_piece")
                    valid_movement = False
                else:
                    Printer.printer("Source_key_error")
                    valid_movement = False
    else:
        check_winner(tabletop.tabletop)
