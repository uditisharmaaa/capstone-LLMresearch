# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 475
# filename        : gen_0475_opus_03.py
# timestamp       : 2026-05-07T22:47:04Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 2784
# tokens_total    : 3199
# cost_usd        : 0.215025
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

import os
import random

# Global constants for board dimensions and player count
NUM_COLUMNS = 7  # Number of columns in the Connect 4 board (A through G)
NUM_ROWS = 6     # Number of rows in the Connect 4 board
NUM_PLAYERS = 2  # Number of players in the game

# Player checker symbols
PLAYER_CHECKERS = ["X", "O"]  # X for player 1, O for player 2

# Column labels for the board display
COLUMN_LABELS = ["A", "B", "C", "D", "E", "F", "G"]


def create_board():
    """
    Creates and returns an empty Connect 4 board.
    The board is a 2D list with NUM_ROWS rows and NUM_COLUMNS columns.
    Each cell is initialized with a space character to represent empty.
    """
    # Create a 2D list using list comprehension
    # Outer loop creates rows, inner loop creates columns within each row
    board = []
    for row in range(NUM_ROWS):
        # Create a new row with empty spaces for each column
        new_row = []
        for col in range(NUM_COLUMNS):
            new_row.append(" ")  # Space represents an empty cell
        board.append(new_row)
    return board


def clear_screen():
    """
    Clears the terminal screen for a cleaner display.
    Uses the 'clear' command which works on Unix/Linux/Mac systems.
    """
    os.system('clear')


def print_board(board):
    """
    Prints the current state of the board with column labels and grid lines.
    The format matches the required output with +---+ separators and | dividers.
    """
    # First, print the column labels (A through G) with proper spacing
    # Each column is 4 characters wide (3 for cell + 1 for divider)
    header = "   "  # Initial spacing to align with the grid
    for label in COLUMN_LABELS:
        header += label + "   "  # Each label followed by 3 spaces for alignment
    print(header)
    
    # Print the top border of the grid
    print_horizontal_line()
    
    # Print each row of the board
    for row in range(NUM_ROWS):
        # Start the row with a vertical bar
        row_string = "|"
        for col in range(NUM_COLUMNS):
            # Each cell is formatted as " X |" where X is the checker or space
            row_string += " " + board[row][col] + " |"
        print(row_string)
        
        # Print a horizontal line after each row
        print_horizontal_line()


def print_horizontal_line():
    """
    Prints a horizontal separator line for the board grid.
    Format: +---+---+---+---+---+---+---+
    """
    line = "+"
    for col in range(NUM_COLUMNS):
        line += "---+"  # Each cell separator is 3 dashes and a plus
    print(line)


def get_column_input(current_player):
    """
    Gets and validates the column input from the current player.
    Keeps asking until a valid column (A-G) that isn't full is entered.
    Returns the column index (0-6) corresponding to the chosen column.
    """
    while True:  # Loop until valid input is received
        # Prompt the player for input
        user_input = input(f"Player {current_player}, choose a column (A-G): ")
        
        # Check if input is exactly one character
        if len(user_input) != 1:
            print("Invalid input. Please enter a single letter A-G.")
            continue  # Ask again, don't end the turn
        
        # Convert to uppercase for consistent comparison
        column_letter = user_input.upper()
        
        # Check if the input is a letter
        if not column_letter.isalpha():
            print("Invalid input. Please enter a letter A-G.")
            continue  # Ask again, don't end the turn
        
        # Check if the letter is in the valid range (A-G)
        if column_letter not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter A-G.")
            continue  # Ask again, don't end the turn
        
        # Convert letter to column index (A=0, B=1, ..., G=6)
        column_index = COLUMN_LABELS.index(column_letter)
        
        # Return the valid column index
        return column_index


def is_column_full(board, column_index):
    """
    Checks if a column is full (no empty spaces in the top row).
    Returns True if the column is full, False otherwise.
    """
    # A column is full if the top row (index 0) is not empty
    return board[0][column_index] != " "


def drop_checker(board, column_index, checker):
    """
    Drops a checker into the specified column.
    The checker falls to the lowest available row (simulating gravity).
    Returns the row index where the checker was placed.
    """
    # Start from the bottom row and move up to find the first empty cell
    for row in range(NUM_ROWS - 1, -1, -1):  # Start at bottom (5), go to top (0)
        if board[row][column_index] == " ":  # Found an empty cell
            board[row][column_index] = checker  # Place the checker
            return row  # Return the row where checker was placed
    
    # This should never happen if we validate column isn't full before calling
    return -1


