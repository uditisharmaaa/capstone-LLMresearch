# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 434
# filename        : gen_0434_opus46_07.py
# timestamp       : 2026-05-07T22:34:14Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 2540
# tokens_total    : 2960
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

import os
import random

# Constant global variables for board dimensions and number of players
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

# The column labels that players will use to choose a column
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# The two player checkers
CHECKERS = ['X', 'O']


def create_board():
    """
    Create a 2D board (a list of lists) with NUM_ROWS rows and NUM_COLS columns.
    Each cell is initialized with a space character ' '.
    
    We use a list comprehension here:
    - The outer list comprehension creates each row
    - The inner list comprehension creates each cell in that row
    """
    board = []
    for row in range(NUM_ROWS):
        # Create a new row filled with spaces
        new_row = []
        for col in range(NUM_COLS):
            new_row.append(' ')
        board.append(new_row)
    return board


def print_board(board):
    """
    Print the board in a nice formatted way with column labels on top.
    
    The board looks like this:
       A   B   C   D   E   F   G
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    
    We first clear the screen so it looks clean each time.
    """
    # Clear the screen before printing
    os.system('clear')
    
    # Print the column labels with proper spacing
    # We want: "   A   B   C   D   E   F   G"
    header = " "
    for label in COLUMN_LABELS:
        header += "   " + label
    print(header)
    
    # Print the separator line between rows
    separator = "+---" * NUM_COLS + "+"
    
    # Print each row of the board
    for row in range(NUM_ROWS):
        # Print the separator line above each row
        print(separator)
        
        # Print the cells in this row, separated by '|'
        row_string = "|"
        for col in range(NUM_COLS):
            # Each cell is surrounded by spaces and a pipe character
            row_string += " " + board[row][col] + " |"
        print(row_string)
    
    # Print the bottom separator line
    print(separator)


def get_player_move(board, player_checker):
    """
    Ask the current player to input a column letter (A-G).
    
    We validate the input in several ways:
    1. It must be a single letter
    2. It must be between A and G (uppercase)
    3. The chosen column must not be full
    
    If the input is invalid, we ask again (we do NOT end the turn).
    We return the column index (0-6) corresponding to the chosen column.
    """
    while True:
        # Ask the player for their move
        user_input = input("Player " + player_checker + ", choose a column (A-G): ")
        
        # Check if the input is a single alphabetic character
        if not user_input.isalpha() or len(user_input) != 1:
            print("Invalid input. Please enter a single letter from A to G.")
            continue
        
        # Convert to uppercase in case they typed lowercase (but we expect uppercase)
        column_letter = user_input.upper()
        
        # Check if the letter is in our valid column labels
        if column_letter not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter from A to G.")
            continue
        
        # Convert the letter to a column index
        # 'A' -> 0, 'B' -> 1, ..., 'G' -> 6
        col_index = COLUMN_LABELS.index(column_letter)
        
        # Check if the column is full
        # A column is full if the top row (row 0) is not a space
        if board[0][col_index] != ' ':
            print("Column " + column_letter + " is full. Please choose another column.")
            continue
        
        # If we get here, the input is valid!
        return col_index


def drop_checker(board, col_index, checker):
    """
    Drop a checker into the specified column.
    
    The checker should fall to the lowest available row in that column.
    We start from the bottom row (NUM_ROWS - 1) and work our way up
    until we find an empty cell.
    
    Returns the row where the checker was placed.
    """
    # Start from the bottom row and go up
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_index] == ' ':
            # Found an empty spot! Place the checker here.
            board[row][col_index] = checker
            return row
    
    # This should never happen if we validated the column isn't full
    return -1


def check_win(board, checker):
    """
    Check if the given checker has won the game.
    
    A player wins by getting 4 of their checkers in a row:
    - Horizontally (left to right)
    - Vertically (top to bottom)
    - Diagonally (both directions: top-left to bottom-right, and top-right to bottom-left)
    
    We check every possible starting position for each direction.
    """
    
    # Check horizontal wins
    # We only need to start from columns 0 to NUM_COLS - 4
    # because we need 4 in a row
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            # Check if four consecutive cells in this row match the checker
            if (board[row][col] == checker and
                board[row][col + 1] == checker and
                board[row][col + 2] == checker and
                board[row][col + 3] == checker):
                return True
    
    # Check vertical wins
    # We only need to start from rows 0 to NUM_ROWS - 4
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            # Check if four consecutive cells in this column match the checker
            if (board[row][col] == checker and
                board[row + 1][col] == checker and
                board[row + 2][col] == checker and
                board[row + 3][col] == checker):
                return True
    
    # Check diagonal wins (top-left to bottom-right direction: \)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker and
                board[row + 1][col + 1] == checker and
                board[row + 2][col + 2] == checker and
                board[row + 3][col + 3] == checker):
                return True
    
    # Check diagonal wins (top-right to bottom-left direction: /)
    for row in range(NUM_ROWS - 3):
        for col in range(3, NUM_COLS):
            if (board[row][col] == checker and
                board[row + 1][col - 1] == checker and
                board[row + 2][col - 2] == checker and
                board[row + 3][col - 3] == checker):
                return True
    
    # No win found
    return False


def is_board_full(board):
    """
    Check if the board is completely full (no empty spaces left).
    
    We only need to check the top row (row 0) because checkers
    are dropped from the top. If the top row has no spaces,
    then all columns are full.
    """
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            # Found an empty spot, so the board is not full
            return False
    return True


def main():
    """
    The main function that runs the Connect 4 game.
    
    Steps:
    1. Create the board
    2. Randomly select which player goes first
    3. Loop: print board, get move, drop checker, check for win/draw
    4. End the game when someone wins or the board is full
    """
    # Step 1: Create an empty board
    board = create_board()
    
    # Step 2: Randomly select which player goes first
    # We randomly choose 0 or 1 to pick the starting player
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    # Print the initial empty board
    print_board(board)
    print("Player " + CHECKERS[current_player] + " goes first!")
    
    # Step 3: Main game loop
    while True:
        # Get the current player's checker ('X' or 'O')
        current_checker = CHECKERS[current_player]
        
        # Ask the player for their move (with input validation)
        col_index = get_player_move(board, current_checker)
        
        # Drop the checker into the chosen column
        drop_checker(board, col_index, current_checker)
        
        # Print the updated board
        print_board(board)
        
        # Check if the current player has won
        if check_win(board, current_checker):
            print("Player " + current_checker + " won!")
            break
        
        # Check if the board is full (draw)
        if is_board_full(board):
            print("It's a draw! The board is full with no winner.")
            break
        
        # Switch to the other player
        # If current_player is 0, it becomes 1
        # If current_player is 1, it becomes 0
        current_player = (current_player + 1) % NUM_PLAYERS


# This is the standard way to run the main function in Python.
# The code below checks if this file is being run directly
# (not imported as a module), and if so, calls main().
if __name__ == "__main__":
    main()