
""" 10x10-es üres tábla létrehozása """
def create_board():
    board = []

    for i in range(10):
        row = []
        for j in range(10):
            row.append('.')
        board.append(row)
    
    return board

""" Tábla kirajzolása """
def print_board(board):

    # Oszlop jelölések
    print("   ", end="")
    for i in range(10):
        print(chr(65 + i), end=" ")
    print()

    # Sorok kirajzolása
    for i in range(10):
        # Sorszámok
        print(f"{i+1:2d} ", end="")

        for j in range(10):
            print(board[i][j], end=" ")
        print()

        
board = create_board()
print_board(board)