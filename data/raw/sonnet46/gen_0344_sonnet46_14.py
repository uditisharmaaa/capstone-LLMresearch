# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 344
# filename        : gen_0344_sonnet46_14.py
# timestamp       : 2026-05-07T17:44:17Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 416
# tokens_output   : 712
# tokens_total    : 1128
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
    print('   A   B   C   D   E   F   G')
    sep='+---+---+---+---+---+---+---+'
    for r in range(ROWS):
        print(sep)
        row='|'
        for c in range(COLS):
            row+=' '+b[r][c]+' |'
        print(row)
    print(sep)

def get_move(b,p):
    cols='ABCDEFG'
    while True:
        raw=input(f'Player {p}, choose a column (A-G): ')
        if len(raw)!=1 or not raw.isalpha():
            print('Invalid input. Enter a single letter A-G.')
            continue
        ch=raw.upper()
        if ch not in cols:
            print('Invalid column. Choose A through G.')
            continue
        ci=cols.index(ch)
        if b[0][ci]!=' ':
            print('Column full. Choose another.')
            continue
        return ci

def drop(b,ci,checker):
    for r in range(ROWS-1,-1,-1):
        if b[r][ci]==' ':
            b[r][ci]=checker
            return r

def check_win(b,r,c,checker):
    def count(dr,dc):
        cnt=0
        nr,nc=r+dr,c+dc
        while 0<=nr<ROWS and 0<=nc<COLS and b[nr][nc]==checker:
            cnt+=1
            nr+=dr
            nc+=dc
        return cnt
    dirs=[(0,1),(1,0),(1,1),(1,-1)]
    for dr,dc in dirs:
        if 1+count(dr,dc)+count(-dr,-dc)>=4:
            return True
    return False

def board_full(b):
    return all(b[0][c]!=' ' for c in range(COLS))

def main():
    b=mk_board()
    checkers=['X','O']
    players=[1,2]
    random.shuffle(players)
    turn=0
    print_board(b)
    while True:
        pidx=turn%NUM_PLAYERS
        p=players[pidx]
        checker=checkers[pidx]
        ci=get_move(b,p)
        r=drop(b,ci,checker)
        print_board(b)
        if check_win(b,r,ci,checker):
            print(f'Player {p} won!')
            return
        if board_full(b):
            print('Draw!')
            return
        turn+=1

main()