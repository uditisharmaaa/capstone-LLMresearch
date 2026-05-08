# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 183
# filename        : gen_0183_llama_08.py
# timestamp       : 2026-04-06T09:23:47Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 393
# tokens_output   : 806
# tokens_total    : 1199
# cost_usd        : 0.000809
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

# Constant global variables
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Function to print the board
def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} |'.format(' | '.join(row)))
        print('+---+---+---+---+---+---+---+')

# Function to validate player input
def get_player_move(player):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player)).strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

# Function to drop the checker to the lowest available row
def drop_checker(column, player):
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = 'X' if player == 1 else 'O'
            break

# Function to check for a win
def check_win(player):
    symbol = 'X' if player == 1 else 'O'
    # Check horizontal locations for win
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == symbol and board[row][col + 1] == symbol and board[row][col + 2] == symbol and board[row][col + 3] == symbol:
                return True
    # Check vertical locations for win
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if board[row][col] == symbol and board[row + 1][col] == symbol and board[row + 2][col] == symbol and board[row + 3][col] == symbol:
                return True
    # Check positively sloped diagonals
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == symbol and board[row + 1][col + 1] == symbol and board[row + 2][col + 2] == symbol and board[row + 3][col + 3] == symbol:
                return True
    # Check negatively sloped diagonals
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == symbol and board[row - 1][col + 1] == symbol and board[row - 2][col + 2] == symbol and board[row - 3][col + 3] == symbol:
                return True
    return False

# Main game loop
current_player = random.randint(1, NUM_PLAYERS)
print_board()
while True:
    move = get_player_move(current_player)
    drop_checker(move, current_player)
    print_board()
    if check_win(current_player):
        print("Player {} won!".format(current_player))
        break
    # Check for draw
    if all(board[0][col]!= ' ' for col in range(BOARD_WIDTH)):
        print("It's a draw!")
        break
    current_player = 2 if current_player == 1 else 1
```