def check_win(board, row, col, checker):
    """
    Checks if the last move resulted in a win (4 in a row).
    Checks all four directions: horizontal, vertical, and both diagonals.
    Returns True if the current player has won, False otherwise.
    """
    # Check horizontal (left-right)
    if check_direction(board, row, col, checker, 0, 1):
        return True
    
    # Check vertical (up-down)
    if check_direction(board, row, col, checker, 1, 0):
        return True
    
    # Check diagonal (top-left to bottom-right)
    if check_direction(board, row, col, checker, 1, 1):
        return True
    
    # Check diagonal (top-right to bottom-left)
    if check_direction(board, row, col, checker, 1, -1):
        return True
    
    # No win found in any direction
    return False


def check_direction(board, row, col, checker, row_delta, col_delta):
    """
    Checks for 4 in a row in a specific direction.
    Counts consecutive checkers in both directions from the placed piece.
    row_delta and col_delta define the direction to check.
    Returns True if 4 or more consecutive checkers are found.
    """
    count = 1  # Start with 1 for the piece that was just placed
    
    # Check in the positive direction (row+delta, col+delta)
    count += count_consecutive(board, row, col, checker, row_delta, col_delta)
    
    # Check in the negative direction (row-delta, col-delta)
    count += count_consecutive(board, row, col, checker, -row_delta, -col_delta)
    
    # Win if 4 or more consecutive checkers
    return count >= 4


def count_consecutive(board, row, col, checker, row_delta, col_delta):
    """
    Counts consecutive checkers in one direction from a starting position.
    Does not count the starting position itself.
    Returns the count of consecutive matching checkers.
    """
    count = 0
    current_row = row + row_delta  # Start one step away from the placed piece
    current_col = col + col_delta
    
    # Keep counting while within bounds and matching checker found
    while True:
        # Check if position is within board boundaries
        if current_row < 0 or current_row >= NUM_ROWS:
            break  # Out of bounds vertically
        if current_col < 0 or current_col >= NUM_COLUMNS:
            break  # Out of bounds horizontally
        
        # Check if the cell contains the same checker
        if board[current_row][current_col] != checker:
            break  # Different checker or empty, stop counting
        
        # Found a matching checker, increment count and move to next cell
        count += 1
        current_row += row_delta
        current_col += col_delta
    
    return count


def is_board_full(board):
    """
    Checks if the entire board is full (no empty spaces).
    Returns True if the board is full (draw condition), False otherwise.
    """
    # Check the top row only - if any column has space in top row, board isn't full
    for col in range(NUM_COLUMNS):
        if board[0][col] == " ":  # Found an empty space in top row
            return False
    
    # All columns are full
    return True


def play_game():
    """
    Main game loop that controls the flow of the Connect 4 game.
    Handles player turns, input validation, win checking, and draw detection.
    """
    # Create a new empty board
    board = create_board()
    
    # Randomly select which player goes first (0 or 1)
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    
    # Clear screen and show the initial empty board
    clear_screen()
    print_board(board)
    
    # Main game loop - continues until someone wins or board is full
    while True:
        # Get the current player's checker symbol (X or O)
        current_checker = PLAYER_CHECKERS[current_player_index]
        
        # Get valid column input from the player
        # This loop handles invalid input without ending the turn
        while True:
            column_index = get_column_input(current_checker)
            
            # Check if the selected column is full
            if is_column_full(board, column_index):
                print("That column is full. Please choose another column.")
                continue  # Ask again, don't end the turn
            
            # Valid column selected, exit the input loop
            break
        
        # Drop the checker into the selected column
        row_placed = drop_checker(board, column_index, current_checker)
        
        # Clear screen and display the updated board
        clear_screen()
        print_board(board)
        
        # Check if this move resulted in a win
        if check_win(board, row_placed, column_index, current_checker):
            print(f"{current_checker} won!")
            break  # End the game
        
        # Check if the board is full (draw condition)
        if is_board_full(board):
            print("It's a draw!")
            break  # End the game
        
        # Switch to the other player for the next turn
        # Toggle between 0 and 1 using modulo
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


# Entry point of the program
# This ensures the game only runs when the script is executed directly
if __name__ == "__main__":
    play_game()