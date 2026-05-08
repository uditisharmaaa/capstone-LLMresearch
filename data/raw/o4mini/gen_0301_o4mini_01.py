# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 301
# filename        : gen_0301_o4mini_01.py
# timestamp       : 2026-05-07T17:17:51Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 654
# tokens_total    : 1045
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

# Global constants
ROWS = 6
COLS = 7
PLAYERS = 2
COLUMN_LABELS = "ABCDEFG"

def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')  # Clear the screen
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def is_valid_column(column, board):
    if column < 0 or column >= COLS:
        return False
    return board[0][column] == " "

def get_column_input():
    while True:
        user_input = input("Choose a column (A-G): ").strip().upper()
        if user_input in COLUMN_LABELS:
            return COLUMN_LABELS.index(user_input)
        print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, column, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = checker
            return row

def check_winner(board, row, column, checker):
    def count_in_direction(dr, dc):
        count = 0
        r, c = row + dr, column + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            count += 1
            r += dr
            c += dc
        return count

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        if count_in_direction(dr, dc) + count_in_direction(-dr, -dc) + 1 >= 4:
            return True
    return False

def is_board_full(board):
    return all(board[0][col] != " " for col in range(COLS))

def main():
    board = create_board()
    players = ["X", "O"]
    current_player = random.randint(0, PLAYERS - 1)
    
    print_board(board)
    while True:
        current_checker = players[current_player]
        print(f"Player {current_checker}'s turn.")
        
        column = -1
        while column == -1 or not is_valid_column(column, board):
            if column != -1:
                print("Invalid column. Try again.")
            column = get_column_input()
        
        row = drop_checker(board, column, current_checker)
        print_board(board)
        
        if check_winner(board, row, column, current_checker):
            print(f"Player {current_checker} won!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
```