# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 449
# filename        : gen_0449_sonnet46_07.py
# timestamp       : 2026-05-07T22:39:58Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 420
# tokens_output   : 2135
# tokens_total    : 2555
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

# Global constants for board dimensions and number of players
NUM_COLS = 7
NUM_ROWS = 6
NUM_PLAYERS = 2

# The column labels we will use for the board
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# The checkers each player will use
PLAYER_CHECKERS = ['X', 'O']


def create_board():
    # Create a 2D list (list of lists) with NUM_ROWS rows and NUM_COLS columns
    # Each cell starts as a space character, meaning it is empty
    # We use a nested list comprehension to build this structure
    board = [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    return board


def print_board(board):
    # First, clear the screen so the board always appears at the top
    os.system('clear')

    # Print the column labels (A through G) with spacing to align with the board
    # Each cell is 4 characters wide (| + space + letter + space), so we pad accordingly
    print('   ' + '   '.join(COLUMN_LABELS))

    # Now print each row of the board with the grid lines
    for row in range(NUM_ROWS):
        # Print the horizontal divider line between rows
        print('+---' * NUM_COLS + '+')

        # Print the actual row contents with vertical dividers
        # We build the row string by joining each cell value with '|' separators
        row_string = '|'
        for col in range(NUM_COLS):
            row_string += ' ' + board[row][col] + ' |'
        print(row_string)

    # Print the final bottom divider line
    print('+---' * NUM_COLS + '+')


def get_player_input(board, player_checker):
    # Keep asking the player for input until they give us a valid move
    # This loop will only exit when we successfully return a valid column index
    while True:
        # Ask the player to enter a column letter
        user_input = input(f'Player {player_checker}, choose a column (A-G): ')

        # First, check if the input is actually a single letter
        # We use isalpha() to check if the string contains only letters
        if not user_input.isalpha():
            print('Invalid input! Please enter a letter between A and G.')
            # Continue means go back to the top of the while loop and ask again
            continue

        # Convert the input to uppercase so 'a' and 'A' both work
        user_input = user_input.upper()

        # Check if the letter is one of our valid column labels
        if user_input not in COLUMN_LABELS:
            print('Invalid column! Please choose a letter between A and G.')
            continue

        # Convert the letter to a column index (A=0, B=1, C=2, etc.)
        col_index = COLUMN_LABELS.index(user_input)

        # Check if the chosen column is already full
        # A column is full if the top row (row 0) is not empty
        if board[0][col_index] != ' ':
            print('That column is full! Please choose a different column.')
            continue

        # If we made it here, the input is valid! Return the column index.
        return col_index


def drop_checker(board, col_index, player_checker):
    # We want to drop the checker to the lowest available row in the column
    # So we start from the bottom row (NUM_ROWS - 1) and work our way up
    for row in range(NUM_ROWS - 1, -1, -1):
        # Check if this cell is empty (contains a space)
        if board[row][col_index] == ' ':
            # Place the checker here and stop looking
            board[row][col_index] = player_checker
            # Return the row where we placed the checker (useful for win checking)
            return row

    # This should never happen because we already validated the column is not full
    # But it's good practice to handle this case anyway
    return -1


def check_win(board, row, col, player_checker):
    # After each move, we check if the current player has won
    # We only need to check lines that pass through the most recently placed checker
    # There are four directions to check: horizontal, vertical, and two diagonals

    # Helper function to count consecutive checkers in a given direction
    # direction_row and direction_col tell us which way to move (+1, -1, or 0)
    def count_in_direction(direction_row, direction_col):
        count = 0
        # Check up to 3 cells in the given direction
        current_row = row + direction_row
        current_col = col + direction_col

        while 0 <= current_row < NUM_ROWS and 0 <= current_col < NUM_COLS:
            if board[current_row][current_col] == player_checker:
                count += 1
                current_row += direction_row
                current_col += direction_col
            else:
                # Stop counting as soon as we hit a different checker or empty cell
                break
        return count

    # Define the four directions we need to check
    # Each direction is a pair of (row_change, col_change)
    # We check both ways along each axis and add the counts together
    directions = [
        (0, 1),   # Horizontal: left and right
        (1, 0),   # Vertical: up and down
        (1, 1),   # Diagonal: top-left to bottom-right
        (1, -1),  # Diagonal: top-right to bottom-left
    ]

    for direction_row, direction_col in directions:
        # Count checkers in both the positive and negative direction along this axis
        # Add 1 for the checker we just placed
        total = 1
        total += count_in_direction(direction_row, direction_col)
        total += count_in_direction(-direction_row, -direction_col)

        # If we found 4 or more in a row, the current player wins!
        if total >= 4:
            return True

    # If none of the directions gave us 4 in a row, no win yet
    return False


def check_draw(board):
    # The game is a draw if every cell in the board is filled (no spaces left)
    # We check the top row since it fills last - if it's full, the board is full
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            # Found an empty cell, so the board is not full yet
            return False
    # All cells in the top row are filled, so the board must be completely full
    return True


def play_game():
    # Create a fresh board to start the game
    board = create_board()

    # Randomly decide which player goes first
    # random.randint(0, 1) gives us either 0 or 1, which maps to our two players
    current_player_index = random.randint(0, NUM_PLAYERS - 1)

    # Print the initial empty board before any moves are made
    print_board(board)
    print(f'Player {PLAYER_CHECKERS[current_player_index]} goes first!')

    # The main game loop - keep playing until someone wins or the board is full
    while True:
        # Get the current player's checker symbol
        current_checker = PLAYER_CHECKERS[current_player_index]

        # Ask the player for their move and validate it
        col_index = get_player_input(board, current_checker)

        # Drop the checker into the chosen column and record where it landed
        row_index = drop_checker(board, col_index, current_checker)

        # Print the updated board after the move
        print_board(board)

        # Check if this move resulted in a win
        if check_win(board, row_index, col_index, current_checker):
            print(f'Player {current_checker} won!')
            # End the game by breaking out of the while loop
            break

        # Check if the board is completely full (a draw)
        if check_draw(board):
            print("It's a draw! The board is full.")
            break

        # Switch to the other player for the next turn
        # Using modulo (%) means we cycle back to 0 after reaching NUM_PLAYERS
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


# This is the standard Python way to run code only when the script is executed directly
# It prevents the game from running if this file is imported as a module
if __name__ == '__main__':
    play_game()