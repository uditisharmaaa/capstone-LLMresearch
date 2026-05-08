# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 416
# filename        : gen_0416_o4mini_11.py
# timestamp       : 2026-05-07T19:16:07Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 787
# tokens_total    : 1174
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

# Constants for the game
ROWS = 6
COLS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def clear_screen():
    """Clears the console screen."""
    os.system('clear')

def create_board():
    """Creates and returns an empty Connect 4 board."""
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(column, board):
    """Checks if the chosen column is valid (not full and within range)."""
    if column not in COLUMN_LABELS:
        return False
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] == " "

def drop_checker(board, column, checker):
    """Drops the checker into the lowest available row of the chosen column."""
    col_index = COLUMN_LABELS.index(column)
    for row in reversed(board):
        if row[col_index] == " ":
            row[col_index] = checker
            return

def check_win(board, checker):
    """Checks if the given player has won the game."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (\)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (/)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

def check_draw(board):
    """Checks if the board is full, resulting in a draw."""
    return all(board[0][col] != " " for col in range(COLS))

def get_player_move(board):
    """Prompts the current player to input a valid column."""
    while True:
        column = input("Choose a column (A-G): ").strip().upper()
        if is_valid_column(column, board):
            return column
        print("Invalid input. Please choose a valid column.")

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)

    print_board(board)
    print(f"{current_player} goes first!")

    while True:
        print_board(board)
        print(f"{current_player}'s turn.")
        column = get_player_move(board)
        drop_checker(board, column, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} won!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    main()
```