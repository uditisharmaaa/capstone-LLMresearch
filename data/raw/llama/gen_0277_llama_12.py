# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 277
# filename        : gen_0277_llama_12.py
# timestamp       : 2026-04-06T09:53:08Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 12
# style_text      : Write in a functional style, avoiding global variables where possible.
# tokens_input    : 393
# tokens_output   : 749
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
#   Write in a functional style, avoiding global variables where possible.
# ====================================================================

```python
import os
import random

NUM_PLAYERS = 2
NUM_ROWS = 6
NUM_COLS = 7
CHECKERS = ["X", "O"]

def create_board():
    return [[" " for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---+---+---+---+---+---+---+")

def get_player_move(player):
    while True:
        move = input(f"Player {player}, choose a column (A-G): ").strip().upper()
        if move not in "ABCDEFG":
            print("Invalid input. Please enter a letter between A and G.")
        elif board[NUM_ROWS - 1][ord(move) - ord('A')]!= " ":
            print("Column is full. Please choose another column.")
        else:
            return ord(move) - ord('A')

def drop_checker(board, player, col):
    for row in range(NUM_ROWS):
        if board[row][col] == " ":
            board[row][col] = CHECKERS[player]
            return

def check_win(board, player):
    checker = CHECKERS[player]
    # Check horizontal wins
    for row in board:
        for i in range(NUM_COLS - 3):
            if row[i] == row[i + 1] == row[i + 2] == row[i + 3] == checker:
                return True
    # Check vertical wins
    for col in range(NUM_COLS):
        for i in range(NUM_ROWS - 3):
            if board[i][col] == board[i + 1][col] == board[i + 2][col] == board[i + 3][col] == checker:
                return True
    # Check diagonal wins (top-left to bottom-right)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == checker:
                return True
    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == checker:
                return True
    return False

def check_draw(board):
    return all(cell!= " " for row in board for cell in row)

def game():
    board = create_board()
    current_player = random.randint(0, 1)
    while True:
        print_board(board)
        col = get_player_move(current_player)
        drop_checker(board, current_player, col)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player + 1} won!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

game()
```