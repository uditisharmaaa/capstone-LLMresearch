# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 237
# filename        : gen_0237_gemini_02.py
# timestamp       : 2026-04-06T10:23:37Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 377
# tokens_output   : 775
# tokens_total    : 1152
# cost_usd        : 0.000348
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
#   Write in a compact style, minimizing lines of code.
# ====================================================================

```python
import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, P1, P2 = ' ', 'X', 'O'

def create_board(): return [[EMPTY] * COLS for _ in range(ROWS)]
def print_board(board):
    os.system('clear')
    print('  ' + '   '.join(chr(ord('A') + i) for i in range(COLS)))
    for row in board:
        print('+---' * COLS + '+')
        print('| ' + ' | '.join(row) + ' |')
    print('+---' * COLS + '+')

def get_player_move(board, player):
    while True:
        col = input(f"Player {player}, choose a column (A-G): ").upper()
        if not 'A' <= col <= 'G': print("Invalid input. Choose A-G."); continue
        col_idx = ord(col) - ord('A')
        if all(board[row][col_idx] != EMPTY for row in range(ROWS)):
            print("Column full. Choose another."); continue
        return col_idx

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player; return

def check_win(board, player):
    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)): return True
    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row + i][col] == player for i in range(4)): return True
    # Diagonal (top-left to bottom-right)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)): return True
    # Diagonal (top-right to bottom-left)
    for row in range(ROWS - 3):
        for col in range(3, COLS):
            if all(board[row + i][col - i] == player for i in range(4)): return True
    return False

def is_board_full(board): return all(board[0][col] != EMPTY for col in range(COLS))

def play_connect_4():
    board = create_board()
    current_player = P1 if random.random() < 0.5 else P2
    print_board(board)

    while True:
        col = get_player_move(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = P2 if current_player == P1 else P1

if __name__ == "__main__":
    play_connect_4()
```