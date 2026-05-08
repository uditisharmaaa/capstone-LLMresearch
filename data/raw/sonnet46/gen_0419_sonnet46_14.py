# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 419
# filename        : gen_0419_sonnet46_14.py
# timestamp       : 2026-05-07T19:17:05Z
# model           : @vertexai/anthropic.claude-sonnet-4-6
# model_short     : sonnet46
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 416
# tokens_output   : 731
# tokens_total    : 1147
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
NPLAYERS=2

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

def drop(b,col,ch):
    for r in range(ROWS-1,-1,-1):
        if b[r][col]==' ':
            b[r][col]=ch
            return r
    return -1

def check_win(b,r,c,ch):
    def count(dr,dc):
        cnt=0
        nr,nc=r+dr,c+dc
        while 0<=nr<ROWS and 0<=nc<COLS and b[nr][nc]==ch:
            cnt+=1
            nr+=dr
            nc+=dc
        return cnt
    for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]:
        if 1+count(dr,dc)+count(-dr,-dc)>=4:
            return True
    return False

def full(b):
    return all(b[0][c]!=' ' for c in range(COLS))

def get_move(b,player,ch):
    while True:
        try:
            s=input(f'Player {player} ({ch}), choose column (A-G): ').strip()
            if len(s)!=1 or not s.isalpha():
                print('Invalid input. Enter a letter A-G.')
                continue
            s=s.upper()
            if s<'A' or s>'G':
                print('Invalid column. Enter a letter A-G.')
                continue
            col=ord(s)-65
            if b[0][col]!=' ':
                print('Column full. Choose another.')
                continue
            return col
        except EOFError:
            print('Invalid input. Enter a letter A-G.')

def main():
    b=mk_board()
    checkers=['X','O']
    cur=random.randint(0,NPLAYERS-1)
    players=[1,2]
    print_board(b)
    while True:
        p=players[cur]
        ch=checkers[cur]
        col=get_move(b,p,ch)
        r=drop(b,col,ch)
        print_board(b)
        if check_win(b,r,col,ch):
            print(f'Player {p} won!')
            return
        if full(b):
            print('Draw!')
            return
        cur=(cur+1)%NPLAYERS

main()