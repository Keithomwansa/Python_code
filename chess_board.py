EMPTY = "-"
ROOK = "ROOK"
board = []
PAWN = "PAWN"
KNIGHT = "KNIGHT"

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[3][4] = PAWN
board[4][2] = KNIGHT

print(board)