# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 326
# filename        : gen_0326_o4mini_11.py
# timestamp       : 2026-05-07T17:34:33Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 910
# tokens_total    : 1297
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
#   Write with extensive docstrings for every function.
# ====================================================================

```python
import os
import random

# Constants
BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2
COLUMN_LABELS = ["A", "B", "C", "D", "E", "F", "G"]
PLAYER_CHECKERS = ["X", "O"]

def clear_screen():
    """Clears the console screen."""
    os.system('clear')

def create_board():
    """Creates and initializes the Connect 4 board."""
    return [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    """Prints the current state of the game board."""
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * BOARD_COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * BOARD_COLS + "+")

def is_column_full(board, col):
    """Checks if a column is full."""
    return board[0][col] != " "

def get_column_index(input_char):
    """Converts a column letter to its corresponding index."""
    return COLUMN_LABELS.index(input_char)

def drop_checker(board, col, checker):
    """Drops a checker in the specified column."""
    for row in reversed(board):
        if row[col] == " ":
            row[col] = checker
            break

def is_valid_input(input_char, board):
    """Validates user input."""
    if input_char not in COLUMN_LABELS:
        return False
    col_index = get_column_index(input_char)
    if is_column_full(board, col_index):
        return False
    return True

def check_winner(board, checker):
    """Checks if the given checker has won the game."""
    # Check horizontal
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True
    # Check vertical
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(is_column_full(board, col) for col in range(BOARD_COLS))

def get_player_input(board, player_checker):
    """Prompts the player to input a column and validates the input."""
    while True:
        user_input = input(f"Player {player_checker}, choose a column (A-G): ").strip().upper()
        if is_valid_input(user_input, board):
            return get_column_index(user_input)
        print("Invalid input. Please try again.")

def main():
    """Main function to run the Connect 4 game."""
    # Initialize the game
    board = create_board()
    current_player = random.choice(range(NUM_PLAYERS))  # Randomly select starting player
    print_board(board)

    while True:
        # Get player input and make a move
        player_checker = PLAYER_CHECKERS[current_player]
        col = get_player_input(board, player_checker)
        drop_checker(board, col, player_checker)
        print_board(board)

        # Check for a winner
        if check_winner(board, player_checker):
            print(f"Player {player_checker} won!")
            break

        # Check for a draw
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```