# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 464
# filename        : gen_0464_o4mini_07.py
# timestamp       : 2026-05-07T22:43:40Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 392
# tokens_output   : 793
# tokens_total    : 1185
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

# Initialize the board
def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

# Print the board
def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

# Check if a column is full
def is_column_full(board, col):
    return board[0][col] != " "

# Drop the checker in the chosen column
def drop_checker(board, col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = checker
            return

# Check for a win
def check_win(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (down-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (up-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

# Check if the board is full
def is_draw(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

# Get valid column input from the player
def get_player_input(board, player):
    while True:
        choice = input(f"Player {player} ({player_checkers[player]}), choose a column (A-G): ").strip().upper()
        if choice in COLUMN_LABELS:
            col = COLUMN_LABELS.index(choice)
            if not is_column_full(board, col):
                return col
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please choose a column between A and G.")

# Main game function
def play_game():
    board = create_board()
    print_board(board)

    # Randomly choose which player starts
    current_player = random.randint(0, PLAYERS - 1)
    print(f"Player {current_player + 1} ({player_checkers[current_player]}) goes first!")

    while True:
        col = get_player_input(board, current_player)
        drop_checker(board, col, player_checkers[current_player])
        print_board(board)

        if check_win(board, player_checkers[current_player]):
            print(f"Player {current_player + 1} ({player_checkers[current_player]}) won!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 1 - current_player

# Player checkers
player_checkers = ["X", "O"]

# Run the game
if __name__ == "__main__":
    play_game()
```