# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 244
# filename        : gen_0244_llama_09.py
# timestamp       : 2026-04-06T09:40:56Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 394
# tokens_output   : 777
# tokens_total    : 1171
# cost_usd        : 0.000788
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
#   Write using only basic Python features a first-year student would know.
# ====================================================================

```python
import os
import random

# Constant global variables
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Function to print the board
def print_board():
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(' {} |'.format(cell), end='')
        print()
        print('+---+---+---+---+---+---+---+')

# Function to check for a win
def check_win(player):
    # Check horizontal locations for win
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(BOARD_COLS):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(BOARD_ROWS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_COLS - 3):
        for r in range(3, BOARD_ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

# Main game loop
def play_game():
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board()
        print("Player", current_player, "turn. Choose a column (A-G):")
        while True:
            move = input().upper()
            if move not in 'ABCDEFG':
                print("Invalid input. Please enter a letter between A and G.")
            elif board[0][ord(move) - ord('A')]!= ' ':
                print("Column is full. Please choose another column.")
            else:
                break

        # Drop the checker to the lowest available row in the chosen column
        for row in range(BOARD_ROWS - 1, -1, -1):
            if board[row][ord(move) - ord('A')] == ' ':
                board[row][ord(move) - ord('A')] = current_player
                break

        # Check for a win
        if check_win(current_player):
            print_board()
            print("Player", current_player, "won!")
            break

        # Check for a draw
        if all(cell!= ' ' for row in board for cell in row):
            print_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

play_game()
```