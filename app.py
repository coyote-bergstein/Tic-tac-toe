def input_command(command):
    matrix = [["0", "0", "0"],
              ["0", "0", "0"],
              ["0", "0", "0"]]
    for row in range(3):
        for column in range(3):
            matrix[row][column] = command[row * 3 + column]
    return matrix


def input_cord(matrix, sign, column=-1, row=-1):
    try:
        column = int(column)
        row = int(row)
    except ValueError:
        return "You should enter numbers!"
    if column < 0 or column > 2 or row < 0 or row > 2:
        return "Coordinates should be from 1 to 3!"
    if matrix[row][column] != "_":
        return "This cell is occupied! Choose another one!"
    else:
        matrix[row][column] = sign
        return ""


def status_check(matrix):
    x_amount = 0
    o_amount = 0
    for row in range(3):
        for column in range(3):
            if matrix[row][column] == "X":
                x_amount += 1
            if matrix[row][column] == "O":
                o_amount += 1

    flag = []
    for column in range(3):
        if matrix[0][column] == matrix[1][column] == matrix[2][column]:
            if matrix[0][column] != "_":
                flag.append(matrix[0][column])
    for row in range(3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2]:
            if matrix[row][0] != "_":
                flag.append(matrix[row][0])
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if matrix[0][0] != "_":
            flag.append(matrix[0][0])
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[0][2] != "_":
            flag.append(matrix[0][2])
    if ("X" in flag and "O" in flag) or abs(x_amount - o_amount) >= 2:
        return "Impossible"
    elif len(flag) == 0:
        if "_" in matrix[0] or "_" in matrix[1] or "_" in matrix[2]:
            return "Game not finished"
        else:
            return "Draw"
    else:
        return f"{flag[0]} wins"


def draw(matrix):
    battlefield = "---------\n"
    for row in range(3):
        for column in range(3):
            if column == 0:
                battlefield += "| "
            battlefield += f"{matrix[row][column]} "
            if column == 2:
                battlefield += "|\n"
    battlefield += "---------"
    print(battlefield)
#     print(f"""---------
# | {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |
# | {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |
# | {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |
# ---------""")


state = input_command("_________")
draw(state)
message = ""
sign = "X"
while message != "Draw" and message != "X wins" and message != "O wins":
    status = input_cord(state, sign, *input("Enter the coordinates (column row): ").split())
    if status != "":
        print(status)
    else:
        draw(state)
        if sign == "O":
            sign = "X"
        else:
            sign = "O"
    message = status_check(state)
print(message)
