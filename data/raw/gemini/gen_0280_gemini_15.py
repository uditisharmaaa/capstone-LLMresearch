# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 280
# filename        : gen_0280_gemini_15.py
# timestamp       : 2026-04-06T10:28:51Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 15
# style_text      : Write in a straightforward, no-frills style.
# tokens_input    : 377
# tokens_output   : 966
# tokens_total    : 1343
# cost_usd        : 0.000424
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
#   Write in a straightforward, no-frills style.
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
    print("  " + "   ".join([chr(65 + i) for i in range(COLS)]))
    for row in board:
        print("+---+" * COLS)
        print("| " + " | ".join(row) + " |")
    print("+---+" * COLS)

def get_player_move(board, player_char):
    while True:
        col_str = input(f"Player {player_char}, choose a column (A-G): ").upper()
        if not col_str.isalpha() or len(col_str) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue
        col = ord(col_str) - ord('A')
        if not (0 <= col < COLS):
            print("Invalid column. Please choose a column between A and G.")
            continue
        if board[0][col] != " ":
            print("Column is full. Please choose another column.")
            continue
        return col

def drop_checker(board, col, player_char):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player_char
            return row

def check_win(board, row, col, player_char):
    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r, c = row + i, col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r, c = row + i, col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def play_game():
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    player_char = PLAYER_CHARS[current_player]
    print_board(board)

    while True:
        col = get_player_move(board, player_char)
        row = drop_checker(board, col, player_char)
        print_board(board)

        if check_win(board, row, col, player_char):
            print(f"Player {player_char} won!")
            break

        if check_draw(board):
            print("Draw!")
            break

        current_player = (current_player + 1) % PLAYERS
        player_char = PLAYER_CHARS[current_player]

if __name__ == "__main__":
    play_game()
```