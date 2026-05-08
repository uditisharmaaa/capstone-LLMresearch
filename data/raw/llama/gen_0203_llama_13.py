# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 203
# filename        : gen_0203_llama_13.py
# timestamp       : 2026-04-06T09:28:44Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 390
# tokens_output   : 823
# tokens_total    : 1213
# cost_usd        : 0.000820
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

```python
import os
import random

# Constants
NUM_PLAYERS = 2
NUM_ROWS = 6
NUM_COLS = 7

# Initialize board with spaces
board = [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} | {} | {} | {} | {} | {} | {} |'.format(*row))
        print('+---+---+---+---+---+---+---+')

def is_valid_move(col):
    return board[0][col] == ' '

def get_move(player):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player)).upper()
        if len(move)!= 1 or not move.isalpha():
            print("Invalid input. Please enter a letter (A-G).")
        elif ord(move) < ord('A') or ord(move) > ord('G'):
            print("Invalid column. Please choose a column between A and G.")
        elif not is_valid_move(ord(move) - ord('A')):
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def make_move(player, col):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = 'X' if player == 1 else 'O'
            return

def check_win(player):
    symbol = 'X' if player == 1 else 'O'
    # Check horizontal
    for row in board:
        for col in range(NUM_COLS - 3):
            if row[col] == symbol and row[col + 1] == symbol and row[col + 2] == symbol and row[col + 3] == symbol:
                return True
    # Check vertical
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if board[row][col] == symbol and board[row + 1][col] == symbol and board[row + 2][col] == symbol and board[row + 3][col] == symbol:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if board[row][col] == symbol and board[row + 1][col + 1] == symbol and board[row + 2][col + 2] == symbol and board[row + 3][col + 3] == symbol:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == symbol and board[row - 1][col + 1] == symbol and board[row - 2][col + 2] == symbol and board[row - 3][col + 3] == symbol:
                return True
    return False

def is_draw():
    return all(board[0][col]!= ' ' for col in range(NUM_COLS))

def main():
    player_turn = random.randint(1, NUM_PLAYERS)
    while True:
        print_board()
        col = get_move(player_turn)
        make_move(player_turn, col)
        if check_win(player_turn):
            print_board()
            print("Player {} won!".format(player_turn))
            break
        if is_draw():
            print_board()
            print("It's a draw!")
            break
        player_turn = 2 if player_turn == 1 else 1

if __name__ == "__main__":
    main()
```