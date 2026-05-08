# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 226
# filename        : gen_0226_gemini_06.py
# timestamp       : 2026-04-06T10:20:19Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 376
# tokens_output   : 943
# tokens_total    : 1319
# cost_usd        : 0.000415
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_CHARS = ["X", "O"]


def create_board():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    os.system('clear')
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for row in board:
        print("+---" * COLS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * COLS + "+")


def get_player_move(board, player):
    while True:
        col_input = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not col_input.isalpha() or len(col_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = ord(col_input) - ord('A')
        if not 0 <= col < COLS:
            print("Invalid column. Choose a column between A and G.")
            continue
        if board[0][col] != " ":
            print("Column is full. Choose another column.")
            continue
        return col


def drop_checker(board, col, player_char):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player_char
            return row


def check_win(board, row, col, player_char):
    # Horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False


def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def main():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    print_board(board)

    while True:
        col = get_player_move(board, current_player)
        row = drop_checker(board, col, PLAYER_CHARS[current_player])
        print_board(board)

        if check_win(board, row, col, PLAYER_CHARS[current_player]):
            print(f"Player {current_player + 1} won!")
            break

        if check_draw(board):
            print("Draw!")
            break

        current_player = (current_player + 1) % PLAYERS


if __name__ == "__main__":
    main()
```