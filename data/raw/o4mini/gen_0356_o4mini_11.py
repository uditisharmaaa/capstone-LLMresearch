# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 356
# filename        : gen_0356_o4mini_11.py
# timestamp       : 2026-05-07T17:47:49Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 971
# tokens_total    : 1358
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
ROWS = 6
COLS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Creates and returns a new Connect 4 board initialized with spaces."""
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Clears the screen and prints the current state of the board."""
    os.system('clear')  # Clear the screen
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(choice, board):
    """
    Checks if the column choice is valid.
    Returns True if the column exists and is not full, False otherwise.
    """
    if choice not in COLUMN_LABELS:
        return False
    col_index = COLUMN_LABELS.index(choice)
    return board[0][col_index] == ' '

def drop_checker(board, column, player_checker):
    """
    Drops the player's checker into the specified column.
    Updates the board and returns the modified board.
    """
    col_index = COLUMN_LABELS.index(column)
    for row in range(ROWS - 1, -1, -1):  # Start from the bottom row
        if board[row][col_index] == ' ':
            board[row][col_index] = player_checker
            return board

def check_winner(board, player_checker):
    """
    Checks if the player has won after their move.
    Returns True if the player has 4 in a row (horizontally, vertically, or diagonally), False otherwise.
    """
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player_checker for i in range(4)):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_checker for i in range(4)):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player_checker for i in range(4)):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player_checker for i in range(4)):
                return True

    return False

def is_draw(board):
    """
    Checks if the board is completely filled with no winner.
    Returns True if the game is a draw, False otherwise.
    """
    return all(board[0][col] != ' ' for col in range(COLS))

def get_player_choice(board):
    """
    Prompts the current player for a valid column choice.
    Validates the input and returns the chosen column.
    """
    while True:
        choice = input("Choose a column (A-G): ").strip().upper()
        if is_valid_column(choice, board):
            return choice
        print("Invalid choice. Please try again.")

def main():
    """
    Main function to set up and run the Connect 4 game.
    Handles game logic, player turns, and win/draw conditions.
    """
    board = create_board()
    players = ['X', 'O']
    current_player = random.randint(0, PLAYERS - 1)  # Randomly select who starts first

    print_board(board)
    print(f"Player {players[current_player]} goes first!")

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        column = get_player_choice(board)
        board = drop_checker(board, column, players[current_player])

        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} won!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()
```