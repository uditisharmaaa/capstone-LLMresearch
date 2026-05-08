# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 430
# filename        : gen_0430_opus46_03.py
# timestamp       : 2026-05-07T22:32:56Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 415
# tokens_output   : 2114
# tokens_total    : 2529
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

# Global constants for board dimensions and number of players
NUM_ROWS = 6        # Number of rows in the Connect 4 board
NUM_COLS = 7        # Number of columns in the Connect 4 board
NUM_PLAYERS = 2     # Number of players in the game

# Column labels corresponding to each column index
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# The two player checkers
CHECKERS = ['X', 'O']


def create_board():
    """Create and return a 2D board initialized with spaces."""
    # Each cell is a space character indicating it is empty
    board = []
    for row in range(NUM_ROWS):
        # Create a row of NUM_COLS spaces
        new_row = [' '] * NUM_COLS
        board.append(new_row)
    return board


def print_board(board):
    """Clear the screen and print the board with column labels and grid formatting."""
    # Clear the terminal screen before printing
    os.system('clear')

    # Print the column labels with proper spacing
    # Each column label is centered in a 4-character wide space, except the first which has leading spaces
    header = "  "
    for i in range(NUM_COLS):
        header += " " + COLUMN_LABELS[i] + "  "
    print(header)

    # Print the separator line between rows
    separator = "+" + "---+" * NUM_COLS

    # Print each row of the board
    for row in range(NUM_ROWS):
        # Print the top border of this row
        print(separator)
        # Print the cells in this row, each surrounded by | and spaces
        row_str = "|"
        for col in range(NUM_COLS):
            # Each cell is formatted as " X " where X is the checker or space
            row_str += " " + board[row][col] + " |"
        print(row_str)

    # Print the bottom border of the last row
    print(separator)


def drop_checker(board, col, checker):
    """
    Drop a checker into the specified column.
    The checker falls to the lowest available row (highest index).
    Returns the row where the checker was placed, or -1 if the column is full.
    """
    # Start from the bottom row (highest index) and move upward
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            # Found an empty cell, place the checker here
            board[row][col] = checker
            return row
    # If we get here, the column is full
    return -1


def is_column_full(board, col):
    """Check if a column is full (top cell is not empty)."""
    # If the top row of the column is not a space, the column is full
    return board[0][col] != ' '


def check_win(board, checker):
    """
    Check if the given checker has won the game.
    A win is 4 in a row horizontally, vertically, or diagonally.
    Returns True if the checker has won, False otherwise.
    """
    # Check horizontal wins
    # For each row, check all possible horizontal sequences of 4
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):  # Only need to check starting positions where 4 fit
            if (board[row][col] == checker and
                board[row][col + 1] == checker and
                board[row][col + 2] == checker and
                board[row][col + 3] == checker):
                return True

    # Check vertical wins
    # For each column, check all possible vertical sequences of 4
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):  # Only need to check starting positions where 4 fit
            if (board[row][col] == checker and
                board[row + 1][col] == checker and
                board[row + 2][col] == checker and
                board[row + 3][col] == checker):
                return True

    # Check diagonal wins (top-left to bottom-right, i.e., descending diagonal)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker and
                board[row + 1][col + 1] == checker and
                board[row + 2][col + 2] == checker and
                board[row + 3][col + 3] == checker):
                return True

    # Check diagonal wins (bottom-left to top-right, i.e., ascending diagonal)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker and
                board[row - 1][col + 1] == checker and
                board[row - 2][col + 2] == checker and
                board[row - 3][col + 3] == checker):
                return True

    # No win found
    return False


def is_board_full(board):
    """Check if the entire board is full (no empty spaces in the top row)."""
    # If any cell in the top row is empty, the board is not full
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            return False
    return True


def get_player_input(board, player_checker):
    """
    Prompt the current player for a column choice.
    Validates the input:
    - Must be a single letter A-G (uppercase)
    - The chosen column must not be full
    Keeps asking until valid input is received.
    Returns the column index (0-6).
    """
    while True:
        # Prompt the player for their move
        user_input = input("Player " + player_checker + ", choose a column (A-G): ")

        # Check if the input is a single alphabetic character
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue

        # Convert to uppercase for consistency (though we expect uppercase input)
        user_input = user_input.upper()

        # Check if the letter is within the valid range A-G
        if user_input not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter from A to G.")
            continue

        # Convert the letter to a column index (A=0, B=1, ..., G=6)
        col = ord(user_input) - ord('A')

        # Check if the chosen column is full
        if is_column_full(board, col):
            print("Column " + user_input + " is full. Please choose another column.")
            continue

        # Input is valid, return the column index
        return col


def main():
    """Main function to run the Connect 4 game."""
    # Create a new empty board
    board = create_board()

    # Randomly select which player goes first (0 or 1)
    # This index corresponds to the CHECKERS list
    current_player = random.randint(0, NUM_PLAYERS - 1)

    # Print the initial empty board
    print_board(board)
    print("Player " + CHECKERS[current_player] + " goes first!")

    # Main game loop - continues until someone wins or the board is full
    while True:
        # Get the current player's checker symbol
        checker = CHECKERS[current_player]

        # Get valid column input from the current player
        col = get_player_input(board, checker)

        # Drop the checker into the chosen column
        drop_checker(board, col, checker)

        # Print the updated board
        print_board(board)

        # Check if the current player has won
        if check_win(board, checker):
            # Announce the winner and end the game
            print("Player " + checker + " won!")
            break

        # Check if the board is completely full (draw condition)
        if is_board_full(board):
            # Announce a draw and end the game
            print("It's a draw! The board is full with no winner.")
            break

        # Switch to the next player
        # Using modulo to cycle between 0 and 1
        current_player = (current_player + 1) % NUM_PLAYERS


# Run the game when the script is executed directly
if __name__ == "__main__":
    main()
```