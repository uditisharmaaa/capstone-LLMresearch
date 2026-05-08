# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 264
# filename        : gen_0264_gemini_14.py
# timestamp       : 2026-04-06T10:27:38Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 375
# tokens_output   : 956
# tokens_total    : 1331
# cost_usd        : 0.000420
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

```python
import os
import random

COLS = 7
ROWS = 6
PLAYERS = 2
P1 = "X"
P2 = "O"

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for r in range(ROWS):
        row_str = "+"
        for c in range(COLS):
            row_str += "---+"
        print(row_str)
        row_str = "|"
        for c in range(COLS):
            row_str += " " + board[r][c] + " |"
        print(row_str)
    row_str = "+"
    for c in range(COLS):
        row_str += "---+"
    print(row_str)

def get_player_move(board, player):
    while True:
        col_str = input(f"Player {player}, choose a column (A-G): ").upper()
        if not col_str.isalpha() or len(col_str) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = ord(col_str) - ord('A')
        if not (0 <= col < COLS):
            print("Invalid column. Please choose a column between A and G.")
            continue
        if board[0][col] != " ":
            print("Column is full. Please choose another column.")
            continue
        return col

def drop_checker(board, col, player):
    for r in range(ROWS - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = player
            return

def check_win(board, player):
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
    return False

def check_draw(board):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == " ":
                return False
    return True

def main():
    board = create_board()
    player = random.choice([P1, P2])
    print_board(board)

    while True:
        col = get_player_move(board, player)
        drop_checker(board, col, player)
        print_board(board)

        if check_win(board, player):
            print(f"{player} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        player = P2 if player == P1 else P1

if __name__ == "__main__":
    main()
```