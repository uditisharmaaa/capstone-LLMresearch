# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 355
# filename        : gen_0355_opus46_10.py
# timestamp       : 2026-05-07T17:47:35Z
# model           : @vertexai/anthropic.claude-opus-4-6
# model_short     : opus46
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 419
# tokens_output   : 1380
# tokens_total    : 1799
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


def get_column_index(letter):
    return ord(letter) - ord('A')


def is_valid_column_letter(letter):
    if len(letter) != 1:
        return False
    if not letter.isalpha():
        return False
    if letter not in COLUMN_LABELS:
        return False
    return True


def is_column_full(board, col):
    return board[0][col] != ' '


def drop_checker(board, col, checker):
    for r in range(NUM_ROWS - 1, -1, -1):
        if board[r][col] == ' ':
            board[r][col] = checker
            return r
    return -1


def check_direction(board, row, col, d_row, d_col, checker):
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


def check_horizontal(board, checker):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS - 3):
            if check_direction(board, r, c, 0, 1, checker):
                return True
    return False


def check_vertical(board, checker):
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS):
            if check_direction(board, r, c, 1, 0, checker):
                return True
    return False


def check_diagonal_down_right(board, checker):
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if check_direction(board, r, c, 1, 1, checker):
                return True
    return False


def check_diagonal_down_left(board, checker):
    for r in range(NUM_ROWS - 3):
        for c in range(3, NUM_COLS):
            if check_direction(board, r, c, 1, -1, checker):
                return True
    return False


def check_win(board, checker):
    if check_horizontal(board, checker):
        return True
    if check_vertical(board, checker):
        return True
    if check_diagonal_down_right(board, checker):
        return True
    if check_diagonal_down_left(board, checker):
        return True
    return False


def is_board_full(board):
    for c in range(NUM_COLS):
        if board[0][c] == ' ':
            return False
    return True


def get_player_move(board, checker):
    while True:
        user_input = input("Player " + checker + ", choose a column (A-G): ")
        if not is_valid_column_letter(user_input.upper() if len(user_input) == 1 else user_input):
            print("Invalid input. Please enter a letter from A to G.")
            continue
        letter = user_input.upper()
        col = get_column_index(letter)
        if is_column_full(board, col):
            print("Column " + letter + " is full. Choose another column.")
            continue
        return col


def select_first_player():
    checkers = ['X', 'O']
    index = random.randint(0, NUM_PLAYERS - 1)
    return checkers[index]


def switch_player(checker):
    if checker == 'X':
        return 'O'
    else:
        return 'X'


def play_game():
    board = create_board()
    current_checker = select_first_player()

    clear_screen()
    print_board(board)
    print("Player " + current_checker + " goes first!")

    while True:
        col = get_player_move(board, current_checker)
        drop_checker(board, col, current_checker)

        clear_screen()
        print_board(board)

        if check_win(board, current_checker):
            print("Player " + current_checker + " won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_checker = switch_player(current_checker)


def main():
    play_game()


if __name__ == '__main__':
    main()
```