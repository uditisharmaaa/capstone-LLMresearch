# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 450
# filename        : gen_0450_opus46_08.py
# timestamp       : 2026-05-07T22:40:17Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 418
# tokens_output   : 1542
# tokens_total    : 1960
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
#   Write with a focus on code readability over brevity.
# ====================================================================



```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def create_board():
    board = []
    for row in range(NUM_ROWS):
        new_row = []
        for col in range(NUM_COLS):
            new_row.append(' ')
        board.append(new_row)
    return board


def print_board(board):
    os.system('clear')

    # Print column labels
    header = "  "
    for col_index in range(NUM_COLS):
        header += " " + COLUMN_LABELS[col_index] + "  "
    print(header)

    # Print each row with borders
    for row in range(NUM_ROWS):
        # Print the separator line
        separator = "+"
        for col in range(NUM_COLS):
            separator += "---+"
        print(separator)

        # Print the row contents
        row_string = "|"
        for col in range(NUM_COLS):
            row_string += " " + board[row][col] + " |"
        print(row_string)

    # Print the bottom separator line
    bottom_separator = "+"
    for col in range(NUM_COLS):
        bottom_separator += "---+"
    print(bottom_separator)


def get_column_choice(board, current_player):
    while True:
        user_input = input("Player " + current_player + ", choose a column (A-G): ")

        # Check if input is exactly one character and is a letter
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter from A to G.")
            continue

        # Convert to uppercase for consistency
        user_input = user_input.upper()

        # Check if the letter is within the valid range
        if user_input not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter from A to G.")
            continue

        # Convert letter to column index
        col_index = COLUMN_LABELS.index(user_input)

        # Check if the column is full
        if board[0][col_index] != ' ':
            print("Column " + user_input + " is full. Please choose a different column.")
            continue

        return col_index


def drop_checker(board, col_index, checker):
    # Start from the bottom row and find the lowest available spot
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col_index] == ' ':
            board[row][col_index] = checker
            return row
    return -1


def check_horizontal_win(board, checker):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker and
                board[row][col + 1] == checker and
                board[row][col + 2] == checker and
                board[row][col + 3] == checker):
                return True
    return False


def check_vertical_win(board, checker):
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if (board[row][col] == checker and
                board[row + 1][col] == checker and
                board[row + 2][col] == checker and
                board[row + 3][col] == checker):
                return True
    return False


def check_diagonal_win(board, checker):
    # Check diagonal going down-right
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker and
                board[row + 1][col + 1] == checker and
                board[row + 2][col + 2] == checker and
                board[row + 3][col + 3] == checker):
                return True

    # Check diagonal going down-left
    for row in range(NUM_ROWS - 3):
        for col in range(3, NUM_COLS):
            if (board[row][col] == checker and
                board[row + 1][col - 1] == checker and
                board[row + 2][col - 2] == checker and
                board[row + 3][col - 3] == checker):
                return True

    return False


def check_win(board, checker):
    if check_horizontal_win(board, checker):
        return True
    if check_vertical_win(board, checker):
        return True
    if check_diagonal_win(board, checker):
        return True
    return False


def is_board_full(board):
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            return False
    return True


def main():
    board = create_board()

    # Define the two players
    players = ['X', 'O']

    # Randomly select which player goes first
    current_player_index = random.randint(0, NUM_PLAYERS - 1)

    # Print the initial empty board
    print_board(board)

    game_over = False

    while not game_over:
        current_checker = players[current_player_index]

        # Get a valid column choice from the current player
        col_index = get_column_choice(board, current_checker)

        # Drop the checker into the chosen column
        drop_checker(board, col_index, current_checker)

        # Print the updated board
        print_board(board)

        # Check if the current player has won
        if check_win(board, current_checker):
            print(current_checker + " won!")
            game_over = True
        # Check if the board is full (draw)
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch to the other player
            current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()
```