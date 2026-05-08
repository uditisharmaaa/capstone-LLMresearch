# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 470
# filename        : gen_0470_opus46_13.py
# timestamp       : 2026-05-07T22:45:10Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 417
# tokens_output   : 1178
# tokens_total    : 1595
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================



```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for r in range(NUM_ROWS):
        row = []
        for c in range(NUM_COLS):
            row.append(" ")
        board.append(row)
    return board

def print_board(board):
    os.system('clear')
    # Print column labels
    header = "   "
    for c in range(NUM_COLS):
        letter = chr(ord('A') + c)
        header += letter + "   "
    print(header)
    # Print separator
    separator = "+"
    for c in range(NUM_COLS):
        separator += "---+"
    print(separator)
    # Print each row
    for r in range(NUM_ROWS):
        row_str = "|"
        for c in range(NUM_COLS):
            row_str += " " + board[r][c] + " |"
        print(row_str)
        print(separator)

def get_column_choice(board, player):
    while True:
        user_input = input("Player " + player + ", choose a column (A-G): ")
        # Check if input is a single letter
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        user_input = user_input.upper()
        if user_input < 'A' or user_input > 'G':
            print("Invalid input. Please enter a letter A through G.")
            continue
        col = ord(user_input) - ord('A')
        # Check if column is full
        if board[0][col] != " ":
            print("Column " + user_input + " is full. Choose another column.")
            continue
        return col

def drop_checker(board, col, player):
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == " ":
            board[r][col] = player
            return r
    return -1

def check_win(board, player):
    # Check horizontal
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if (board[r][c] == player and board[r][c+1] == player and
                board[r][c+2] == player and board[r][c+3] == player):
                return True
    # Check vertical
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS):
            if (board[r][c] == player and board[r+1][c] == player and
                board[r+2][c] == player and board[r+3][c] == player):
                return True
    # Check diagonal (top-left to bottom-right)
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if (board[r][c] == player and board[r+1][c+1] == player and
                board[r+2][c+2] == player and board[r+3][c+3] == player):
                return True
    # Check diagonal (bottom-left to top-right)
    for r in range(3, NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if (board[r][c] == player and board[r-1][c+1] == player and
                board[r-2][c+2] == player and board[r-3][c+3] == player):
                return True
    return False

def is_board_full(board):
    for c in range(NUM_COLS):
        if board[0][c] == " ":
            return False
    return True

def main():
    board = create_board()
    players = ["X", "O"]
    # Randomly select which player goes first
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)
    while True:
        current_player = players[current_player_index]
        col = get_column_choice(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)
        if check_win(board, current_player):
            print(current_player + " won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break
        current_player_index = (current_player_index + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```