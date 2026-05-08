# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 440
# filename        : gen_0440_o4mini_13.py
# timestamp       : 2026-05-07T22:35:55Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 387
# tokens_output   : 740
# tokens_total    : 1127
# cost_usd        : 0.000000
# --------------------------------------------------------------------
# full_prompt:
#   You are a first-year computer science student completing a programming assignment. Write a complete Python3 implementation of the Connect 4 game with the following requirements:
#   
#   1. Create a 2D board with 7 columns and 6 rows, initialized with spaces
#   2. Support exactly 2 players using checkers "X" and "O"
#   3. Use constant global variables for board dimensions and number of players
#   4. Randomly select which player goes first at the start
#   5. Print the board with column labels A through G before the game starts and after each turn
#   6. Clear the screen before printing using os.system('clear')
#   7. Players input an uppercase letter (A-G) to choose a column
#   8. Validate all input: reject letters outside A-G, reject full columns, reject non-letter input - do NOT end the turn on invalid input, ask again
#   9. Drop the checker to the lowest available row in the chosen column
#   10. After each move, check for a win: 4 in a row horizontally, vertically, or diagonally
#   11. If the board fills with no winner, declare a draw
#   12. When a player wins, print "[Player] won!" and end the game
#   
#   The board must look exactly like this format:
#      A   B   C   D   E   F   G
#   +---+---+---+---+---+---+---+
#   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+
#   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+
#   
#   Provide ONLY the complete Python code. No explanations, no markdown code blocks, just raw Python code starting with import statements.
#   
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

```python
import os
import random

# Constants for the board dimensions and number of players
ROWS = 6
COLUMNS = 7
PLAYERS = 2

# Create the board
def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

# Print the board
def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

# Check for a win condition
def check_win(board, player):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

# Check if the board is full
def is_full(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

# Drop a checker in the chosen column
def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return

# Validate input
def validate_input(choice, board):
    if len(choice) != 1 or choice < 'A' or choice > 'G':
        return False
    col = ord(choice) - ord('A')
    if board[0][col] != " ":
        return False
    return True

# Main game loop
def play_game():
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    print_board(board)

    while True:
        print(f"{current_player}'s turn. Choose a column (A-G):")
        while True:
            choice = input().strip().upper()
            if validate_input(choice, board):
                break
            print("Invalid choice. Please choose a valid column (A-G):")

        col = ord(choice) - ord('A')
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"{current_player} won!")
            break

        if is_full(board):
            print("The game is a draw!")
            break

        current_player = "X" if current_player == "O" else "O"

# Run the game
if __name__ == "__main__":
    play_game()
```