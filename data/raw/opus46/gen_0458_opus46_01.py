# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 458
# filename        : gen_0458_opus46_01.py
# timestamp       : 2026-05-07T22:42:28Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 421
# tokens_output   : 1108
# tokens_total    : 1529
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

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

def create_board():
    board = []
    for row in range(NUM_ROWS):
        board.append([" "] * NUM_COLS)
    return board

def print_board(board):
    os.system('clear')
    header = "   "
    for col in range(NUM_COLS):
        header += chr(ord('A') + col) + "   "
    print(header)
    print("+---" * NUM_COLS + "+")
    for row in range(NUM_ROWS):
        line = "|"
        for col in range(NUM_COLS):
            line += " " + board[row][col] + " |"
        print(line)
        print("+---" * NUM_COLS + "+")

def get_column_choice(board, player):
    while True:
        choice = input("Player " + player + ", choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        choice = choice.upper()
        if choice < 'A' or choice > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        col = ord(choice) - ord('A')
        if board[0][col] != " ":
            print("Column " + choice + " is full. Please choose another column.")
            continue
        return col

def drop_checker(board, col, player):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return row
    return -1

def check_win(board, player):
    # Check horizontal
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player and
                board[row][col + 1] == player and
                board[row][col + 2] == player and
                board[row][col + 3] == player):
                return True

    # Check vertical
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if (board[row][col] == player and
                board[row + 1][col] == player and
                board[row + 2][col] == player and
                board[row + 3][col] == player):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player and
                board[row + 1][col + 1] == player and
                board[row + 2][col + 2] == player and
                board[row + 3][col + 3] == player):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == player and
                board[row - 1][col + 1] == player and
                board[row - 2][col + 2] == player and
                board[row - 3][col + 3] == player):
                return True

    return False

def is_board_full(board):
    for col in range(NUM_COLS):
        if board[0][col] == " ":
            return False
    return True

def main():
    board = create_board()
    players = ["X", "O"]
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    print_board(board)

    while True:
        current_player = players[current_player_index]
        col = get_column_choice(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print("Player " + current_player + " won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player_index = (current_player_index + 1) % NUM_PLAYERS

main()
```