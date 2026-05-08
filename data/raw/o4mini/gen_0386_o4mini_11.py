# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 386
# filename        : gen_0386_o4mini_11.py
# timestamp       : 2026-05-07T17:56:33Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 817
# tokens_total    : 1204
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

# Global constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def create_board():
    """Creates and initializes a 2D board with spaces."""
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Clears the screen and prints the current state of the board with column labels."""
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(board, column):
    """Checks if a column is valid and not full."""
    return 0 <= column < COLUMNS and board[0][column] == " "

def get_column_choice():
    """Prompts the player for a column choice, validates input, and returns a valid column index."""
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if len(choice) == 1 and choice in COLUMN_LABELS:
            column = COLUMN_LABELS.index(choice)
            return column
        else:
            print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, column, checker):
    """Drops the player's checker to the lowest available row in the given column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = checker
            return row

def check_winner(board, row, column, checker):
    """Checks if the player has 4 in a row horizontally, vertically, or diagonally."""
    def count_consecutive(dx, dy):
        count = 0
        x, y = column, row
        while 0 <= y < ROWS and 0 <= x < COLUMNS and board[y][x] == checker:
            count += 1
            x += dx
            y += dy
        return count

    # Horizontal, vertical, and two diagonal directions
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        if count_consecutive(dx, dy) + count_consecutive(-dx, -dy) - 1 >= 4:
            return True
    return False

def is_board_full(board):
    """Checks if the board is completely filled."""
    return all(board[0][col] != " " for col in range(COLUMNS))

def main():
    """Main function to handle the game flow."""
    board = create_board()
    players = ["X", "O"]
    current_player = random.randint(0, NUM_PLAYERS - 1)  # Randomly select starting player
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn!")
        column = get_column_choice()

        # Validate column choice
        while not is_valid_column(board, column):
            print("Column is full or invalid. Choose again.")
            column = get_column_choice()

        # Drop checker and update the board
        row = drop_checker(board, column, players[current_player])
        print_board(board)

        # Check for a winner
        if check_winner(board, row, column, players[current_player]):
            print(f"Player {players[current_player]} won!")
            break

        # Check for a draw
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```