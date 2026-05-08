# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 432
# filename        : gen_0432_o4mini_05.py
# timestamp       : 2026-05-07T22:33:26Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 387
# tokens_output   : 723
# tokens_total    : 1110
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
#   Write with descriptive function names and minimal comments.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ["X", "O"]
COLUMN_LABELS = ["A", "B", "C", "D", "E", "F", "G"]

def clear_screen():
    os.system('clear')

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def get_player_input(board, player):
    while True:
        try:
            column = input(f"Player {PLAYER_SYMBOLS[player]}, choose a column (A-G): ").strip().upper()
            if column not in COLUMN_LABELS:
                print("Invalid input. Please choose a column between A and G.")
                continue
            col_index = COLUMN_LABELS.index(column)
            if board[0][col_index] != " ":
                print("Column is full. Choose another column.")
                continue
            return col_index
        except (IndexError, ValueError):
            print("Invalid input. Try again.")

def drop_checker(board, col, symbol):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = symbol
            return row, col

def check_direction(board, row, col, dr, dc, symbol):
    count = 0
    for i in range(-3, 4):
        r, c = row + dr * i, col + dc * i
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_win(board, row, col, symbol):
    return (
        check_direction(board, row, col, 1, 0, symbol) or  # Vertical
        check_direction(board, row, col, 0, 1, symbol) or  # Horizontal
        check_direction(board, row, col, 1, 1, symbol) or  # Diagonal /
        check_direction(board, row, col, 1, -1, symbol)    # Diagonal \
    )

def is_board_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    print_board(board)

    while True:
        col = get_player_input(board, current_player)
        row, col = drop_checker(board, col, PLAYER_SYMBOLS[current_player])
        print_board(board)

        if check_win(board, row, col, PLAYER_SYMBOLS[current_player]):
            print(f"Player {PLAYER_SYMBOLS[current_player]} won!")
            break

        if is_board_full(board):
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % PLAYERS

if __name__ == "__main__":
    main()
```