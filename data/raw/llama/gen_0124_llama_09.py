# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 124
# filename        : gen_0124_llama_09.py
# timestamp       : 2026-04-06T09:57:59Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 9
# style_text      : Write using only basic Python features a first-year student would know.
# tokens_input    : 394
# tokens_output   : 749
# tokens_total    : 1143
# cost_usd        : 0.000767
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

# Global constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Initialize the board with spaces
board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board():
    os.system('clear')
    print('  A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print()
        print('+---+---+---+---+---+---+---+')

def get_player_move(player):
    while True:
        move = input(f"Player {player}, choose a column (A-G): ")
        if len(move)!= 1 or not move.isalpha():
            print("Invalid input. Please enter a letter.")
            continue
        column = ord(move.upper()) - ord('A')
        if column < 0 or column >= BOARD_WIDTH:
            print("Invalid column. Please choose a column between A and G.")
            continue
        for row in reversed(board):
            if row[column] == ' ':
                row[column] = 'X' if player == 1 else 'O'
                return
        print("Column is full. Please choose another column.")

def check_win():
    # Check horizontal wins
    for row in board:
        for i in range(BOARD_WIDTH - 3):
            if row[i]!= ' ' and row[i] == row[i+1] == row[i+2] == row[i+3]:
                return row[i]

    # Check vertical wins
    for col in range(BOARD_WIDTH):
        for i in range(BOARD_HEIGHT - 3):
            if board[i][col]!= ' ' and board[i][col] == board[i+1][col] == board[i+2][col] == board[i+3][col]:
                return board[i][col]

    # Check diagonal wins (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col]!= ' ' and board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                return board[row][col]

    # Check diagonal wins (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col]!= ' ' and board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
                return board[row][col]

    return None

def main():
    random.seed()
    player_turn = random.randint(1, NUM_PLAYERS)
    print_board()
    while True:
        get_player_move(player_turn)
        print_board()
        winner = check_win()
        if winner is not None:
            print(f"Player {1 if winner == 'X' else 2} won!")
            break
        if all(cell!= ' ' for row in board for cell in row):
            print("It's a draw!")
            break
        player_turn = 2 if player_turn == 1 else 1

if __name__ == "__main__":
    main()
```