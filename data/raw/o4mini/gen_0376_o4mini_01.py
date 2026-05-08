# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 376
# filename        : gen_0376_o4mini_01.py
# timestamp       : 2026-05-07T17:53:19Z
# model           : @gpt-4o/o4-mini
# model_short     : o4mini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 391
# tokens_output   : 652
# tokens_total    : 1043
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLUMNS = 7
PLAYERS = 2
COLUMN_LABELS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]

def print_board(board):
    os.system('clear')
    print("   " + "   ".join(COLUMN_LABELS))
    print("+---" * COLUMNS + "+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---" * COLUMNS + "+")

def is_valid_column(column, board):
    return 0 <= column < COLUMNS and board[0][column] == ' '

def drop_checker(column, player, board):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            return (row, column)

def check_win(row, col, player, board):
    def count_in_direction(dr, dc):
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLUMNS and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        return count

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        if count_in_direction(dr, dc) + count_in_direction(-dr, -dc) + 1 >= 4:
            return True
    return False

def is_draw(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def get_player_input(board):
    while True:
        column_letter = input("Choose a column (A-G): ").strip().upper()
        if column_letter in COLUMN_LABELS:
            column = COLUMN_LABELS.index(column_letter)
            if is_valid_column(column, board):
                return column
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid input. Please choose a letter between A and G.")

def main():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)
    
    print_board(board)
    print(f"{current_player} goes first!")

    while True:
        print(f"{current_player}'s turn.")
        column = get_player_input(board)
        row, col = drop_checker(column, current_player, board)
        print_board(board)

        if check_win(row, col, current_player, board):
            print(f"{current_player} won!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        current_player = players[1] if current_player == players[0] else players[0]

if __name__ == "__main__":
    main()
```