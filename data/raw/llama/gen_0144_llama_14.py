# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 144
# filename        : gen_0144_llama_14.py
# timestamp       : 2026-04-06T10:04:36Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 390
# tokens_output   : 618
# tokens_total    : 1008
# cost_usd        : 0.000666
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

COLUMNS, ROWS, PLAYERS = 7, 6, 2
board = [[' ']*COLUMNS for _ in range(ROWS)]
checkers = ['X', 'O']

def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---+---+---+---+---+---+---+')

def get_column():
    while True:
        col = input("Choose a column: ").strip().upper()
        if len(col)!= 1 or not 'A' <= col <= 'G':
            print("Invalid input. Please enter a letter from A to G.")
        elif board[0][ord(col) - ord('A')]!= ' ':
            print("Column is full. Please choose another column.")
        else:
            return ord(col) - ord('A')

def drop_checker(col, checker):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return

def check_win(checker):
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == checker:
                # Check horizontal
                if col < COLUMNS - 3 and all(board[row][col + i] == checker for i in range(4)):
                    return True
                # Check vertical
                if row < ROWS - 3 and all(board[row + i][col] == checker for i in range(4)):
                    return True
                # Check diagonal (top-left to bottom-right)
                if row < ROWS - 3 and col < COLUMNS - 3 and all(board[row + i][col + i] == checker for i in range(4)):
                    return True
                # Check diagonal (bottom-left to top-right)
                if row > 2 and col < COLUMNS - 3 and all(board[row - i][col + i] == checker for i in range(4)):
                    return True
    return False

def main():
    current_player = random.randint(0, PLAYERS - 1)
    print_board()
    while True:
        col = get_column()
        drop_checker(col, checkers[current_player])
        print_board()
        if check_win(checkers[current_player]):
            print(f"Player {checkers[current_player]} won!")
            break
        current_player = (current_player + 1) % PLAYERS
        if all(all(cell!= ' ' for cell in row) for row in board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
```