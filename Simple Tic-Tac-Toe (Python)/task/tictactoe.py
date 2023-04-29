
def print_board(M):
    print("---------")
    for i in range(3):
        print("|", ' '.join(M[i]), "|")
    print("---------")


def find_winner(mat, symbol):
    found = False
    for i in range(3):
        if ''.join(mat[i]) == (3 * symbol):
            found = True
            break
        elif ''.join([mat[0][i],
                      mat[1][i],
                      mat[2][i]]) == (3 * symbol):
            found = True
            break
    if not found:
        if ''.join([mat[0][0], mat[1][1], mat[2][2]]) == (3 * symbol):
            found = True
        elif ''.join([mat[0][2], mat[1][1], mat[2][0]]) == (3 * symbol):
            found = True
    return found

def validate_move(move, board):
    arr = (move.split())
    result = True
    if len(arr) != 2:
        print("Wrong number of coordinates!")
        result = False
    else:
        try:
            coords = [int(x) - 1 for x in arr]
            for coord in coords:
                if coord not in range(3):
                    result = False
                    print("Coordinates should be from 1 to 3!")
                    break
        except (TypeError, ValueError):
            print("You should enter numbers!")
            result = False
    if result:
        if board[coords[0]][coords[1]] != " ":
            result = False
            print("This cell is occupied! Choose another one!")
        else:
            result = tuple(coords)
    return result


def game_finished(board):
    result = True
    for i in range(len(board)):
        if ''.join(board[i]).find(" ") != -1:
            result = False
    return result


def winner(board):
    if find_winner(board, "X"):
        result = True
        print("X wins")
    elif find_winner(board, "O"):
        result = True
        print("O wins")
    else:
        result = False
    return result


M = [[" " for _ in range(3)] for _ in range(3)]
print_board(M)
player = "X"
while (not winner(M)) and (not game_finished(M)):
    # determine_state(input_state)
    coords = False
    while not coords:
        user_move = input()
        coords = validate_move(user_move, M)
    M[coords[0]][coords[1]] = player
    print_board(M)
    if player == "X":
        player = "O"
    else:
        player = "X"
if not winner(M):
    print("Draw")