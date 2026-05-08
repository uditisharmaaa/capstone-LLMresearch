# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 436
# filename        : gen_0436_o4mini_09.py
# timestamp       : 2026-05-07T22:34:41Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 391
# tokens_output   : 650
# tokens_total    : 1041
# cost_usd        : 0.000000
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

# Constants
BOARD_ROWS = 6
BOARD_COLS = 7
NUM_PLAYERS = 2

def create_board():
    return [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def print_board(board):
    os.system('clear')
    print("   A   B   C   D   E   F   G")
    print("+---+---+---+---+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+---+---+---+---+")

def is_valid_column(col, board):
    return col in range(BOARD_COLS) and board[0][col] == " "

def drop_checker(board, col, checker):
    for row in range(BOARD_ROWS-1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = checker
            return row, col

def check_win(board, row, col, checker):
    def count(direction_row, direction_col):
        r, c = row, col
        count = 0
        while 0 <= r < BOARD_ROWS and 0 <= c < BOARD_COLS and board[r][c] == checker:
            count += 1
            r += direction_row
            c += direction_col
        return count - 1
    
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        if count(dr, dc) + count(-dr, -dc) >= 3:
            return True
    return False

def is_full(board):
    return all(board[0][col] != " " for col in range(BOARD_COLS))

def get_column_input():
    while True:
        col_input = input("Choose a column (A-G): ").strip()
        if len(col_input) == 1 and col_input in "ABCDEFG":
            return ord(col_input) - ord('A')
        print("Invalid input. Please enter a letter from A-G.")

def main():
    board = create_board()
    player_checkers = ["X", "O"]
    current_player = random.randint(0, NUM_PLAYERS - 1)
    
    print_board(board)
    while True:
        print(f"Player {player_checkers[current_player]}'s turn.")
        
        col = get_column_input()
        while not is_valid_column(col, board):
            print("Column is full or invalid. Choose again.")
            col = get_column_input()
        
        row, col = drop_checker(board, col, player_checkers[current_player])
        print_board(board)
        
        if check_win(board, row, col, player_checkers[current_player]):
            print(f"Player {player_checkers[current_player]} won!")
            break
        
        if is_full(board):
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

main()
```