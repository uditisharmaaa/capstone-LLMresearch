# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 186
# filename        : gen_0186_gemini_11.py
# timestamp       : 2026-04-06T10:12:56Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 11
# style_text      : Write with extensive docstrings for every function.
# tokens_input    : 375
# tokens_output   : 1080
# tokens_total    : 1455
# cost_usd        : 0.000470
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
#   Write with extensive docstrings for every function.
# ====================================================================

```python
import os
import random

# Constants for board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

def create_board():
    """Creates a 2D list representing the Connect 4 board."""
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for i in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for j in range(COLS):
            print(" " + board[i][j] + " |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets the player's move, validating the input."""
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column_index = ord(column_input) - ord('A')
        if not 0 <= column_index < COLS:
            print("Invalid column. Please enter a letter A-G.")
            continue

        if board[0][column_index] != ' ':
            print("That column is full. Please choose another.")
            continue

        return column_index

def drop_checker(board, column, player):
    """Drops the checker to the lowest available row in the chosen column."""
    for i in range(ROWS - 1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return i

def check_win(board, row, column, player):
    """Checks for a win (4 in a row) horizontally, vertically, or diagonally."""
    # Check horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for i in range(ROWS):
        if board[i][column] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        if 0 <= row + i < ROWS and 0 <= column + i < COLS and board[row + i][column + i] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        if 0 <= row + i < ROWS and 0 <= column - i < COLS and board[row + i][column - i] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

def check_draw(board):
    """Checks if the board is full (draw)."""
    for i in range(COLS):
        if board[0][i] == ' ':
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1 = "X"
    player2 = "O"
    players = [player1, player2]
    current_player = random.choice(players)
    game_over = False

    print_board(board)

    while not game_over:
        column = get_player_move(board, current_player)
        row = drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, row, column, current_player):
            print(f"{current_player} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```