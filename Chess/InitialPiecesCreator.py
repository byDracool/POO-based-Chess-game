import Bishop
import King
import Knight
import Pawn
import Queen
import Rook


# Create pieces and move them to their initial tabletop position
def initial_pieces_creator(tabletop):
    player1_pawn1 = Pawn.Pawn(0, 1, "blanco")
    tabletop.tabletop["01"] = player1_pawn1
    player1_pawn2 = Pawn.Pawn(1, 1, "blanco")
    tabletop.tabletop["11"] = player1_pawn2
    player1_pawn3 = Pawn.Pawn(2, 1, "blanco")
    tabletop.tabletop["21"] = player1_pawn3
    player1_pawn4 = Pawn.Pawn(3, 1, "blanco")
    tabletop.tabletop["31"] = player1_pawn4
    player1_pawn5 = Pawn.Pawn(4, 1, "blanco")
    tabletop.tabletop["41"] = player1_pawn5
    player1_pawn6 = Pawn.Pawn(5, 1, "blanco")
    tabletop.tabletop["51"] = player1_pawn6
    player1_pawn7 = Pawn.Pawn(6, 1, "blanco")
    tabletop.tabletop["61"] = player1_pawn7
    player1_pawn8 = Pawn.Pawn(7, 1, "blanco")
    tabletop.tabletop["71"] = player1_pawn8
    player1_rook1 = Rook.Rook(0, 0, "blanco")
    tabletop.tabletop["00"] = player1_rook1
    player1_rook2 = Rook.Rook(7, 0, "blanco")
    tabletop.tabletop["70"] = player1_rook2
    player1_knight1 = Knight.Knight(1, 0, "blanco")
    tabletop.tabletop["10"] = player1_knight1
    player1_knight2 = Knight.Knight(6, 0, "blanco")
    tabletop.tabletop["60"] = player1_knight2
    player1_bishop1 = Bishop.Bishop(2, 0, "blanco")
    tabletop.tabletop["20"] = player1_bishop1
    player1_bishop2 = Bishop.Bishop(5, 0, "blanco")
    tabletop.tabletop["50"] = player1_bishop2
    player1_queen = Queen.Queen(3, 0, "blanco")
    tabletop.tabletop["30"] = player1_queen
    player1_king = King.King(4, 0, "blanco")
    tabletop.tabletop["40"] = player1_king

    player2_pawn1 = Pawn.Pawn(0, 6, "negro")
    tabletop.tabletop["06"] = player2_pawn1
    player2_pawn2 = Pawn.Pawn(1, 6, "negro")
    tabletop.tabletop["16"] = player2_pawn2
    player2_pawn3 = Pawn.Pawn(2, 6, "negro")
    tabletop.tabletop["26"] = player2_pawn3
    player2_pawn4 = Pawn.Pawn(3, 6, "negro")
    tabletop.tabletop["36"] = player2_pawn4
    player2_pawn5 = Pawn.Pawn(4, 6, "negro")
    tabletop.tabletop["46"] = player2_pawn5
    player2_pawn6 = Pawn.Pawn(5, 6, "negro")
    tabletop.tabletop["56"] = player2_pawn6
    player2_pawn7 = Pawn.Pawn(6, 6, "negro")
    tabletop.tabletop["66"] = player2_pawn7
    player2_pawn8 = Pawn.Pawn(7, 6, "negro")
    tabletop.tabletop["76"] = player2_pawn8
    player2_rook1 = Rook.Rook(0, 7, "negro")
    tabletop.tabletop["07"] = player2_rook1
    player2_rook2 = Rook.Rook(7, 7, "negro")
    tabletop.tabletop["77"] = player2_rook2
    player2_knight1 = Knight.Knight(1, 7, "negro")
    tabletop.tabletop["17"] = player2_knight1
    player2_knight2 = Knight.Knight(6, 7, "negro")
    tabletop.tabletop["67"] = player2_knight2
    player2_bishop1 = Bishop.Bishop(2, 7, "negro")
    tabletop.tabletop["27"] = player2_bishop1
    player2_bishop2 = Bishop.Bishop(5, 7, "negro")
    tabletop.tabletop["57"] = player2_bishop2
    player2_queen = Queen.Queen(3, 7, "negro")
    tabletop.tabletop["37"] = player2_queen
    player2_king = King.King(4, 7, "negro")
    tabletop.tabletop["47"] = player2_king
