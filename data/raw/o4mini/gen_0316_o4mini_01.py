# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 316
# filename        : gen_0316_o4mini_01.py
# timestamp       : 2026-05-07T17:31:01Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 792
# tokens_total    : 1183
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
COLUMNS = 7
NUM_PLAYERS = 2
COLUMN_LABELS = ["A", "B", "C", "D", "E", "F", "G"]

def create_board():
    return [[" " for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def get_column_input(board):
    while True:
        column_input = input("Choose a column (A-G): ").strip()
        if column_input in COLUMN_LABELS:
            column_index = COLUMN_LABELS.index(column_input)
            if board[0][column_index] == " ":
                return column_index
            else:
                print("Column is full. Choose another column.")
        else:
            print("Invalid input. Please choose a letter between A and G.")

def drop_checker(board, column, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = checker
            return

def check_win(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == checker:
                return True
    
    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLUMNS):
            if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == checker:
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(ROWS - 3):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == checker:
                return True
    
    # Check diagonal (top-left to bottom-right)
    for row in range(3, ROWS):
        for col in range(COLUMNS - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3] == checker:
                return True
    
    return False

def is_draw(board):
    for col in range(COLUMNS):
        if board[0][col] == " ":
            return False
    return True

def main():
    board = create_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    
    print_board(board)
    print(f"{current_player} goes first!")
    
    while True:
        print_board(board)
        print(f"{current_player}'s turn.")
        
        column = get_column_input(board)
        drop_checker(board, column, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} won!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    main()
```