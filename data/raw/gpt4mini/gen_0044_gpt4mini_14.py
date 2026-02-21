# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 44
# filename        : gen_0044_gpt4mini_14.py
# timestamp       : 2026-02-19T20:45:37Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 14
# style_text      : Write with minimal whitespace and short variable names.
# tokens_input    : 387
# tokens_output   : 517
# tokens_total    : 904
# cost_usd        : 0.000368
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

ROWS, COLS, PLAYERS = 6, 7, 2
board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board():
 os.system('clear')
 print("   A   B   C   D   E   F   G")
 print("+---+---+---+---+---+---+---+")
 for row in board:
  print('|' + '|'.join(row) + '|')
  print("+---+---+---+---+---+---+---+")

def drop_checker(col, player):
 for r in range(ROWS-1,-1,-1):
  if board[r][col] == ' ':
   board[r][col] = player
   return r
 return -1

def check_win(r, c, player):
 directions = [(1,0), (0,1), (1,1), (1,-1)]
 for dr, dc in directions:
  count = 1
  for d in [1, -1]:
   nr, nc = r, c
   while 0 <= nr + d*dr < ROWS and 0 <= nc + d*dc < COLS and board[nr + d*dr][nc + d*dc] == player:
    count += 1
    nr += d*dr
    nc += d*dc
  if count >= 4:
   return True
 return False

def is_full():
 return all(board[0][c] != ' ' for c in range(COLS))

def main():
 player = 'X' if random.choice([True, False]) else 'O'
 while True:
  print_board()
  col = input(f"Player {player}, choose a column (A-G): ").upper()
  if col not in 'ABCDEFG':
   print("Invalid input. Try again.")
   continue
  col_idx = ord(col) - ord('A')
  if board[0][col_idx] != ' ':
   print("Column full. Try again.")
   continue
  r = drop_checker(col_idx, player)
  if check_win(r, col_idx, player):
   print_board()
   print(f"Player {player} won!")
   break
  if is_full():
   print_board()
   print("It's a draw!")
   break
  player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
 main()