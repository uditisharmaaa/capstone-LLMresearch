# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 269
# filename        : gen_0269_llama_04.py
# timestamp       : 2026-04-06T09:47:27Z
# model           : meta-llama/llama-3.1-70b-instruct
# model_short     : llama
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 394
# tokens_output   : 847
# tokens_total    : 1241
# cost_usd        : 0.000840
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
import string

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYERS = ['X', 'O']

def create_board():
    """Create a 2D board with spaces"""
    return [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def print_board(board):
    """Print the board with column labels"""
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
    """Get player move, validating input"""
    while True:
        move = input(f"Player {player}, choose a column (A-G): ")
        if move.upper() in string.ascii_uppercase[:BOARD_WIDTH]:
            return string.ascii_uppercase.index(move.upper())
        print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, column, player):
    """Drop the checker to the lowest available row in the chosen column"""
    for row in reversed(board):
        if row[column] == ' ':
            row[column] = player
            return

def check_win(board, player):
    """Check for a win: 4 in a row horizontally, vertically, or diagonally"""
    # Check horizontal locations for win
    for c in range(BOARD_WIDTH - 3):
        for r in range(BOARD_HEIGHT):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(BOARD_WIDTH):
        for r in range(BOARD_HEIGHT - 3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(BOARD_WIDTH - 3):
        for r in range(BOARD_HEIGHT - 3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(BOARD_WIDTH - 3):
        for r in range(3, BOARD_HEIGHT):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

def main():
    board = create_board()
    players = PLAYERS[:]
    random.shuffle(players)  # Randomly select which player goes first
    current_player = 0

    while True:
        print_board(board)
        column = get_player_move(players[current_player])
        if ' ' not in board[0][column]:  # Check if column is full
            print("Column is full. Please choose another column.")
            continue
        drop_checker(board, column, players[current_player])
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} won!")
            break
        if all(cell!= ' ' for row in board for cell in row):  # Check for draw
            print_board(board)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```