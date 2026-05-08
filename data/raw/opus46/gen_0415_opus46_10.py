# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 415
# filename        : gen_0415_opus46_10.py
# timestamp       : 2026-05-07T19:15:54Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1123
# tokens_total    : 1542
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================



```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2

COLUMN_LABELS = [chr(ord('A') + i) for i in range(NUM_COLS)]


def create_board():
    board = []
    for r in range(NUM_ROWS):
        row = []
        for c in range(NUM_COLS):
            row.append(' ')
        board.append(row)
    return board


def clear_screen():
    os.system('clear')


def print_board(board):
    header = "   " + "   ".join(COLUMN_LABELS)
    print(header)
    separator = "+---" * NUM_COLS + "+"
    for r in range(NUM_ROWS):
        print(separator)
        row_str = "|"
        for c in range(NUM_COLS):
            row_str += " " + board[r][c] + " |"
        print(row_str)
    print(separator)


def get_player_checker(player_index):
    if player_index == 0:
        return 'X'
    else:
        return 'O'


def get_column_input(board, player_checker):
    while True:
        user_input = input("Player " + player_checker + ", choose a column (A-G): ")
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        letter = user_input.upper()
        if letter not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter A through G.")
            continue
        col = ord(letter) - ord('A')
        if is_column_full(board, col):
            print("Column " + letter + " is full. Choose another column.")
            continue
        return col


def is_column_full(board, col):
    return board[0][col] != ' '


def drop_checker(board, col, checker):
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = checker
            return r
    return -1


def check_direction(board, row, col, d_row, d_col):
    checker = board[row][col]
    if checker == ' ':
        return False
    count = 0
    for i in range(4):
        r = row + i * d_row
        c = col + i * d_col
        if r < 0 or r >= NUM_ROWS or c < 0 or c >= NUM_COLS:
            return False
        if board[r][c] != checker:
            return False
        count += 1
    return count == 4


def check_win(board):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if board[r][c] == ' ':
                continue
            if check_direction(board, r, c, 0, 1):
                return board[r][c]
            if check_direction(board, r, c, 1, 0):
                return board[r][c]
            if check_direction(board, r, c, 1, 1):
                return board[r][c]
            if check_direction(board, r, c, 1, -1):
                return board[r][c]
    return None


def is_board_full(board):
    for c in range(NUM_COLS):
        if board[0][c] == ' ':
            return False
    return True


def select_first_player():
    return random.randint(0, NUM_PLAYERS - 1)


def play_game():
    board = create_board()
    current_player = select_first_player()

    clear_screen()
    print_board(board)

    while True:
        checker = get_player_checker(current_player)
        col = get_column_input(board, checker)
        drop_checker(board, col, checker)

        clear_screen()
        print_board(board)

        winner = check_win(board)
        if winner is not None:
            print("Player " + winner + " won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS


if __name__ == '__main__':
    play_game()
```