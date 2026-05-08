# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 306
# filename        : gen_0306_o4mini_06.py
# timestamp       : 2026-05-07T17:19:22Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 6
# style_text      : Write as concisely as possible, avoiding any redundancy.
# tokens_input    : 390
# tokens_output   : 617
# tokens_total    : 1007
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
EMPTY, TOKENS = " ", ["X", "O"]

def clear(): os.system('clear')

def print_board(board):
    clear()
    print("   " + "   ".join("ABCDEFG"))
    print("+---" * COLS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLS + "+")

def drop_piece(board, col, token):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = token
            return True
    return False

def is_valid_move(board, col):
    return 0 <= col < COLS and board[0][col] == EMPTY

def check_win(board, token):
    for r in range(ROWS):
        for c in range(COLS):
            if c + 3 < COLS and all(board[r][c + i] == token for i in range(4)): return True
            if r + 3 < ROWS and all(board[r + i][c] == token for i in range(4)): return True
            if r + 3 < ROWS and c + 3 < COLS and all(board[r + i][c + i] == token for i in range(4)): return True
            if r + 3 < ROWS and c - 3 >= 0 and all(board[r + i][c - i] == token for i in range(4)): return True
    return False

def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

def get_input():
    while True:
        move = input("Choose a column (A-G): ").strip().upper()
        if len(move) == 1 and 'A' <= move <= 'G': return ord(move) - ord('A')
        print("Invalid input. Try again.")

def main():
    board = [[EMPTY] * COLS for _ in range(ROWS)]
    current_player = random.randint(0, PLAYERS - 1)
    
    while True:
        print_board(board)
        print(f"Player {TOKENS[current_player]}'s turn.")
        col = get_input()
        if is_valid_move(board, col):
            drop_piece(board, col, TOKENS[current_player])
            if check_win(board, TOKENS[current_player]):
                print_board(board)
                print(f"Player {TOKENS[current_player]} won!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = 1 - current_player
        else:
            print("Column full or invalid. Try again.")

if __name__ == "__main__":
    main()
```