# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 262
# filename        : gen_0262_llama_12.py
# timestamp       : 2026-04-06T09:45:27Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 393
# tokens_output   : 755
# tokens_total    : 1148
# cost_usd        : 0.000771
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

```python
import os
import random

# Constants
BOARD_COLS = 7
BOARD_ROWS = 6
NUM_PLAYERS = 2
PLAYERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(' {} |'.format(cell), end='')
        print('\n+---+---+---+---+---+---+---+')
    print()

def is_valid_move(board, col):
    return board[0][col] == ' '

def get_player_move(player, board):
    while True:
        move = input("Player {}, choose a column (A-G): ".format(player)).strip().upper()
        if move not in 'ABCDEFG':
            print("Invalid input. Please enter a letter between A and G.")
        elif not is_valid_move(board, ord(move) - ord('A')):
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def make_move(board, player, col):
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            break

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

def is_draw(board):
    return all(cell!= ' ' for row in board for cell in row)

def play_game():
    board = create_board()
    players = list(PLAYERS)
    random.shuffle(players)
    current_player = 0

    print_board(board)

    while True:
        player = players[current_player]
        col = get_player_move(player, board)
        make_move(board, player, col)
        print_board(board)

        if check_win(board, player):
            print("Player {} won!".format(player))
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS

play_game()
```