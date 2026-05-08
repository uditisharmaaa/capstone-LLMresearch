# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 179
# filename        : gen_0179_llama_04.py
# timestamp       : 2026-04-06T10:12:06Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 394
# tokens_output   : 767
# tokens_total    : 1161
# cost_usd        : 0.000780
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

```python
import os
import random

# Constant global variables
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2
CHECKERS = ['X', 'O']

def create_board():
    """Create a 2D board with spaces"""
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    """Print the board with column labels A through G"""
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

def get_player_move(player):
    """Get a valid column move from the player"""
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, col, checker):
    """Drop the checker to the lowest available row in the chosen column"""
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = checker
            return

def check_win(board, checker):
    """Check for a win: 4 in a row horizontally, vertically, or diagonally"""
    # Check horizontal wins
    for row in board:
        for col in range(BOARD_COLS - 3):
            if all([cell == checker for cell in row[col:col+4]]):
                return True

    # Check vertical wins
    for col in range(BOARD_COLS):
        for row in range(BOARD_ROWS - 3):
            if all([board[row+i][col] == checker for i in range(4)]):
                return True

    # Check diagonal wins (top-left to bottom-right)
    for row in range(BOARD_ROWS - 3):
        for col in range(BOARD_COLS - 3):
            if all([board[row+i][col+i] == checker for i in range(4)]):
                return True

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_ROWS):
        for col in range(BOARD_COLS - 3):
            if all([board[row-i][col+i] == checker for i in range(4)]):
                return True

    return False

def main():
    global board
    board = create_board()
    players = list(range(NUM_PLAYERS))
    random.shuffle(players)
    current_player = 0

    while True:
        print_board(board)
        col = get_player_move(CHECKERS[players[current_player]])
        drop_checker(board, col, CHECKERS[players[current_player]])
        if check_win(board, CHECKERS[players[current_player]]):
            print_board(board)
            print(f"Player {CHECKERS[players[current_player]]} won!")
            break
        if all([all([cell!= ' ' for cell in row]) for row in board]):
            print_board(board)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```