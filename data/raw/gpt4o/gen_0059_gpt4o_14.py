# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 59
# filename        : gen_0059_gpt4o_14.py
# timestamp       : 2026-02-19T20:48:42Z
# model           : openai/gpt-4o
# model_short     : gpt4o
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 525
# tokens_total    : 912
# cost_usd        : 0.006218
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

import os,random

ROWS,COLS,PLAYERS=6,7,2
def clr_scr():os.system('clear')
def init_board():return [[' ' for _ in range(COLS)] for _ in range(ROWS)]
def print_board(b):
    clr_scr()
    print("   A   B   C   D   E   F   G")
    print("+---"*COLS+"+")
    for r in b:
        print("| "+" | ".join(r)+" |")
        print("+---"*COLS+"+")

def get_move(b):
    while True:
        col=input("Choose column (A-G): ").strip().upper()
        if col in 'ABCDEFG':
            c=ord(col)-ord('A')
            if b[0][c]==' ':
                return c
        print("Invalid move. Try again.")

def make_move(b,c,p):
    for r in reversed(range(ROWS)):
        if b[r][c]==' ':
            b[r][c]=p
            break

def check_winner(b,p):
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(b[r][c+i]==p for i in range(4)):return True
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(b[r+i][c]==p for i in range(4)):return True
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(b[r+i][c+i]==p for i in range(4)):return True
    for r in range(3,ROWS):
        for c in range(COLS-3):
            if all(b[r-i][c+i]==p for i in range(4)):return True
    return False

def full_board(b):
    return all(b[0][c]!=' ' for c in range(COLS))

def main():
    b=init_board()
    players=['X','O']
    current=random.choice(players)
    print_board(b)
    while True:
        print(f"Player {current}'s turn.")
        c=get_move(b)
        make_move(b,c,current)
        print_board(b)
        if check_winner(b,current):
            print(f"Player {current} won!")
            break
        if full_board(b):
            print("It's a draw!")
            break
        current='O' if current=='X' else 'X'

if __name__=='__main__':
    main()