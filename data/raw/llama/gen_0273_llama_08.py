# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 273
# filename        : gen_0273_llama_08.py
# timestamp       : 2026-04-06T09:48:39Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 393
# tokens_output   : 661
# tokens_total    : 1054
# cost_usd        : 0.000700
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

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_CHECKERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} |'.format(' | '.join(row)))
        print('+---+---+---+---+---+---+---+')

def get_player_move(player_checker):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player_checker)).strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter from A to G.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, column, checker):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = checker
            return

def check_win(board, checker):
    # Check horizontal
    for row in board:
        for i in range(BOARD_WIDTH - 3):
            if all([cell == checker for cell in row[i:i+4]]):
                return True

    # Check vertical
    for col in range(BOARD_WIDTH):
        for i in range(BOARD_HEIGHT - 3):
            if all([board[row][col] == checker for row in range(i, i+4)]):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if all([board[row+i][col+i] == checker for i in range(4)]):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if all([board[row-i][col+i] == checker for i in range(4)]):
                return True

    return False

def check_draw(board):
    return all([cell!= ' ' for row in board for cell in row])

board = create_board()
current_player = random.randint(0, NUM_PLAYERS - 1)

while True:
    print_board(board)
    column = get_player_move(PLAYER_CHECKERS[current_player])
    drop_checker(board, column, PLAYER_CHECKERS[current_player])
    if check_win(board, PLAYER_CHECKERS[current_player]):
        print_board(board)
        print("Player {} won!".format(PLAYER_CHECKERS[current_player]))
        break
    elif check_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    current_player = (current_player + 1) % NUM_PLAYERS
```