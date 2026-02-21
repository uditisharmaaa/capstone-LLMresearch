# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 63
# filename        : gen_0063_gpt4o_03.py
# timestamp       : 2026-02-19T20:52:12Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 1045
# tokens_total    : 1432
# cost_usd        : 0.011417
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

# Constants for board dimensions and number of players
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

# Player symbols
PLAYER_SYMBOLS = ['X', 'O']

def clear_screen():
    """Clear the console screen."""
    os.system('clear')

def create_board():
    """Create a 2D board initialized with spaces."""
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Print the board with column labels."""
    clear_screen()
    # Print column labels
    print("   A   B   C   D   E   F   G")
    print("+---" * NUM_COLS + "+")
    # Print each row of the board
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * NUM_COLS + "+")

def is_valid_move(board, col):
    """Check if the move is valid for the given column."""
    # Column must be within bounds and not full
    return 0 <= col < NUM_COLS and board[0][col] == ' '

def get_next_open_row(board, col):
    """Return the next open row in the specified column."""
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            return r
    return None

def drop_checker(board, row, col, checker):
    """Place the checker in the specified location."""
    board[row][col] = checker

def check_for_win(board, checker):
    """Check all win conditions for the current checker."""
    # Check horizontal locations for win
    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS):
            if board[r][c] == checker and board[r][c+1] == checker and board[r][c+2] == checker and board[r][c+3] == checker:
                return True
    
    # Check vertical locations for win
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == checker and board[r+1][c] == checker and board[r+2][c] == checker and board[r+3][c] == checker:
                return True
    
    # Check positively sloped diagonals
    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == checker and board[r+1][c+1] == checker and board[r+2][c+2] == checker and board[r+3][c+3] == checker:
                return True

    # Check negatively sloped diagonals
    for c in range(NUM_COLS - 3):
        for r in range(3, NUM_ROWS):
            if board[r][c] == checker and board[r-1][c+1] == checker and board[r-2][c+2] == checker and board[r-3][c+3] == checker:
                return True

    return False

def is_draw(board):
    """Check if the board is completely filled."""
    for c in range(NUM_COLS):
        if board[0][c] == ' ':
            return False
    return True

def get_player_input():
    """Get player input and validate it."""
    while True:
        try:
            col_input = input("Choose a column (A-G): ").strip().upper()
            if col_input not in "ABCDEFG" or len(col_input) != 1:
                raise ValueError("Invalid input")
            return ord(col_input) - ord('A')
        except ValueError as e:
            print(e)

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    game_over = False

    # Randomly select which player starts
    turn = random.randint(0, NUM_PLAYERS - 1)

    while not game_over:
        print_board(board)
        print(f"Player {PLAYER_SYMBOLS[turn]}'s turn.")

        # Get valid player input
        col = get_player_input()

        if is_valid_move(board, col):
            row = get_next_open_row(board, col)
            drop_checker(board, row, col, PLAYER_SYMBOLS[turn])
            
            # Check for win condition
            if check_for_win(board, PLAYER_SYMBOLS[turn]):
                print_board(board)
                print(f"Player {PLAYER_SYMBOLS[turn]} won!")
                game_over = True
            # Check for draw condition
            elif is_draw(board):
                print_board(board)
                print("The game is a draw!")
                game_over = True
            else:
                # Switch to the other player
                turn = (turn + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```