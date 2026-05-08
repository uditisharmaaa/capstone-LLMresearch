# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 215
# filename        : gen_0215_llama_10.py
# timestamp       : 2026-04-06T10:17:53Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 393
# tokens_output   : 698
# tokens_total    : 1091
# cost_usd        : 0.000728
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

```python
import os
import random

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} | {} | {} | {} | {} | {} | {} |'.format(*row))
        print('+---+---+---+---+---+---+---+')

def get_player_move(player):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player)).strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid column. Please try again.")
        elif board[0][ord(move) - ord('A')]!= ' ':
            print("Column is full. Please try again.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, player, column):
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player
            return

def check_win(board, player):
    # Check horizontal
    for row in board:
        for i in range(len(row) - 3):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == player:
                return True
    # Check vertical
    for col in range(len(board[0])):
        for i in range(len(board) - 3):
            if board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col] == player:
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == player:
                return True
    return False

def check_draw(board):
    return all(cell!= ' ' for row in board for cell in row)

def game():
    global board
    board = create_board()
    print_board(board)
    players = PLAYERS[:]
    random.shuffle(players)
    while True:
        for player in players:
            column = get_player_move(player)
            drop_checker(board, player, column)
            print_board(board)
            if check_win(board, player):
                print("Player {} won!".format(player))
                return
            elif check_draw(board):
                print("It's a draw!")
                return

game()
```