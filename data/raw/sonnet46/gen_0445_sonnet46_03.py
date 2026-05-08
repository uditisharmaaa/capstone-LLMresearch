# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 445
# filename        : gen_0445_sonnet46_03.py
# timestamp       : 2026-05-07T22:37:23Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 2236
# tokens_total    : 2651
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

import os
import random

# Global constants for board dimensions and number of players
NUM_COLS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2

# Column labels for display and input validation
COL_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# The two player checkers
CHECKERS = ['X', 'O']


def create_board():
    """
    Create and return a fresh 2D board initialized with spaces.
    The board is a list of rows, each row is a list of cells.
    board[0] is the top row, board[NUM_ROWS-1] is the bottom row.
    """
    # Use a list comprehension to build NUM_ROWS rows, each with NUM_COLS spaces
    board = [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    return board


def print_board(board):
    """
    Clear the screen and print the current state of the board.
    Format includes column labels A-G and dividing lines between rows.
    """
    # Clear the terminal screen before printing so the board refreshes in place
    os.system('clear')

    # Print the column header labels, spaced to align with board columns
    # Each column cell is 4 characters wide (| + space + checker + space),
    # so we center each label in a 4-char field, then strip the trailing space
    header = '   ' + '   '.join(COL_LABELS)
    print(header)

    # Build the horizontal divider line that separates rows
    # It looks like: +---+---+---+---+---+---+---+
    divider = '+' + '+'.join(['---'] * NUM_COLS) + '+'

    # Print each row with dividers above and below
    for row in board:
        # Print the top divider for this row
        print(divider)

        # Build the row string: each cell is | followed by space+checker+space
        row_str = '|' + '|'.join([' ' + cell + ' ' for cell in row]) + '|'
        print(row_str)

    # Print the final bottom divider after the last row
    print(divider)


def get_player_input(board, player_checker):
    """
    Prompt the current player to choose a column (A-G).
    Validates input continuously until a valid, non-full column is chosen.
    Returns the integer column index (0-6) of the chosen column.
    """
    while True:
        # Ask the player for their move
        raw = input(f"Player {player_checker}, choose a column (A-G): ")

        # Check that the input is exactly one character and is a letter
        if len(raw) != 1 or not raw.isalpha():
            # Invalid input: not a single letter, ask again
            print("Invalid input. Please enter a single letter from A to G.")
            continue

        # Convert to uppercase to handle lowercase input gracefully
        col_letter = raw.upper()

        # Check that the letter is one of the valid column labels
        if col_letter not in COL_LABELS:
            # Letter is outside A-G range, ask again
            print(f"'{col_letter}' is not a valid column. Choose from A to G.")
            continue

        # Convert the letter to a column index (A=0, B=1, ..., G=6)
        col_index = COL_LABELS.index(col_letter)

        # Check that the chosen column is not already full
        # The top cell of a column is at row index 0; if it's not a space, the column is full
        if board[0][col_index] != ' ':
            print(f"Column {col_letter} is full. Please choose another column.")
            continue

        # All checks passed; return the valid column index
        return col_index


def drop_checker(board, col_index, checker):
    """
    Drop the given checker into the specified column.
    The checker falls to the lowest available (bottom-most empty) row.
    Modifies the board in place.
    """
    # Iterate from the bottom row upward to find the lowest empty cell
    for row_index in range(NUM_ROWS - 1, -1, -1):
        if board[row_index][col_index] == ' ':
            # Found the lowest empty cell; place the checker here
            board[row_index][col_index] = checker
            # Return the row index where the checker landed (used for win checking)
            return row_index

    # This point should never be reached if input validation is correct
    return -1


def check_win(board, row, col, checker):
    """
    Check whether the last move at (row, col) resulted in a win for checker.
    Checks all four directions: horizontal, vertical, and both diagonals.
    Returns True if the player has won, False otherwise.
    """

    def count_in_direction(delta_row, delta_col):
        """
        Count consecutive checkers in one direction from (row, col).
        delta_row and delta_col define the direction to look.
        Returns the count of consecutive matching checkers (not counting the origin).
        """
        count = 0
        # Step outward in the given direction, up to 3 additional cells
        r, c = row + delta_row, col + delta_col
        while 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS and board[r][c] == checker:
            count += 1
            r += delta_row
            c += delta_col
        return count

    # Define the four axis directions to check:
    # Each tuple is (direction1, direction2) as (delta_row, delta_col) pairs
    directions = [
        # Horizontal: left and right
        ((0, -1), (0, 1)),
        # Vertical: up and down
        ((-1, 0), (1, 0)),
        # Diagonal top-left to bottom-right
        ((-1, -1), (1, 1)),
        # Diagonal top-right to bottom-left
        ((-1, 1), (1, -1)),
    ]

    for dir1, dir2 in directions:
        # Count consecutive matching checkers in both directions along this axis
        # Add 1 to include the checker just placed at (row, col)
        total = 1 + count_in_direction(*dir1) + count_in_direction(*dir2)

        # If 4 or more in a line, it's a win
        if total >= 4:
            return True

    # No winning line found
    return False


def check_draw(board):
    """
    Check whether the board is completely full (a draw condition).
    Returns True if every cell is occupied, False otherwise.
    """
    # If any cell in the top row is empty, the board is not yet full
    # (checkers fill from the bottom, so the top row is last to fill)
    for col_index in range(NUM_COLS):
        if board[0][col_index] == ' ':
            return False
    # All top-row cells are filled, meaning the entire board is full
    return True


def play_game():
    """
    Main game loop. Sets up the board, randomly selects who goes first,
    and alternates turns until someone wins or the board is full (draw).
    """
    # Create the initial empty board
    board = create_board()

    # Randomly decide which player goes first (0 or 1 index into CHECKERS)
    current_player_index = random.randint(0, NUM_PLAYERS - 1)

    # Print the initial empty board before any moves are made
    print_board(board)
    print(f"Player {CHECKERS[current_player_index]} goes first!")

    # Main game loop: continue until a win or draw is detected
    while True:
        # Get the current player's checker symbol
        current_checker = CHECKERS[current_player_index]

        # Prompt the current player for a valid column choice
        col_index = get_player_input(board, current_checker)

        # Drop the checker into the chosen column and record where it landed
        row_index = drop_checker(board, col_index, current_checker)

        # Refresh the board display after the move
        print_board(board)

        # Check if the current move resulted in a win
        if check_win(board, row_index, col_index, current_checker):
            # Announce the winner and end the game
            print(f"Player {current_checker} won!")
            break

        # Check if the board is completely full (draw condition)
        if check_draw(board):
            # Announce the draw and end the game
            print("It's a draw!")
            break

        # Switch to the other player for the next turn
        # Toggle between index 0 and 1 using modulo arithmetic
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


# Entry point: run the game when this script is executed directly
if __name__ == '__main__':
    play_game()