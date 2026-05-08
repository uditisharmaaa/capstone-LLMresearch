# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 391
# filename        : gen_0391_o4mini_01.py
# timestamp       : 2026-05-07T18:00:02Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 742
# tokens_total    : 1133
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column):
    return column in COLUMN_LABELS

def is_column_full(board, col_index):
    return board[0][col_index] != " "

def get_column_index(column):
    return COLUMN_LABELS.index(column)

def drop_checker(board, col_index, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col_index] == " ":
            board[row][col_index] = checker
            break

def check_winner(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == checker and all(board[row][col + i] == checker for i in range(4)):
                return True
    # Check vertical
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if board[row][col] == checker and all(board[row + i][col] == checker for i in range(4)):
                return True
    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == checker and all(board[row + i][col + i] == checker for i in range(4)):
                return True
    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == checker and all(board[row - i][col + i] == checker for i in range(4)):
                return True
    return False

def is_draw(board):
    return all(board[0][col] != " " for col in range(COLUMNS))

def main():
    board = create_board()
    players = ["X", "O"]
    current_player = random.randint(0, PLAYERS - 1)
    game_over = False

    print_board(board)
    while not game_over:
        print(f"Player {players[current_player]}'s turn. Enter a column (A-G):")
        column = input().strip().upper()

        if not is_valid_column(column):
            print("Invalid column. Please enter a letter between A and G.")
            continue

        col_index = get_column_index(column)
        if is_column_full(board, col_index):
            print("Column is full. Choose another column.")
            continue

        drop_checker(board, col_index, players[current_player])
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} won!")
            game_over = True
        elif is_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()
```