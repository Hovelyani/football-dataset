import random

symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
symbols = random.choices(symbols, k=9)
grid = []
for i in range(3):
    row = []
    for j in range(3):
        row.append({"symbol": symbols[i * 3 + j], "captured": False})
    grid.append(row)

def display_grid(grid):
    for row in grid:
        formatted_row = []
        for cell in row:
            if cell["captured"]:
                formatted_row.append(" ")
            else:
                formatted_row.append(cell["symbol"])
        print(" | ".join(formatted_row))
    print()

def capture_cell(grid, row, col):
    cell = grid[row][col]
    if cell["captured"]:
        print("Cell is already captured. Try again.")
        return False
    else:
        symbol_to_remove = cell["symbol"]
        for r in range(3):
            for c in range(3):
                if grid[r][c]["symbol"] == symbol_to_remove:
                    grid[r][c]["captured"] = True
                    grid[r][c]["symbol"] = ""  
        print("Captured symbol '" + symbol_to_remove + "' at (" + str(row) + ", " + str(col) + ")")
        return True

def player_capture(grid, player_symbols):
    rownumber = input("Choose row number (1-3): ")
    columnnumber = input("Choose column number (1-3): ")
    if rownumber.isdigit() and columnnumber.isdigit():
        rownumber = int(rownumber) - 1
        columnnumber = int(columnnumber) - 1
        if 0 <= rownumber <= 2 and 0 <= columnnumber <= 2:
            if capture_cell(grid, rownumber, columnnumber):
                player_symbols.add(grid[rownumber][columnnumber]["symbol"])
                return True  
            else:
                print("Cell is already captured. Try a different cell.")
        else:
            print("Invalid row or column number. Please enter numbers between 1 and 3.")
    else:
        print("Invalid input. Please enter valid integer numbers between 1 and 3.")
    return False

def is_game_over(grid):
    for row in grid:
        for cell in row:
            if not cell["captured"]:
                return False
    return True

def game_loop(grid):
    player_x_symbols = set()
    player_y_symbols = set()
    current_player = "X"
    while not is_game_over(grid):
        display_grid(grid)
        print(f"Player {current_player}'s turn.")
        if current_player == "X":
            player_capture(grid, player_x_symbols)
            current_player = "Y"
        else:
            player_capture(grid, player_y_symbols)
            current_player = "X"
    print("Game over!")
    display_grid(grid)
    player_x_score = len(player_x_symbols)
    player_y_score = len(player_y_symbols)
    print("Player X's unique symbols:", player_x_symbols)
    print("Player Y's unique symbols:", player_y_symbols)

    if len(player_x_symbols) > len(player_y_symbols):
        print("Player X wins!")
    elif len(player_x_symbols) < len(player_y_symbols):
        print("Player Y wins!")
    else:
        print("It's a draw!")

game_loop(grid)
