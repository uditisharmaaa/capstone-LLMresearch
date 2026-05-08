# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 164
# filename        : gen_0164_llama_04.py
# timestamp       : 2026-04-06T10:08:52Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 394
# tokens_output   : 743
# tokens_total    : 1137
# cost_usd        : 0.000762
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

```python
import os
import random

# Global constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

def print_board(board):
    os.system('clear')
    print('   A   B   C   D   E   F   G')
    print('+---+---+---+---+---+---+---+')
    for row in board:
        print('|', end='')
        for cell in row:
            print(f' {cell} |', end='')
        print('\n+---+---+---+---+---+---+---+')

def check_win(board, player):
    # Check horizontal
    for row in board:
        for col in range(BOARD_WIDTH - 3):
            if row[col] == player and row[col + 1] == player and row[col + 2] == player and row[col + 3] == player:
                return True

    # Check vertical
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True

    return False

def main():
    board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    players = ['X', 'O']
    current_player = random.choice(players)

    while True:
        print_board(board)
        while True:
            col = input(f"Player {current_player}, choose a column (A-G): ").upper()
            if col < 'A' or col > 'G':
                print("Invalid input. Please enter a letter between A and G.")
            elif board[0][ord(col) - ord('A')]!= ' ':
                print("Column is full. Please choose another column.")
            else:
                break

        col_idx = ord(col) - ord('A')
        for row in range(BOARD_HEIGHT - 1, -1, -1):
            if board[row][col_idx] == ' ':
                board[row][col_idx] = current_player
                break

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break

        if all(all(cell!= ' ' for cell in row) for row in board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
```