# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 401
# filename        : gen_0401_o4mini_11.py
# timestamp       : 2026-05-07T19:11:45Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 860
# tokens_total    : 1247
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
#   Write with extensive docstrings for every function.
# ====================================================================

```python
import os
import random

# Global constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def create_board():
    """Creates and returns a blank Connect 4 board."""
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the current state of the board with column labels."""
    clear_screen()
    print('   ' + '   '.join(COLUMN_LABELS))
    print('+---' * COLUMNS + '+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * COLUMNS + '+')

def is_valid_column(board, column):
    """Checks if the chosen column is valid for a move."""
    if column not in COLUMN_LABELS:
        return False
    col_index = COLUMN_LABELS.index(column)
    return board[0][col_index] == ' '

def get_column_choice(board, player):
    """Prompts the player to choose a valid column."""
    while True:
        choice = input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a column (A-G): ").strip().upper()
        if is_valid_column(board, choice):
            return COLUMN_LABELS.index(choice)
        print("Invalid choice. Try again.")

def drop_checker(board, column, player):
    """Drops the player's checker into the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = 'X' if player == 1 else 'O'
            break

def check_winner(board, player):
    """Checks if the current player has won the game."""
    checker = 'X' if player == 1 else 'O'

    # Check horizontally
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertically
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (negative slope)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row - i][col + i] == checker for i in range(4)):
                return True

    return False

def is_draw(board):
    """Checks if the game is a draw (board is full)."""
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    print_board(board)

    # Randomly select the starting player
    current_player = random.randint(1, PLAYERS)

    while True:
        print_board(board)
        column = get_column_choice(board, current_player)
        drop_checker(board, column, current_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} ({'X' if current_player == 1 else 'O'}) won!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 1 if current_player == 2 else 2

if __name__ == "__main__":
    main()
```