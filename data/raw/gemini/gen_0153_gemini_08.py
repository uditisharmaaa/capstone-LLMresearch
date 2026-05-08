# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 153
# filename        : gen_0153_gemini_08.py
# timestamp       : 2026-04-06T10:06:20Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1065
# tokens_total    : 1441
# cost_usd        : 0.000464
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
#   Write with a focus on code readability over brevity.
# ====================================================================

```python
import os
import random

# Constants
ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_MARKS = ["X", "O"]

def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+" * COLS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---+" * COLS + "+")

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(column_input) - ord('A')
        if not 0 <= column < COLS:
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][column] != " ":
            print("Column is full. Please choose a different column.")
            continue

        return column

def drop_checker(board, column, player):
    """Drops the player's checker into the specified column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = PLAYER_MARKS[player]
            return

def check_win(board, player):
    """Checks if the player has won the game."""
    mark = PLAYER_MARKS[player]

    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == mark and board[row][col+1] == mark and \
               board[row][col+2] == mark and board[row][col+3] == mark:
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if board[row][col] == mark and board[row+1][col] == mark and \
               board[row+2][col] == mark and board[row+3][col] == mark:
                return True

    # Check positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == mark and board[row+1][col+1] == mark and \
               board[row+2][col+2] == mark and board[row+3][col+3] == mark:
                return True

    # Check negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == mark and board[row-1][col+1] == mark and \
               board[row-2][col+2] == mark and board[row-3][col+3] == mark:
                return True

    return False

def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    """Plays a game of Connect 4."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)  # Randomly choose starting player
    game_over = False

    print_board(board)

    while not game_over:
        column = get_player_move(board, current_player)
        drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player + 1} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    play_game()
```