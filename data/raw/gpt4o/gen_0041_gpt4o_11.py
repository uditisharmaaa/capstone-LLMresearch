# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 41
# filename        : gen_0041_gpt4o_11.py
# timestamp       : 2026-02-19T20:45:01Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 792
# tokens_total    : 1179
# cost_usd        : 0.008887
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
NUM_ROWS = 6
NUM_COLUMNS = 7
NUM_PLAYERS = 2
PLAYER_SYMBOLS = ['X', 'O']
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    """Create and return an empty Connect 4 board."""
    return [[' ' for _ in range(NUM_COLUMNS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Clear the screen and print the current state of the board with column labels."""
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * NUM_COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * NUM_COLUMNS + "+")

def get_column_choice(player):
    """Prompt the player to choose a column and return the column index."""
    while True:
        choice = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if choice in COLUMN_LABELS:
            column_index = COLUMN_LABELS.index(choice)
            if board[0][column_index] == ' ':
                return column_index
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please choose a valid column (A-G).")

def drop_checker(board, column, player_symbol):
    """Drop the player's checker into the chosen column."""
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player_symbol
            break

def check_for_win(board, player_symbol):
    """Check the board for a win condition for the current player."""
    # Check horizontal locations
    for r in range(NUM_ROWS):
        for c in range(NUM_COLUMNS - 3):
            if all(board[r][c+i] == player_symbol for i in range(4)):
                return True

    # Check vertical locations
    for c in range(NUM_COLUMNS):
        for r in range(NUM_ROWS - 3):
            if all(board[r+i][c] == player_symbol for i in range(4)):
                return True

    # Check positively sloped diagonals
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLUMNS - 3):
            if all(board[r+i][c+i] == player_symbol for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for r in range(3, NUM_ROWS):
        for c in range(NUM_COLUMNS - 3):
            if all(board[r-i][c+i] == player_symbol for i in range(4)):
                return True

    return False

def is_draw(board):
    """Check if the board is full, indicating a draw."""
    return all(board[0][c] != ' ' for c in range(NUM_COLUMNS))

def main():
    """Main function to run the Connect 4 game."""
    global board
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)

    while True:
        print_board(board)
        column = get_column_choice(current_player + 1)
        drop_checker(board, column, PLAYER_SYMBOLS[current_player])

        if check_for_win(board, PLAYER_SYMBOLS[current_player]):
            print_board(board)
            print(f"Player {current_player + 1} ({PLAYER_SYMBOLS[current_player]}) won!")
            break

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
