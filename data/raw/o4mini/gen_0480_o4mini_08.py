# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 480
# filename        : gen_0480_o4mini_08.py
# timestamp       : 2026-05-07T22:48:27Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 389
# tokens_output   : 717
# tokens_total    : 1106
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
#   Write with a focus on code readability over brevity.
# ====================================================================

```python
import os
import random

# Global constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear_screen():
    os.system('clear')

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    clear_screen()
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column, board):
    if column not in COLUMN_LABELS:
        return False
    column_index = COLUMN_LABELS.index(column)
    return board[0][column_index] == ' '

def get_player_input(player, board):
    while True:
        column = input(f"Player {player} ({'X' if player == 1 else 'O'}), choose a column (A-G): ").strip().upper()
        if column in COLUMN_LABELS and is_valid_column(column, board):
            return COLUMN_LABELS.index(column)
        print("Invalid input. Please choose a valid column.")

def drop_checker(board, column_index, checker):
    for row in reversed(board):
        if row[column_index] == ' ':
            row[column_index] = checker
            break

def check_for_win(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if all(board[row][col + i] == checker for i in range(4)):
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if all(board[row + i][col] == checker for i in range(4)):
                return True

    # Check diagonal (down-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if all(board[row + i][col + i] == checker for i in range(4)):
                return True

    # Check diagonal (down-left)
    for row in range(ROWS - 3):
        for col in range(3, COLUMNS):
            if all(board[row + i][col - i] == checker for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = create_board()
    current_player = random.randint(1, PLAYERS)
    checker = {1: 'X', 2: 'O'}

    print_board(board)

    while True:
        print_board(board)
        column_index = get_player_input(current_player, board)
        drop_checker(board, column_index, checker[current_player])

        if check_for_win(board, checker[current_player]):
            print_board(board)
            print(f"Player {current_player} ({checker[current_player]}) won!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 1 if current_player == 2 else 2

if __name__ == "__main__":
    main()
```