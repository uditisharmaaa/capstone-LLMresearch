# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 479
# filename        : gen_0479_opus_07.py
# timestamp       : 2026-05-07T22:48:17Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 2515
# tokens_total    : 2935
# cost_usd        : 0.194925
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
# Using uppercase names is a Python convention for constants
ROWS = 6
COLUMNS = 7
NUM_PLAYERS = 2

# The two player checkers
PLAYER_CHECKERS = ["X", "O"]


def create_board():
    """
    Create and return an empty game board.
    
    We use a 2D list (a list of lists) to represent the board.
    Each cell is initialized with a space character " " to show it's empty.
    
    The board has ROWS rows and COLUMNS columns.
    """
    # We create ROWS number of rows, each containing COLUMNS spaces
    board = []
    for row in range(ROWS):
        # Create a new row with COLUMNS empty spaces
        new_row = []
        for col in range(COLUMNS):
            new_row.append(" ")
        board.append(new_row)
    return board


def print_board(board):
    """
    Print the current state of the board with column labels.
    
    First, we clear the screen so the game looks clean.
    Then we print column labels A through G.
    Finally, we print each row with separators.
    """
    # Clear the screen - 'clear' works on Mac/Linux
    os.system('clear')
    
    # Print column labels (A through G)
    # We use chr() to convert numbers to letters: chr(65) = 'A', chr(66) = 'B', etc.
    header = "   "  # Start with some spacing
    for col in range(COLUMNS):
        # 65 is the ASCII code for 'A'
        header += chr(65 + col) + "   "
    print(header)
    
    # Print the top border
    print("+---" * COLUMNS + "+")
    
    # Print each row with its contents
    for row in range(ROWS):
        # Start building the row string
        row_string = "|"
        for col in range(COLUMNS):
            # Add the cell content surrounded by spaces and a separator
            row_string += " " + board[row][col] + " |"
        print(row_string)
        # Print the border after each row
        print("+---" * COLUMNS + "+")


def get_column_choice(player, board):
    """
    Ask the player to choose a column and validate their input.
    
    This function keeps asking until the player gives valid input.
    Valid input means:
    1. It must be a single letter
    2. It must be between A and G (uppercase)
    3. The chosen column must not be full
    
    Returns the column index (0-6) for the chosen column.
    """
    while True:  # Keep asking until we get valid input
        # Ask the player for their choice
        user_input = input(f"Player {player}, choose a column (A-G): ")
        
        # Check if input is exactly one character
        if len(user_input) != 1:
            print("Please enter a single letter from A to G.")
            continue  # Go back to the start of the while loop
        
        # Check if the input is a letter
        if not user_input.isalpha():
            print("Please enter a letter, not a number or symbol.")
            continue
        
        # Convert to uppercase for consistency
        user_input = user_input.upper()
        
        # Check if the letter is in the valid range A-G
        if user_input < 'A' or user_input > 'G':
            print("Please enter a letter between A and G.")
            continue
        
        # Convert the letter to a column index
        # ord() gives us the ASCII code: ord('A') = 65, ord('B') = 66, etc.
        # So ord(letter) - ord('A') gives us 0 for A, 1 for B, etc.
        column_index = ord(user_input) - ord('A')
        
        # Check if the column is full
        # A column is full if the top row (row 0) is not empty
        if board[0][column_index] != " ":
            print("That column is full. Please choose another column.")
            continue
        
        # If we get here, the input is valid!
        return column_index


def drop_checker(board, column, checker):
    """
    Drop a checker into the specified column.
    
    The checker falls to the lowest available row, just like in real Connect 4.
    We start from the bottom row and work our way up to find the first empty spot.
    
    Returns the row where the checker landed.
    """
    # Start from the bottom row (ROWS - 1) and go up to row 0
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            # Found an empty spot! Place the checker here.
            board[row][column] = checker
            return row
    
    # This should never happen if we validate input correctly
    return -1


def check_winner(board, row, col, checker):
    """
    Check if the last move resulted in a win.
    
    A player wins by getting 4 of their checkers in a row:
    - Horizontally (left-right)
    - Vertically (up-down)
    - Diagonally (both directions)
    
    We check all four directions from the last placed checker.
    """
    # Define the four directions to check
    # Each direction is represented as (row_change, col_change)
    directions = [
        (0, 1),   # Horizontal: left-right
        (1, 0),   # Vertical: up-down
        (1, 1),   # Diagonal: top-left to bottom-right
        (1, -1)   # Diagonal: top-right to bottom-left
    ]
    
    for row_dir, col_dir in directions:
        # Count checkers in both directions from the current position
        count = 1  # Start with 1 for the checker we just placed
        
        # Check in the positive direction
        count += count_in_direction(board, row, col, row_dir, col_dir, checker)
        
        # Check in the negative direction (opposite direction)
        count += count_in_direction(board, row, col, -row_dir, -col_dir, checker)
        
        # If we found 4 or more in a row, it's a win!
        if count >= 4:
            return True
    
    return False


def count_in_direction(board, start_row, start_col, row_dir, col_dir, checker):
    """
    Count consecutive checkers in a specific direction.
    
    Starting from (start_row, start_col), we move in the direction
    specified by (row_dir, col_dir) and count matching checkers.
    
    We don't count the starting position itself.
    """
    count = 0
    current_row = start_row + row_dir
    current_col = start_col + col_dir
    
    # Keep going while we're on the board and finding matching checkers
    while True:
        # Check if we're still within the board boundaries
        if current_row < 0 or current_row >= ROWS:
            break
        if current_col < 0 or current_col >= COLUMNS:
            break
        
        # Check if the current cell has our checker
        if board[current_row][current_col] != checker:
            break
        
        # Found a matching checker! Increment count and move to next cell
        count += 1
        current_row += row_dir
        current_col += col_dir
    
    return count


def is_board_full(board):
    """
    Check if the board is completely full (no empty spaces).
    
    We only need to check the top row - if it's full, all columns are full.
    """
    for col in range(COLUMNS):
        if board[0][col] == " ":
            return False  # Found an empty space, board is not full
    return True  # No empty spaces found, board is full


def play_game():
    """
    Main game function that runs the Connect 4 game.
    
    This function:
    1. Creates the board
    2. Randomly selects who goes first
    3. Alternates turns between players
    4. Checks for wins and draws
    5. Ends the game when there's a winner or draw
    """
    # Create a fresh board
    board = create_board()
    
    # Randomly select which player goes first (0 or 1)
    # random.randint(0, 1) returns either 0 or 1
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    
    # Print the initial empty board
    print_board(board)
    
    # Main game loop
    while True:
        # Get the current player's checker (X or O)
        current_checker = PLAYER_CHECKERS[current_player_index]
        
        # Get the player's column choice
        column = get_column_choice(current_checker, board)
        
        # Drop the checker and get the row where it landed
        row = drop_checker(board, column, current_checker)
        
        # Print the updated board
        print_board(board)
        
        # Check if this move won the game
        if check_winner(board, row, column, current_checker):
            print(f"{current_checker} won!")
            break  # End the game
        
        # Check if the board is full (draw)
        if is_board_full(board):
            print("It's a draw! The board is full with no winner.")
            break  # End the game
        
        # Switch to the other player
        # If current_player_index is 0, it becomes 1
        # If current_player_index is 1, it becomes 0
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


# This is the entry point of our program
# The code below only runs if we execute this file directly
# (not if we import it as a module)
if __name__ == "__main__":
    play_game()