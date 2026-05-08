# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 374
# filename        : gen_0374_sonnet46_14.py
# timestamp       : 2026-05-07T17:52:56Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 416
# tokens_output   : 677
# tokens_total    : 1093
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
#   Write with minimal whitespace and short variable names.
# ====================================================================

import os
import random

COLS=7
ROWS=6
NUM_PLAYERS=2

def mk_board():
    return [[' ']*COLS for _ in range(ROWS)]

def print_board(b):
    os.system('clear')
    print('   '+'   '.join(chr(65+i) for i in range(COLS)))
    sep='+---'*COLS+'+'
    for r in range(ROWS):
        print(sep)
        print('|'+'|'.join(' '+b[r][c]+' ' for c in range(COLS))+'|')
    print(sep)

def get_col(b):
    while True:
        s=input('Enter column (A-G): ').strip()
        if len(s)!=1 or not s.isalpha():
            print('Invalid input.')
            continue
        s=s.upper()
        if s<'A' or s>'G':
            print('Letter out of range.')
            continue
        c=ord(s)-65
        if b[0][c]!=' ':
            print('Column full.')
            continue
        return c

def drop(b,c,ch):
    for r in range(ROWS-1,-1,-1):
        if b[r][c]==' ':
            b[r][c]=ch
            return r

def check_win(b,r,c,ch):
    def cnt(dr,dc):
        n=0
        rr,cc=r+dr,c+dc
        while 0<=rr<ROWS and 0<=cc<COLS and b[rr][cc]==ch:
            n+=1
            rr+=dr
            cc+=dc
        return n
    dirs=[(0,1),(1,0),(1,1),(1,-1)]
    for dr,dc in dirs:
        if 1+cnt(dr,dc)+cnt(-dr,-dc)>=4:
            return True
    return False

def board_full(b):
    return all(b[0][c]!=' ' for c in range(COLS))

def main():
    b=mk_board()
    players=['X','O']
    cur=random.randint(0,NUM_PLAYERS-1)
    print_board(b)
    while True:
        ch=players[cur]
        print(f'Player {ch}\'s turn')
        c=get_col(b)
        r=drop(b,c,ch)
        print_board(b)
        if check_win(b,r,c,ch):
            print(f'Player {ch} won!')
            break
        if board_full(b):
            print('Draw!')
            break
        cur=(cur+1)%NUM_PLAYERS

main()