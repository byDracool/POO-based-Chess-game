def printer(value):
    if value == "Same_color_piece_error":
        return print("Casilla ocupada por otra pieza de tu mismo color")
    elif value == "Valid_movement":
        return print("Movimiento valido")
    elif value == "Destiny_key_error":
        return print("Error en casilla de destino")
    elif value == "Other_player_piece":
        return print("Error, no puedes mover piezas de otro jugador")
    elif value == "Path_blocked":
        return print("Error, camino bloqueado")
    elif value == "Create_players":
        return print("Creando jugadores...")
    elif value == "Create_tabletop":
        return print("Creando tablero...")
    elif value == "Create initial pieces":
        return print("Creando piezas y asignandolas en su posicion inicial...")
    elif value == "Source_key_error":
        return print("Error en casilla de origen")
    elif value == "Piece_movement":
        return print("Moviendo pieza a casilla de destino...")