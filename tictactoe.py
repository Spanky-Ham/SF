
current_player = "X"

board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

def board_print():
    print("   A   B   C")
    for i in range(3):
        row = board[i]
        drow = [cell if cell != "" else " " for cell in row]
        row_str = "  | ".join(drow)
        print(f"{i + 1} {row_str}")
        if i < 2:
            print("  ---+----+---")

def move():
    global current_player

    a = input(f"Игрок {current_player}, введите колонку (A, B, C): ").upper()
    while a not in ("A", "B", "C"):
        a = input("Введено неверное значение, повторите попытку: ").upper()

    b = int(input("Введите строку (1, 2, 3): "))
    while b not in (1, 2, 3):
        b = int(input("Введено неверное значение, повторите попытку: "))

    col_index = {"A": 0, "B": 1, "C": 2}[a]
    row_index = b - 1

    if board[row_index][col_index] == "":
        board[row_index][col_index] = current_player
        board_print()
    else:
        print("Клетка занята, выберите другую клетку")
        move()

def player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def check_win(symbol):
    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

board_print()
while True:
    move()
    if check_win(current_player):
        print(f"Игрок {current_player} победил!")
        break
    if check_draw():
        print("Ничья!")
        break
    player()
