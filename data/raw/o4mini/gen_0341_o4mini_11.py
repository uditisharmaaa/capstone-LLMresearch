# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 341
# filename        : gen_0341_o4mini_11.py
# timestamp       : 2026-05-07T17:40:00Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 1307
# tokens_total    : 1694
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
COLS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
EMPTY_CELL = ' '

def create_board():
    """
    Create and initialize the Connect 4 board as a 2D list.
    Each cell is initialized with a space character.
    Returns:
        list: A 2D list representing the board.
    """
    return [[EMPTY_CELL for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """
    Clear the screen and print the current state of the board.
    The board includes column labels and grid lines.
    Args:
        board (list): The current state of the board.
    """
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(column):
    """
    Check if the column input is valid (A-G).
    Args:
        column (str): The column input from the player.
    Returns:
        bool: True if valid, False otherwise.
    """
    return column in COLUMN_LABELS

def is_column_full(board, col_index):
    """
    Check if a column is full (no empty spaces).
    Args:
        board (list): The current state of the board.
        col_index (int): The index of the column to check.
    Returns:
        bool: True if the column is full, False otherwise.
    """
    return board[0][col_index] != EMPTY_CELL

def get_next_open_row(board, col_index):
    """
    Find the next available row in the specified column.
    Args:
        board (list): The current state of the board.
        col_index (int): The index of the column to check.
    Returns:
        int: The index of the next open row, or None if the column is full.
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col_index] == EMPTY_CELL:
            return row
    return None

def drop_checker(board, row, col_index, checker):
    """
    Place a checker in the specified position on the board.
    Args:
        board (list): The current state of the board.
        row (int): The row index where the checker should be placed.
        col_index (int): The column index where the checker should be placed.
        checker (str): The checker's symbol ("X" or "O").
    """
    board[row][col_index] = checker

def check_winner(board, checker):
    """
    Check if the specified player has won the game.
    Args:
        board (list): The current state of the board.
        checker (str): The checker's symbol ("X" or "O").
    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

def is_draw(board):
    """
    Check if the game is a draw (board is full with no winner).
    Args:
        board (list): The current state of the board.
    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return all(board[0][col] != EMPTY_CELL for col in range(COLS))

def get_player_input():
    """
    Prompt the player to input a column letter.
    Returns:
        str: The validated column letter.
    """
    while True:
        column = input("Choose a column (A-G): ").strip().upper()
        if len(column) == 1 and column in COLUMN_LABELS:
            return column
        print("Invalid input. Please enter a letter between A and G.")

def play_game():
    """
    Main function to play the Connect 4 game.
    """
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    print(f"Player {current_player} goes first!")

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get and validate player input
        col_index = None
        while col_index is None:
            column = get_player_input()
            col_index = COLUMN_LABELS.index(column)
            if is_column_full(board, col_index):
                print("Column is full. Try a different column.")
                col_index = None

        # Drop the checker and check for win/draw
        row = get_next_open_row(board, col_index)
        drop_checker(board, row, col_index, current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch to the other player
        current_player = "X" if current_player == "O" else "O"

# Run the game
if __name__ == "__main__":
    play_game()
```