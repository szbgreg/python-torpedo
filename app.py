
""" 10x10-es üres tábla létrehozása """
def create_board():
    board = []

    for i in range(10):
        row = []
        for j in range(10):
            row.append('.')
        board.append(row)
    
    return board

""" Játékosok tábláinak kirajzolása """
def print_boards(board):
    print()
    print("*" * 55)
    print(" " * 10 + "ENEMY" + " " * 24 + "PLAYER")
    print()

    # Ellenfél tábla oszlopjelölései
    print(" " * 3, end="")
    for i in range(10):
        print(chr(65 + i), end=" ")
        
    print(" " * 10, end="")

    # Saját tábla oszlopjelölései
    for i in range(10):
        print(chr(65 + i), end=" ")

    print()

    # Sorok kirajzolása
    for i in range(10):
        # Ellenfél tábla sorjelölései
        print(f"{i+1:2d} ", end="")

        # Ellenfél tábla sorai
        for j in range(10):
            print(board[i][j], end=" ")

        print(" " * 7, end="")

        # Saját tábla sorjelölései
        print(f"{i+1:2d} ", end="")

        # Saját tábla sorai
        for j in range(10):
            print(board[i][j], end=" ")
        print()

        
player_board = create_board()
enemey_board = create_board()
print_boards(player_board)