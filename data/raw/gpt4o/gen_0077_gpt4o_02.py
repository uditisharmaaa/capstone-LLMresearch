# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 77
# filename        : gen_0077_gpt4o_02.py
# timestamp       : 2026-02-19T21:00:37Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 2
# style_text      : Write in a compact style, minimizing lines of code.
# tokens_input    : 389
# tokens_output   : 552
# tokens_total    : 941
# cost_usd        : 0.006493
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


import os
import random

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
players = ['X', 'O']
symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def clear(): os.system('clear')

def print_board():
    clear()
    print('   ' + '   '.join(symbols))
    print('+---' * COLS + '+')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('+---' * COLS + '+')

def is_valid_column(col): return 0 <= col < COLS and board[0][col] == ' '

def drop_checker(col, checker):
    for row in reversed(range(ROWS)):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row, col

def check_win(row, col, checker):
    def count(dx, dy): 
        r, c, cnt = row + dy, col + dx, 0
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == checker:
            cnt, r, c = cnt + 1, r + dy, c + dx
        return cnt
    return any(count(dx, dy) + count(-dx, -dy) >= 3 for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)])

def is_draw(): return all(board[0][col] != ' ' for col in range(COLS))

def main():
    current_player = random.choice(players)
    while True:
        print_board()
        print(f"{current_player}'s turn. Choose a column (A-G): ", end='')
        col_input = input().strip().upper()
        if col_input in symbols:
            col = symbols.index(col_input)
            if is_valid_column(col):
                row, col = drop_checker(col, current_player)
                if check_win(row, col, current_player):
                    print_board()
                    print(f"{current_player} won!")
                    break
                if is_draw():
                    print_board()
                    print("It's a draw!")
                    break
                current_player = players[(players.index(current_player) + 1) % PLAYERS]
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid input. Try again.")

if __name__ == '__main__':
    main()
