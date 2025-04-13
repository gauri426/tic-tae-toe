def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])


def play_game():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")

        if move not in '123456789':
            print("Invalid input. Try again.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


play_game()
