from random import randrange

def initialize_board():
    return [['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3']]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell.isdigit() == False for row in board for cell in row)

def make_move(board, player, row, col):
    if board[row][col].isdigit():
        board[row][col] = player
        return True
    else:
        print("Invalid move. Try again.")
        return False

def get_player_move():
    try:
        row = int(input("Enter the row (1, 2, or 3): ")) - 1
        col = int(input("Enter the column (1, 2, or 3): ")) - 1
        return row, col
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid row and column numbers.")
        return get_player_move()

def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        if current_player == 'X':
            row, col = get_player_move()
        else:
            row, col = randrange(3), randrange(3)
            print(f"Computer chose row {row + 1}, column {col + 1}.")

        if make_move(board, current_player, row, col):
            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
