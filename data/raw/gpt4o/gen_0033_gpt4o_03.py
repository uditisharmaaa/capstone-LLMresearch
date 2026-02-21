# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 33
# filename        : gen_0033_gpt4o_03.py
# timestamp       : 2026-02-19T20:43:21Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 891
# tokens_total    : 1278
# cost_usd        : 0.009877
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

```python
import os
import random

# Constants for the board dimensions and number of players
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2

# Symbols for the players
PLAYER_SYMBOLS = ['X', 'O']

def create_board():
    """Initialize the board with spaces."""
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Clear the screen and print the board with labels."""
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_column(column):
    """Check if the column input is valid."""
    return column in 'ABCDEFG'

def is_column_full(board, column):
    """Check if the chosen column is full."""
    col_index = ord(column) - ord('A')
    return board[0][col_index] != ' '

def get_next_open_row(board, col_index):
    """Get the next open row in the chosen column."""
    for r in range(ROWS-1, -1, -1):
        if board[r][col_index] == ' ':
            return r
    return None

def place_checker(board, row, col_index, player):
    """Place the player's checker into the board."""
    board[row][col_index] = PLAYER_SYMBOLS[player]

def check_for_win(board, player):
    """Check the board for a win condition."""
    symbol = PLAYER_SYMBOLS[player]
    # Check horizontal locations
    for r in range(ROWS):
        for c in range(COLUMNS-3):
            if all(board[r][c+i] == symbol for i in range(4)):
                return True

    # Check vertical locations
    for c in range(COLUMNS):
        for r in range(ROWS-3):
            if all(board[r+i][c] == symbol for i in range(4)):
                return True

    # Check positively sloped diagonals
    for r in range(ROWS-3):
        for c in range(COLUMNS-3):
            if all(board[r+i][c+i] == symbol for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for r in range(3, ROWS):
        for c in range(COLUMNS-3):
            if all(board[r-i][c+i] == symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    """Check if the board is full without a winner."""
    return all(board[0][c] != ' ' for c in range(COLUMNS))

def main():
    """Main game loop."""
    board = create_board()
    print_board(board)

    # Randomly select which player goes first
    current_player = random.randint(0, NUM_PLAYERS - 1)

    while True:
        # Prompt the player for input
        column = input(f"Player {PLAYER_SYMBOLS[current_player]}, choose a column (A-G): ").strip().upper()

        # Validate input
        if not is_valid_column(column):
            print("Invalid column. Please choose a column A-G.")
            continue

        col_index = ord(column) - ord('A')

        if is_column_full(board, column):
            print("Column is full. Choose another column.")
            continue

        # Place the checker
        row = get_next_open_row(board, col_index)
        place_checker(board, row, col_index, current_player)

        # Print the board after the move
        print_board(board)

        # Check for a win
        if check_for_win(board, current_player):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break

        # Check for a draw
        if is_draw(board):
            print("The game is a draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```