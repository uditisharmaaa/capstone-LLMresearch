# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 446
# filename        : gen_0446_opus46_04.py
# timestamp       : 2026-05-07T22:38:57Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1115
# tokens_total    : 1536
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
#   Write in a professional style following PEP 8 conventions strictly.
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
    for row in range(NUM_ROWS):
        board.append([' '] * NUM_COLS)
    return board


def print_board(board):
    os.system('clear')
    header = "   " + "   ".join(COLUMN_LABELS)
    print(header)
    separator = "+---" * NUM_COLS + "+"
    for row in range(NUM_ROWS):
        print(separator)
        row_str = "|"
        for col in range(NUM_COLS):
            row_str += " " + board[row][col] + " |"
        print(row_str)
    print(separator)


def get_column_choice(board, player):
    while True:
        choice = input(f"Player {player}, choose a column (A-G): ")
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid input. Please enter a single letter A through G.")
            continue
        choice = choice.upper()
        if choice not in COLUMN_LABELS:
            print("Invalid column. Please enter a letter A through G.")
            continue
        col = ord(choice) - ord('A')
        if board[0][col] != ' ':
            print("That column is full. Please choose another column.")
            continue
        return col


def drop_checker(board, col, checker):
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row
    return -1


def check_win(board, checker):
    # Check horizontal
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker
                    and board[row][col + 1] == checker
                    and board[row][col + 2] == checker
                    and board[row][col + 3] == checker):
                return True

    # Check vertical
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS):
            if (board[row][col] == checker
                    and board[row + 1][col] == checker
                    and board[row + 2][col] == checker
                    and board[row + 3][col] == checker):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(NUM_ROWS - 3):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker
                    and board[row + 1][col + 1] == checker
                    and board[row + 2][col + 2] == checker
                    and board[row + 3][col + 3] == checker):
                return True

    # Check diagonal (bottom-left to top-right)
    for row in range(3, NUM_ROWS):
        for col in range(NUM_COLS - 3):
            if (board[row][col] == checker
                    and board[row - 1][col + 1] == checker
                    and board[row - 2][col + 2] == checker
                    and board[row - 3][col + 3] == checker):
                return True

    return False


def is_board_full(board):
    for col in range(NUM_COLS):
        if board[0][col] == ' ':
            return False
    return True


def main():
    board = create_board()
    checkers = ['X', 'O']
    current_player = random.randint(0, NUM_PLAYERS - 1)

    print_board(board)

    while True:
        checker = checkers[current_player]
        col = get_column_choice(board, checker)
        drop_checker(board, col, checker)
        print_board(board)

        if check_win(board, checker):
            print(f"{checker} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()
```