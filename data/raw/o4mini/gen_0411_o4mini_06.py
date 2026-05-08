# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 411
# filename        : gen_0411_o4mini_06.py
# timestamp       : 2026-05-07T19:14:38Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 551
# tokens_total    : 941
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
#   Write as concisely as possible, avoiding any redundancy.
# ====================================================================

```python
import os, random

ROWS, COLS, PLAYERS = 6, 7, 2
EMPTY, P1, P2 = ' ', 'X', 'O'

def clear_screen(): os.system('clear')
def init_board(): return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
def print_board(board):
    clear_screen()
    print("   " + "   ".join("ABCDEFG"))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def valid_move(board, col): return col.isalpha() and 'A' <= col <= 'G' and board[0][ord(col) - 65] == EMPTY
def make_move(board, col, symbol):
    col = ord(col) - 65
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = symbol
            return row, col

def is_winner(board, r, c, symbol):
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:
        count = 0
        for i in range(-3, 4):
            nr, nc = r + dr * i, c + dc * i
            if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == symbol:
                count += 1
                if count == 4: return True
            else: count = 0
    return False

def full_board(board): return all(board[0][col] != EMPTY for col in range(COLS))

def main():
    board = init_board()
    players = [(P1, "Player 1"), (P2, "Player 2")]
    random.shuffle(players)
    print_board(board)

    while True:
        symbol, name = players[0]
        col = input(f"{name}'s turn ({symbol}). Choose column (A-G): ").strip().upper()
        if not valid_move(board, col): continue
        r, c = make_move(board, col, symbol)
        print_board(board)
        if is_winner(board, r, c, symbol):
            print(f"{name} won!")
            break
        if full_board(board):
            print("It's a draw!")
            break
        players.reverse()

if __name__ == "__main__": main()
```