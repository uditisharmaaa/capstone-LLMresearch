# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 187
# filename        : gen_0187_llama_12.py
# timestamp       : 2026-04-06T10:13:25Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 393
# tokens_output   : 763
# tokens_total    : 1156
# cost_usd        : 0.000777
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

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
PLAYERS = ['X', 'O']

def create_board():
    return [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| {} |'.format(' | '.join(row)))
        print('+---+---+---+---+---+---+---+')

def is_valid_input(column):
    return column.upper() in 'ABCDEFG'

def is_valid_move(board, column):
    return board[0][column] == ' '

def get_move():
    while True:
        move = input("Enter a column (A-G): ")
        if is_valid_input(move):
            column = ord(move.upper()) - ord('A')
            if is_valid_move(board, column):
                return column
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid input. Try again.")

def drop_checker(board, player, column):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            return

def check_win(board, player):
    # Check horizontal locations for win
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                return True

    # Check vertical locations for win
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS - 3):
            if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                return True

    # Check positively sloped diagonals
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                return True

    # Check negatively sloped diagonals
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player:
                return True

def check_draw(board):
    return all(board[0][col]!= ' ' for col in range(NUM_COLS))

def game():
    global board
    board = create_board()
    player = random.choice(PLAYERS)
    while True:
        print_board(board)
        print("Player", player, "turn")
        column = get_move()
        drop_checker(board, player, column)
        if check_win(board, player):
            print_board(board)
            print("Player", player, "won!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = 'O' if player == 'X' else 'X'

game()
```