# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 243
# filename        : gen_0243_gemini_08.py
# timestamp       : 2026-04-06T10:24:33Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1178
# tokens_total    : 1554
# cost_usd        : 0.000509
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
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_MARKS = ["X", "O"]

def create_board():
    """Creates a 2D list representing the Connect 4 board."""
    board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

def print_board(board):
    """Prints the Connect 4 board to the console."""
    os.system('clear')
    print("  " + "   ".join([chr(ord('A') + i) for i in range(BOARD_WIDTH)]))
    for row in board:
        print("+---" * BOARD_WIDTH + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * BOARD_WIDTH + "+")

def get_player_move(player_mark, board):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player_mark}, enter column (A-G): ").upper()

        if not column_input:
            print("Invalid input. Please enter a column letter (A-G).")
            continue

        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a single letter (A-G).")
            continue

        column_index = ord(column_input) - ord('A')

        if not (0 <= column_index < BOARD_WIDTH):
            print("Invalid column. Please enter a column between A and G.")
            continue

        if board[0][column_index] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column_index


def drop_checker(board, column_index, player_mark):
    """Drops the player's checker into the specified column."""
    for row_index in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row_index][column_index] == " ":
            board[row_index][column_index] = player_mark
            return row_index

def check_win(board, row_index, column_index, player_mark):
    """Checks if the player has won the game."""

    # Check horizontal
    count = 0
    for col in range(BOARD_WIDTH):
        if board[row_index][col] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for row in range(BOARD_HEIGHT):
        if board[row][column_index] == player_mark:
            count += 1
            if count == 4:
                return True
        else:
            count = 0


    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        row = row_index + i
        col = column_index + i
        if 0 <= row < BOARD_HEIGHT and 0 <= col < BOARD_WIDTH:
            if board[row][col] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        row = row_index + i
        col = column_index - i
        if 0 <= row < BOARD_HEIGHT and 0 <= col < BOARD_WIDTH:
            if board[row][col] == player_mark:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)
    game_over = False

    print_board(board)

    while not game_over:
        player_mark = PLAYER_MARKS[current_player]
        column_index = get_player_move(player_mark, board)
        row_index = drop_checker(board, column_index, player_mark)

        print_board(board)

        if check_win(board, row_index, column_index, player_mark):
            print(f"Player {player_mark} won!")
            game_over = True
        elif is_board_full(board):
            print("Draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS

if __name__ == "__main__":
    main()
```