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
    print("-" * 44)
    print("+---+---+---+")
    print(f"| {game_board[0]} | {game_board[1]} | {game_board[2]} |")
    print("+---+---+---+")
    print(f"| {game_board[3]} | {game_board[4]} | {game_board[5]} |")
    print("+---+---+---+")
    print(f"| {game_board[6]} | {game_board[7]} | {game_board[8]} |")
    print("+---+---+---+")
    print(DOUBLE_SEPARATOR)