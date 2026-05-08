# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 366
# filename        : gen_0366_o4mini_06.py
# timestamp       : 2026-05-07T17:50:35Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 556
# tokens_total    : 946
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

```python
import os
import random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, PLAYER1, PLAYER2 = ' ', 'X', 'O'
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(col, board):
    return col in COLUMN_LABELS and board[0][COLUMN_LABELS.index(col)] == EMPTY

def drop_checker(board, col, checker):
    col_idx = COLUMN_LABELS.index(col)
    for row in reversed(board):
        if row[col_idx] == EMPTY:
            row[col_idx] = checker
            return

def check_winner(board, checker):
    for r in range(ROWS):
        for c in range(COLS):
            if c <= COLS - 4 and all(board[r][c+i] == checker for i in range(4)): return True
            if r <= ROWS - 4 and all(board[r+i][c] == checker for i in range(4)): return True
            if r <= ROWS - 4 and c <= COLS - 4 and all(board[r+i][c+i] == checker for i in range(4)): return True
            if r <= ROWS - 4 and c >= 3 and all(board[r+i][c-i] == checker for i in range(4)): return True
    return False

def is_draw(board):
    return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = create_board()
    players = [PLAYER1, PLAYER2]
    current_player = random.choice(players)
    print_board(board)
    while True:
        col = input(f"{current_player}'s turn (A-G): ").strip().upper()
        if is_valid_column(col, board):
            drop_checker(board, col, current_player)
            print_board(board)
            if check_winner(board, current_player):
                print(f"{current_player} won!")
                break
            if is_draw(board):
                print("It's a draw!")
                break
            current_player = PLAYER1 if current_player == PLAYER2 else PLAYER2
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
```