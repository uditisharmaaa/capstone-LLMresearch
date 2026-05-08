# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 210
# filename        : gen_0210_gemini_05.py
# timestamp       : 2026-04-06T10:16:41Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 5
# style_text      : Write with descriptive function names and minimal comments.
# tokens_input    : 375
# tokens_output   : 1150
# tokens_total    : 1525
# cost_usd        : 0.000498
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
#   Write with descriptive function names and minimal comments.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2
PLAYER_1 = "X"
PLAYER_2 = "O"


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
        print("| " + " | ".join(board[i]) + " |")
    print("+---+---+---+---+---+---+---+")


def get_player_move(board, player):
    """Gets a valid column choice from the player."""
    while True:
        column_input = input(f"Player {player}, choose a column (A-G): ").upper()
        if len(column_input) != 1 or column_input < 'A' or column_input > 'G':
            print("Invalid input. Please enter a letter from A to G.")
            continue

        try:
            column = ord(column_input) - ord('A')
            if not is_valid_location(board, column):
                print("That column is full. Please choose another.")
                continue
            return column
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")


def is_valid_location(board, column):
    """Checks if a column has available space."""
    return board[0][column] == " "


def drop_checker(board, row, column, player):
    """Drops the player's checker into the specified location."""
    board[row][column] = player


def get_next_open_row(board, column):
    """Gets the lowest available row in the specified column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            return row


def winning_move(board, player):
    """Checks if the current move results in a win."""
    # Check horizontal
    for c in range(COLS - 3):
        for r in range(ROWS):
            if board[r][c] == player and board[r][c + 1] == player and board[r][c + 2] == player and board[r][c + 3] == player:
                return True

    # Check vertical
    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r + 1][c] == player and board[r + 2][c] == player and board[r + 3][c] == player:
                return True

    # Check positive diagonals
    for c in range(COLS - 3):
        for r in range(ROWS - 3):
            if board[r][c] == player and board[r + 1][c + 1] == player and board[r + 2][c + 2] == player and board[r + 3][c + 3] == player:
                return True

    # Check negative diagonals
    for c in range(COLS - 3):
        for r in range(3, ROWS):
            if board[r][c] == player and board[r - 1][c + 1] == player and board[r - 2][c + 2] == player and board[r - 3][c + 3] == player:
                return True

    return False


def is_board_full(board):
    """Checks if the board is completely full."""
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == " ":
                return False
    return True


def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    print_board(board)
    game_over = False
    turn = random.randint(0, PLAYERS - 1)  # Randomly choose first player

    while not game_over:
        if turn % PLAYERS == 0:
            player = PLAYER_1
        else:
            player = PLAYER_2

        column = get_player_move(board, player)
        row = get_next_open_row(board, column)
        drop_checker(board, row, column, player)
        print_board(board)

        if winning_move(board, player):
            print(f"{player} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True

        turn += 1


if __name__ == "__main__":
    main()
```