# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 282
# filename        : gen_0282_gemini_02.py
# timestamp       : 2026-04-06T10:28:56Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 377
# tokens_output   : 652
# tokens_total    : 1029
# cost_usd        : 0.000298
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
EMPTY, X, O = ' ', 'X', 'O'

def create_board(): return [[EMPTY] * COLS for _ in range(ROWS)]
def print_board(board):
    os.system('clear')
    print('  ' + '   '.join(chr(ord('A') + i) for i in range(COLS)))
    for row in board: print('+---+' * COLS); print('| ' + ' | '.join(row) + ' |')
    print('+---+' * COLS)

def get_move(board, player):
    while True:
        move = input(f"Player {player}, enter column (A-G): ").upper()
        if not 'A' <= move <= 'G': print("Invalid input. Enter a letter A-G."); continue
        col = ord(move) - ord('A')
        if board[0][col] != EMPTY: print("Column full. Choose another."); continue
        return col

def drop_checker(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY: board[row][col] = player; return row

def check_win(board, row, col, player):
    def count(dr, dc):
        c = 0; r, cl = row, col
        while 0 <= r < ROWS and 0 <= cl < COLS and board[r][cl] == player: c += 1; r += dr; cl += dc
        return c
    return (count(0, 1) + count(0, -1) - 1 >= 4 or count(1, 0) + count(-1, 0) - 1 >= 4 or
            count(1, 1) + count(-1, -1) - 1 >= 4 or count(1, -1) + count(-1, 1) - 1 >= 4)

def check_draw(board): return all(board[0][col] != EMPTY for col in range(COLS))

def play_game():
    board = create_board()
    players = [X, O]
    current_player = random.choice(players)
    print_board(board)

    while True:
        col = get_move(board, current_player)
        row = drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, row, col, current_player): print(f"{current_player} won!"); break
        if check_draw(board): print("Draw!"); break

        current_player = players[1 - players.index(current_player)]

play_game()
```