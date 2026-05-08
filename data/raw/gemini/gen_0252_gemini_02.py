# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 252
# filename        : gen_0252_gemini_02.py
# timestamp       : 2026-04-06T10:25:49Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 377
# tokens_output   : 654
# tokens_total    : 1031
# cost_usd        : 0.000299
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
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for row in board:
        print("+---" * COLS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * COLS + "+")

def get_move(board, player):
    while True:
        col_str = input(f"Player {player}, enter column (A-G): ").upper()
        if not 'A' <= col_str <= 'G': continue
        col = ord(col_str) - ord('A')
        if all(board[row][col] != EMPTY for row in range(ROWS)): continue
        return col

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = player
            return row

def check_win(board, row, col, player):
    def count(dr, dc):
        c = 0
        for i in range(-3, 4):
            r, cc = row + i * dr, col + i * dc
            if 0 <= r < ROWS and 0 <= cc < COLS and board[r][cc] == player: c += 1
            else: c = 0
            if c == 4: return True
        return False
    return count(0, 1) or count(1, 0) or count(1, 1) or count(1, -1)

def check_draw(board): return all(board[0][col] != EMPTY for col in range(COLS))

def play_game():
    board = create_board()
    p1, p2 = P1, P2
    current_player = random.choice([p1, p2])
    print_board(board)

    while True:
        col = get_move(board, current_player)
        row = drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, row, col, current_player):
            print(f"{current_player} won!")
            break
        if check_draw(board):
            print("Draw!")
            break

        current_player = p2 if current_player == p1 else p1

if __name__ == "__main__": play_game()
```