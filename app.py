from random import randint

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
def print_boards(enemy_board, player_board):
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
            cell = enemy_board[i][j]

            # Hajó elrejtése az ellenfél tábláján
            if cell == '#':
                print('.', end=" ")
            else:
                print(cell, end=" ")

        print(" " * 7, end="")

        # Saját tábla sorjelölései
        print(f"{i+1:2d} ", end="")

        # Saját tábla sorai
        for j in range(10):
            print(player_board[i][j], end=" ")
        print()
        
""" Hajók elhelyezése a táblán """
def random_place_ships(board):

    ships_sizes = [2, 3, 4]

    for size in ships_sizes:
        placed = False

        while not placed:
            # Választunk random egy irányt ahol 0 a vízszintes és 1 a függőleges
            orientation = randint(0, 1) 

            # Választunk egy random kezdő pozíciót
            # Figyyelembe vesszük a hajó méretét és az irányt is
            row = randint(0, 9 - size) if orientation == 1 else randint(0, 9)
            col = randint(0, 9 - size) if orientation == 0 else randint(0, 9)

            can_place = True

            # Ellenőrizzük, hogy elfér-e a hajó a kiválasztott pozícióban
            if orientation == 0:
                for i in range(size):
                    if board[row][col + i] != '.':
                        can_place = False
                        break
            else:
                for i in range(size):
                    if board[row + i][col] != '.':
                        can_place = False
                        break
            
            # Csak akkor rakjuk le a hajót, ha elfér
            if can_place:
                if orientation == 0:
                    for i in range(size):
                        board[row][col + i] = '#'
                else:
                    for i in range(size):
                        board[row + i][col] = '#'

                placed = True


""" Lövés bekérése a játékostól """
def player_shot():

    while True:
        shot = input("Add meg a célpont koordinátáit (pl. A5): ").upper()
        
        col_char = shot[0] 
        row_char = shot[1:]

        if len(shot) < 2 or len(shot) > 3:
            print("Érvénytelen koordináta. Próbáld újra.")
            continue

        if col_char < 'A' or col_char > 'J':
            print("Érvénytelen oszlop. Próbáld újra.")
            continue

        if not row_char.isdigit() or int(row_char) < 1 or int(row_char) > 10:
            print("Érvénytelen sor. Próbáld újra.")
            continue
        
        return shot
       
""" Lövés feldolgozása """
def process_shot(shot, board):
    col = ord(shot[0]) - 65
    row = int(shot[1:]) - 1

    cell = board[row][col]

    if cell == '#':
        board[row][col] = 'X'
        return "Talált!"
    elif cell == '.':
        board[row][col] = 'O'
        return "Mellé!"
    else:
        return "Ide már lőttél!"
    
""" Az ellenfél lövése """
def enemy_shot(board):
    while True:
        col = randint(0, 9)
        row = randint(0, 9)

        if board[row][col] in ['.', '#']:
            shot = f"{chr(65 + col)}{row + 1}"
            return shot

player_board = create_board()
enemy_board = create_board()

random_place_ships(enemy_board)
random_place_ships(player_board)

print_boards(enemy_board, player_board)

current_player = "player"

while True:

    if current_player == "player":
        print()
        print("A te köröd következik.")
        player_shot_coords = player_shot()
        result = process_shot(player_shot_coords, enemy_board)
        print_boards(enemy_board, player_board)
        print()

        if result == "Talált!":
            check_enemy_ships = any('#' in row for row in enemy_board)
            if not check_enemy_ships:
                print("Gratulálok! Megnyerted a játékot!")
                break
            else:
                print("Találat! Lőhetsz még egyszer.")
        elif result == "Ide már lőttél!":
            print("Ide már lőttél! Próbáld újra.")
        else:
            current_player = "enemy"
            print("Mellé lőttél. Az ellenfél következik.")
            input("Nyomj egy entert a folytatáshoz...")


    else:
        print()
        print("Az ellenfél köre következik.")
        enemy_shot_coords = enemy_shot(player_board)
        result = process_shot(enemy_shot_coords, player_board)
        print_boards(enemy_board, player_board)
        print()
        print(f"Az ellenfél a {enemy_shot_coords} koordinátára lőtt.")
        
        if result == "Talált!":
            check_player_ships = any('#' in row for row in player_board)
            if not check_player_ships:
                print("Sajnos vesztettél. Az ellenfél nyert.")
                break
            else:
                print("Az ellenfél talált! Újra lőhet.")
                input("Nyomj egy entert a folytatáshoz...")

        elif result == "Ide már lőttél!":
            print("Az ellenfél hibázott és újra lőhet.")
        else:
            current_player = "player"
            print("Mellé lőtt.")
