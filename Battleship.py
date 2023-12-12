import random

def create_board():
    return [['O' for _ in range(7)] for _ in range(7)]

def print_board(board, hide_ships=False):
    print("   A B C D E F G")
    for i in range(7):
        print(f"{i+1} ", end="")
        for j in range(7):
            if hide_ships and board[i][j] != 'O':
                print('O', end=" ")
            else:
                print(board[i][j], end=" ")
        print()

def place_ship(board, ship_size):
    while True:
        row = random.randint(0, 6)
        col = random.randint(0, 6)
        orientation = random.choice(['H', 'V'])
        ship_cells = [(0, i) if orientation == 'H' else (i, 0) for i in range(ship_size)]

        if all(0 <= row + r < 7 and 0 <= col + c < 7 and board[row + r][col + c] == 'O' for r, c in ship_cells):
            for r, c in ship_cells:
                board[row + r][col + c] = str(ship_size)
            break

def is_valid_shot(shots_board, row, col):
    return 0 <= row < 7 and 0 <= col < 7 and shots_board[row][col] == 'O'

def player_turn(board, shots_board, player_shots_board):
    while True:
        try:
            move = input("Enter your move (e.g., A:3): ").strip().upper()
            col = ord(move[0]) - ord('A')
            row = int(move[2:]) - 1  # Adjust row index

            if is_valid_shot(shots_board, row, col):
                return row, col
            else:
                print("Invalid move. Try again.")

        except (ValueError, IndexError):
            print("Invalid input format. Please use format like 'A:3'.")

def computer_turn(board, shots_board, player_shots_board):
    computer_row, computer_col = random.randint(0, 6), random.randint(0, 6)

    if board[computer_row][computer_col] != 'O':
        print("Computer hit your ship!")
        board[computer_row][computer_col] = 'X'
        shots_board[computer_row][computer_col] = 'X'
        if all(cell == 'X' for row in board for cell in row):
            print("Computer won!")
            return True
    else:
        print("Computer missed!")
        shots_board[computer_row][computer_col] = '-'
    return False

def place_ships(board):
    for ship_size in [3, 2, 1]:
        place_ship(board, ship_size)

def play_game():
    player_ships_board = create_board()
    computer_ships_board = create_board()
    player_shots_board = create_board()
    computer_shots_board = create_board()

    print("Welcome to Battleship!")
    place_ships(player_ships_board)
    print("\nComputer is placing ships...")
    place_ships(computer_ships_board)

    while True:
        print("\nPlayer's turn:")
        print_board(computer_ships_board, hide_ships=True)
        player_row, player_col = player_turn(computer_ships_board, computer_shots_board, player_shots_board)

        if computer_ships_board[player_row][player_col] != 'O':
            print("Hit!")
            computer_ships_board[player_row][player_col] = 'X'
            player_shots_board[player_row][player_col] = 'X'
            if all(cell == 'X' for row in computer_ships_board for cell in row):
                print("Congratulations! You won!")
                break
        else:
            print("Miss!")
            player_shots_board[player_row][player_col] = '-'

        print("\nComputer's turn:")
        if computer_turn(player_ships_board, computer_shots_board, player_shots_board):
            break

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
play_game()
