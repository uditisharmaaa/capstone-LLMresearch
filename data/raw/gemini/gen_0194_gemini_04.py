# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 194
# filename        : gen_0194_gemini_04.py
# timestamp       : 2026-04-06T10:14:13Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 378
# tokens_output   : 1054
# tokens_total    : 1432
# cost_usd        : 0.000459
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
    for i in range(ROWS):
        print("+---" * COLS + "+")
        print("| " + " | ".join(board[i]) + " |")
    print("+---" * COLS + "+")


def get_player_move(player_symbol, board):
    """Gets and validates the player's move."""
    while True:
        move = input(f"Player {player_symbol}, enter column (A-G): ").upper()
        if not move.isalpha() or len(move) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(move) - ord('A')
        if not 0 <= column < COLS:
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][column] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column


def drop_checker(board, column, player_symbol):
    """Drops the checker into the chosen column."""
    for i in range(ROWS - 1, -1, -1):
        if board[i][column] == " ":
            board[i][column] = player_symbol
            return


def check_win(board, player_symbol):
    """Checks for a win in all directions."""
    # Check horizontal
    for i in range(ROWS):
        for j in range(COLS - 3):
            if (board[i][j] == board[i][j+1] == board[i][j+2] ==
                    board[i][j+3] == player_symbol):
                return True

    # Check vertical
    for i in range(ROWS - 3):
        for j in range(COLS):
            if (board[i][j] == board[i+1][j] == board[i+2][j] ==
                    board[i+3][j] == player_symbol):
                return True

    # Check positive diagonal
    for i in range(ROWS - 3):
        for j in range(COLS - 3):
            if (board[i][j] == board[i+1][j+1] == board[i+2][j+2] ==
                    board[i+3][j+3] == player_symbol):
                return True

    # Check negative diagonal
    for i in range(ROWS - 3):
        for j in range(3, COLS):
            if (board[i][j] == board[i+1][j-1] == board[i+2][j-2] ==
                    board[i+3][j-3] == player_symbol):
                return True

    return False


def check_draw(board):
    """Checks if the board is full, indicating a draw."""
    for i in range(COLS):
        if board[0][i] == " ":
            return False
    return True


def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player_turn = random.randint(0, PLAYERS - 1)
    current_player = PLAYER_SYMBOLS[player_turn]
    game_over = False

    print_board(board)

    while not game_over:
        column = get_player_move(current_player, board)
        drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            player_turn = (player_turn + 1) % PLAYERS
            current_player = PLAYER_SYMBOLS[player_turn]


if __name__ == "__main__":
    main()
```