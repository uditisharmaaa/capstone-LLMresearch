# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 149
# filename        : gen_0149_llama_04.py
# timestamp       : 2026-04-06T10:05:35Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 394
# tokens_output   : 748
# tokens_total    : 1142
# cost_usd        : 0.000766
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

# Constants
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to print the board
def print_board():
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} |'.format(' | '.join(row)))
        print('+---+---+---+---+---+---+---+')

# Function to check for a win
def check_win(player):
    # Check horizontal locations for win
    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS):
            if board[r][c] == player and board[r][c + 1] == player and board[r][c + 2] == player and board[r][c + 3] == player:
                return True

    # Check vertical locations for win
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == player and board[r + 1][c] == player and board[r + 2][c] == player and board[r + 3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(NUM_COLS - 3):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == player and board[r + 1][c + 1] == player and board[r + 2][c + 2] == player and board[r + 3][c + 3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(NUM_COLS - 3):
        for r in range(3, NUM_ROWS):
            if board[r][c] == player and board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and board[r - 3][c + 3] == player:
                return True

# Function to handle player move
def player_move(player):
    while True:
        col = input("Player {}, choose a column (A-G): ".format(player)).strip().upper()
        if not col.isalpha() or not 'A' <= col <= 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = ord(col) - ord('A')
        for row in range(NUM_ROWS - 1, -1, -1):
            if board[row][col] == ' ':
                board[row][col] = player
                return

# Main game loop
def game():
    players = ['X', 'O']
    current_player = random.choice(players)
    while True:
        clear_screen()
        print_board()
        player_move(current_player)
        if check_win(current_player):
            clear_screen()
            print_board()
            print("Player {} won!".format(current_player))
            break
        current_player = 'O' if current_player == 'X' else 'X'
        if all(all(cell!= ' ' for cell in row) for row in board):
            clear_screen()
            print_board()
            print("It's a draw!")
            break

game()
```