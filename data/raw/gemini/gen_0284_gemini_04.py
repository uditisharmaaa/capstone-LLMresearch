# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 284
# filename        : gen_0284_gemini_04.py
# timestamp       : 2026-04-06T10:29:05Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 378
# tokens_output   : 1082
# tokens_total    : 1460
# cost_usd        : 0.000471
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_SYMBOLS = ["X", "O"]


def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(COLS)] for _ in range(ROWS)]
    return board


def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')
    print("  " + "   ".join(chr(ord('A') + i) for i in range(COLS)))
    for row in board:
        print("+---" * COLS + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * COLS + "+")


def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        move = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not move.isalpha() or len(move) != 1 or move < 'A' or move > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue

        col = ord(move) - ord('A')
        if is_valid_move(board, col):
            return col
        else:
            print("Column is full. Please choose another column.")


def is_valid_move(board, col):
    """Checks if a move is valid."""
    return board[0][col] == " "


def drop_checker(board, col, player):
    """Drops the player's checker into the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = PLAYER_SYMBOLS[player]
            return


def check_win(board, player):
    """Checks if the player has won the game."""
    symbol = PLAYER_SYMBOLS[player]

    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == symbol and
                    board[row][col + 1] == symbol and
                    board[row][col + 2] == symbol and
                    board[row][col + 3] == symbol):
                return True

    # Check vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            if (board[row][col] == symbol and
                    board[row + 1][col] == symbol and
                    board[row + 2][col] == symbol and
                    board[row + 3][col] == symbol):
                return True

    # Check positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (board[row][col] == symbol and
                    board[row + 1][col + 1] == symbol and
                    board[row + 2][col + 2] == symbol and
                    board[row + 3][col + 3] == symbol):
                return True

    # Check negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (board[row][col] == symbol and
                    board[row - 1][col + 1] == symbol and
                    board[row - 2][col + 2] == symbol and
                    board[row - 3][col + 3] == symbol):
                return True

    return False


def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def play_game():
    """Plays a game of Connect 4."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)
    print_board(board)

    while True:
        col = get_player_move(board, current_player)
        drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player + 1} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = (current_player + 1) % PLAYERS


if __name__ == "__main__":
    play_game()
```