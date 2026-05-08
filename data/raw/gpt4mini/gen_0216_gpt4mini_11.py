# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 216
# filename        : gen_0216_gpt4mini_11.py
# timestamp       : 2026-04-06T10:18:13Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 1015
# tokens_total    : 1402
# cost_usd        : 0.000667
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

import os
import random

# Constants for the game
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_MARKS = ['X', 'O']

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def create_board():
    """Creates a 2D list representing the Connect 4 board.

    Returns:
        list: A 2D list initialized with spaces representing empty cells.
    """
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the current state of the board with column labels.

    Args:
        board (list): The current state of the Connect 4 board.
    """
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def get_valid_column():
    """Prompts the user for a valid column letter and returns the corresponding index.

    Returns:
        int: The index of the selected column (0-6).
    """
    while True:
        try:
            column = input(f"Player {PLAYER_MARKS[current_player]}, choose a column (A-G): ").upper()
            if column not in 'ABCDEFG':
                raise ValueError("Invalid input. Please choose a column from A to G.")
            column_index = ord(column) - ord('A')
            if board[0][column_index] != ' ':
                raise ValueError("Column is full. Please choose another column.")
            return column_index
        except ValueError as e:
            print(e)

def drop_checker(board, column_index, player_mark):
    """Drops a checker into the specified column of the board.

    Args:
        board (list): The current state of the Connect 4 board.
        column_index (int): The index of the column to drop the checker into.
        player_mark (str): The mark of the player ('X' or 'O').
    """
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = player_mark
            break

def check_win(board, player_mark):
    """Checks if the specified player has won.

    Args:
        board (list): The current state of the Connect 4 board.
        player_mark (str): The mark of the player ('X' or 'O').

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player_mark for i in range(4)):
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == player_mark for i in range(4)):
                return True

    # Check diagonal \
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player_mark for i in range(4)):
                return True

    # Check diagonal /
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == player_mark for i in range(4)):
                return True

    return False

def check_draw(board):
    """Checks if the board is full and the game is a draw.

    Args:
        board (list): The current state of the Connect 4 board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(cell != ' ' for row in board for cell in row)

def main():
    """Runs the main game loop of Connect 4."""
    global current_player, board
    board = create_board()
    current_player = random.randint(0, 1)

    while True:
        clear_screen()
        print_board(board)
        column_index = get_valid_column()
        drop_checker(board, column_index, PLAYER_MARKS[current_player])

        if check_win(board, PLAYER_MARKS[current_player]):
            clear_screen()
            print_board(board)
            print(f"Player {PLAYER_MARKS[current_player]} won!")
            break

        if check_draw(board):
            clear_screen()
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()