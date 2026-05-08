# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 468
# filename        : gen_0468_o4mini_11.py
# timestamp       : 2026-05-07T22:44:42Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 387
# tokens_output   : 1057
# tokens_total    : 1444
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

# Global constants for board dimensions and number of players
ROWS = 6
COLS = 7
NUM_PLAYERS = 2

# Global player tokens
PLAYER_TOKENS = ['X', 'O']

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear')

def create_board():
    """Creates and returns an empty Connect 4 board."""
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    clear_screen()
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_input(input_char):
    """Checks if the input character is a valid column label."""
    return input_char in 'ABCDEFG'

def is_column_full(board, col):
    """Checks if a column is full."""
    return board[0][col] != ' '

def get_column_index(column_label):
    """Converts a column label (A-G) to a zero-based column index."""
    return ord(column_label) - ord('A')

def get_player_input(board):
    """
    Prompts the player for a valid column input.
    Ensures the input is a valid column label and the column is not full.
    """
    while True:
        user_input = input("Choose a column (A-G): ").strip().upper()
        if not is_valid_input(user_input):
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = get_column_index(user_input)
        if is_column_full(board, col):
            print("Column is full. Choose a different column.")
            continue
        return col

def drop_checker(board, col, token):
    """
    Drops a checker into the specified column.
    The checker fills the lowest available row in the column.
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = token
            return row, col

def check_winner(board, row, col, token):
    """
    Checks if placing the token at (row, col) results in a win.
    A win is defined as 4 tokens in a row horizontally, vertically, or diagonally.
    """
    # Directions: (row_delta, col_delta)
    directions = [
        (0, 1),  # Horizontal
        (1, 0),  # Vertical
        (1, 1),  # Diagonal down-right
        (1, -1)  # Diagonal down-left
    ]

    for dr, dc in directions:
        count = 1  # Include the current token

        # Check in the positive direction
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == token:
            count += 1
            r += dr
            c += dc

        # Check in the negative direction
        r, c = row - dr, col - dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == token:
            count += 1
            r -= dr
            c -= dc

        if count >= 4:
            return True

    return False

def is_draw(board):
    """Checks if the board is full, resulting in a draw."""
    return all(board[0][col] != ' ' for col in range(COLS))

def main():
    """Main function to run the Connect 4 game."""
    # Initialize the board
    board = create_board()

    # Randomly select the starting player
    current_player = random.randint(0, NUM_PLAYERS - 1)

    # Game loop
    while True:
        print_board(board)
        print(f"Player {PLAYER_TOKENS[current_player]}'s turn.")
        
        # Get valid player input
        col = get_player_input(board)

        # Drop the checker and get its position
        row, col = drop_checker(board, col, PLAYER_TOKENS[current_player])

        # Check for a win
        if check_winner(board, row, col, PLAYER_TOKENS[current_player]):
            print_board(board)
            print(f"Player {PLAYER_TOKENS[current_player]} won!")
            break
        
        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch to the next player
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```