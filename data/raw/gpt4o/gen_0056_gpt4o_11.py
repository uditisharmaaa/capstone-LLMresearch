# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 56
# filename        : gen_0056_gpt4o_11.py
# timestamp       : 2026-02-19T20:48:02Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 894
# tokens_total    : 1281
# cost_usd        : 0.009907
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

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    """Clear the console screen."""
    os.system('clear')

def initialize_board():
    """Create a 2D list to represent the Connect 4 board."""
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Print the Connect 4 board with column labels."""
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLUMNS + '+')
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+---' * COLUMNS + '+')

def get_column_index(column_letter):
    """Convert a column letter (A-G) to a column index (0-6)."""
    return COLUMN_LABELS.index(column_letter)

def is_valid_input(column):
    """Check if the user input is a valid column letter."""
    return column in COLUMN_LABELS

def is_column_full(board, column_index):
    """Check if a column is full."""
    return board[0][column_index] != ' '

def get_player_input(board):
    """Prompt the player for a valid column input and return the column index."""
    while True:
        column = input("Choose a column (A-G): ").strip().upper()
        if not is_valid_input(column):
            print("Invalid input. Please enter a letter between A and G.")
        else:
            column_index = get_column_index(column)
            if is_column_full(board, column_index):
                print("Column is full. Choose another column.")
            else:
                return column_index

def drop_checker(board, column_index, player_symbol):
    """Drop a checker into the lowest available row in the chosen column."""
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = player_symbol
            break

def check_for_win(board, player_symbol):
    """Check if there's a win condition for the given player symbol."""
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == player_symbol for i in range(4)):
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player_symbol for i in range(4)):
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == player_symbol for i in range(4)):
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == player_symbol for i in range(4)):
                return True
    return False

def is_draw(board):
    """Check if the board is full, resulting in a draw."""
    return all(cell != ' ' for row in board for cell in row)

def main():
    """Main function to run the Connect 4 game."""
    board = initialize_board()
    current_player = random.randint(0, PLAYERS - 1)
    print_board(board)

    while True:
        print(f"Player {PLAYER_SYMBOLS[current_player]}'s turn.")
        column_index = get_player_input(board)
        drop_checker(board, column_index, PLAYER_SYMBOLS[current_player])
        print_board(board)

        if check_for_win(board, PLAYER_SYMBOLS[current_player]):
            print(f"{PLAYER_SYMBOLS[current_player]} won!")
            break

        if is_draw(board):
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()