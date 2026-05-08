# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 158
# filename        : gen_0158_gemini_13.py
# timestamp       : 2026-04-06T10:07:25Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1095
# tokens_total    : 1469
# cost_usd        : 0.000475
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
#   Write prioritizing correctness and clarity over elegance.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for i in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for j in range(COLS):
            print(f" {board[i][j]} |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid column choice from the player."""
    while True:
        column_choice = input(f"Player {player}, choose a column (A-G): ").upper()
        if not column_choice.isalpha() or len(column_choice) != 1:
            print("Invalid input. Please enter a letter between A and G.")
            continue

        column_index = ord(column_choice) - ord('A')

        if 0 <= column_index < COLS:
            if board[0][column_index] == " ":
                return column_index
            else:
                print("That column is full. Please choose another.")
        else:
            print("Invalid column. Please choose a column between A and G.")

def drop_checker(board, column, player):
    """Drops the player's checker into the chosen column."""
    for i in range(ROWS - 1, -1, -1):
        if board[i][column] == " ":
            board[i][column] = player
            return i, column

def check_win(board, row, col, player):
    """Checks if the current move results in a win."""
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
        if board[i][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        if 0 <= row + i < ROWS and 0 <= col + i < COLS:
            if board[row + i][col + i] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        if 0 <= row + i < ROWS and 0 <= col - i < COLS:
            if board[row + i][col - i] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    """Checks if the board is full (draw)."""
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True

def play_connect_4():
    """Plays a game of Connect 4."""
    board = create_board()
    player1 = PLAYER_X
    player2 = PLAYER_O

    # Randomly choose who goes first
    current_player = random.choice([player1, player2])
    print_board(board)

    while True:
        print_board(board)
        column = get_player_move(board, current_player)
        row, col = drop_checker(board, column, current_player)

        if check_win(board, row, col, current_player):
            print_board(board)
            print(f"Player {current_player} won!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    play_connect_4()
```