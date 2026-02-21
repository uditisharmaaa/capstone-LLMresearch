# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 78
# filename        : gen_0078_gpt4o_03.py
# timestamp       : 2026-02-19T21:00:51Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 830
# tokens_total    : 1217
# cost_usd        : 0.009267
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
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

# Define player symbols
PLAYER_X = 'X'
PLAYER_O = 'O'
PLAYERS = [PLAYER_X, PLAYER_O]

def clear_screen():
    """Clears the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def create_board():
    """Creates a 2D board with spaces initialized for Connect 4."""
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    """Prints the current state of the board with column labels."""
    clear_screen()
    columns = '   ' + '   '.join(chr(i) for i in range(ord('A'), ord('A') + NUM_COLS))
    separator = '+---' * NUM_COLS + '+'
    print(columns)
    print(separator)
    for row in board:
        print('|' + '|'.join(f" {cell} " for cell in row) + '|')
        print(separator)

def get_player_input(board, player):
    """Gets a valid column input from the player."""
    while True:
        choice = input(f"Player {player} choose a column (A-G): ").upper()
        if choice in [chr(i) for i in range(ord('A'), ord('A') + NUM_COLS)]:
            col = ord(choice) - ord('A')
            if board[0][col] == ' ':
                return col
            else:
                print("Column is full, choose another one.")
        else:
            print("Invalid input. Please choose a letter between A and G.")

def drop_checker(board, col, player):
    """Drops the player's checker in the specified column."""
    for row in reversed(range(NUM_ROWS)):
        if board[row][col] == ' ':
            board[row][col] = player
            return row

def check_winner(board, player):
    """Checks if the current player has won the game."""
    # Check horizontal
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    # Check vertical
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    # Check diagonal \
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    # Check diagonal /
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False

def check_draw(board):
    """Checks if the board is full, resulting in a draw."""
    return all(board[0][col] != ' ' for col in range(NUM_COLS))

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.choice(PLAYERS)
    print_board(board)
    
    while True:
        col = get_player_input(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} won!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    main()
```