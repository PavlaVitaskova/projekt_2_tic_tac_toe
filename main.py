"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie
author: Pavla Vitaskova
email: pavlavitaskova.pv@gmail.com
discord: pavlavitaskova_29682
"""

DOUBLE_SEPARATOR = 44 * "="
SIMPLE_SEPARATOR = 44 * "-"

# Introductory game text
print(f"""
Welcome to Tic Tac Toe
{DOUBLE_SEPARATOR}
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
{DOUBLE_SEPARATOR}
Let's start the game
{SIMPLE_SEPARATOR}
""")

# Function to draw the game board
def draw_the_game_board(game_board):
    print("+---+---+---+")
    print(f"| {game_board[0]} | {game_board[1]} | {game_board[2]} |")
    print("+---+---+---+")
    print(f"| {game_board[3]} | {game_board[4]} | {game_board[5]} |")
    print("+---+---+---+")
    print(f"| {game_board[6]} | {game_board[7]} | {game_board[8]} |")
    print("+---+---+---+")
    print(DOUBLE_SEPARATOR)

# Check for a winning combination
def check_win(game_board, player):
    winning_combinations = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal top-left to bottom-right
        (2, 4, 6)   # diagonal top-right to bottom-left
    ]

    for a, b, c in winning_combinations:
        if game_board[a] == game_board[b] == game_board[c] == player:
            return True

    return False

# Ask player for a valid move
def get_move(player, game_board):
    while True:
        print(f"Player {player} | Please enter your move number (1-9):")
        entry = input().strip()

        # Check if input is a digit
        if not entry.isdigit():
            print("❗ Enter a valid number (1-9).")
            continue

        move = int(entry)

        # Check range
        if move < 1 or move > 9:
            print("Enter a number between 1 and 9.")
            continue

        # Check if the position is available
        if game_board[move - 1] != " ":
            print("This field is already taken.")
            continue

        return move - 1

# Main function    
def play_game():
    # Create a blank game board with 9 spaces
    game_board = [" "] * 9

    # Set the starting player to "O"
    current_player = "O"

    # Track the number of moves made
    moves = 0

    # Main game loop
    while True:
        # Show current state of the game board
        draw_the_game_board(game_board)

        # Ask the current player for their move
        position = get_move(current_player, game_board)

        # Save the move to the game board
        game_board[position] = current_player

        # Increase the number of moves made
        moves += 1

        # Check if the current player has won
        if check_win(game_board, current_player):
            draw_the_game_board(game_board)
            print(f"Congratulations! Player {current_player} WON!")
            print(DOUBLE_SEPARATOR)
            break

        # If all fields are filled and no winner, it's a draw
        elif moves == 9:
            draw_the_game_board(game_board)
            print("It's a draw! No one won.")
            print(DOUBLE_SEPARATOR)
            break

        # Switch player
        if current_player == "O":
            current_player = "X"
        else:
            current_player = "O"

# Play again prompt
def ask_play_again():
    print("Do you want to play again? (y/n)")
    response = input().strip().lower()
    return response in ["y", "yes"]

# Program entry point
if __name__ == "__main__":
    while True:
        play_game()
        if not ask_play_again():
            print("Thanks for playing!")
            break
