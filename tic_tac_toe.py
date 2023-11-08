def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals
    # This code is so goofy looking tbh
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

while True:
    print_board(board)

    row = int(input(f"Enter row (0, 1, 2) for player {current_player}: "))
    col = int(input(f"Enter column (0, 1, 2) for player {current_player}: "))

    if is_valid_move(board, row, col):
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")
