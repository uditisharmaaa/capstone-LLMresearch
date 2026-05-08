# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 460
# filename        : gen_0460_o4mini_03.py
# timestamp       : 2026-05-07T22:42:52Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 888
# tokens_total    : 1275
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

```python
import os
import random

# Global constants for board dimensions and players
ROWS = 6
COLUMNS = 7
PLAYERS = 2

# Function to create an empty Connect 4 board
def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

# Function to print the board with column labels
def print_board(board):
    os.system('clear')  # Clear the screen
    # Print column labels
    print("   " + "   ".join(chr(65 + i) for i in range(COLUMNS)))
    print("+---" * COLUMNS + "+")
    # Print each row of the board
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

# Function to check if a column is valid and has space
def is_valid_column(board, column):
    return 0 <= column < COLUMNS and board[0][column] == " "

# Function to drop a checker into the lowest available row in a column
def drop_checker(board, column, checker):
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row
        if board[row][column] == " ":
            board[row][column] = checker  # Place the checker
            return row, column  # Return the position of the checker

# Function to check for a win in all directions
def check_win(board, row, col, checker):
    # Helper to count consecutive checkers in a direction
    def count_in_direction(delta_row, delta_col):
        count = 0
        r, c = row, col
        while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == checker:
            count += 1
            r += delta_row
            c += delta_col
        return count

    # Check all four directions: horizontal, vertical, and two diagonals
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        if count_in_direction(dr, dc) + count_in_direction(-dr, -dc) - 1 >= 4:
            return True
    return False

# Function to check if the board is full
def is_draw(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

# Main game function
def connect_4():
    # Create the board
    board = create_board()

    # Randomly select which player goes first
    current_player = random.randint(0, PLAYERS - 1)
    checkers = ["X", "O"]

    # Print the initial board
    print_board(board)

    # Main game loop
    while True:
        # Get the current player's checker
        checker = checkers[current_player]

        # Prompt the player for a column until valid input is received
        while True:
            move = input(f"Player {current_player + 1} ({checker}), choose a column (A-G): ").strip()
            if len(move) == 1 and move.isalpha():  # Ensure input is a single letter
                column = ord(move.upper()) - 65  # Convert A-G to 0-6
                if is_valid_column(board, column):  # Check if the column is valid
                    break
            print("Invalid move. Try again.")

        # Drop the checker into the chosen column
        row, col = drop_checker(board, column, checker)

        # Print the board after the move
        print_board(board)

        # Check if the current player wins
        if check_win(board, row, col, checker):
            print(f"Player {current_player + 1} ({checker}) won!")
            break

        # Check for a draw
        if is_draw(board):
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = (current_player + 1) % PLAYERS

# Run the game
if __name__ == "__main__":
    connect_4()
```