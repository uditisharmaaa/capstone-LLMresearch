# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 143
# filename        : gen_0143_gemini_13.py
# timestamp       : 2026-04-06T10:04:16Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1254
# tokens_total    : 1628
# cost_usd        : 0.000539
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

# Global constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_MARKS = ["X", "O"]

def create_board():
    """Creates an empty Connect 4 board."""
    board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

def print_board(board):
    """Prints the Connect 4 board to the console."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for i in range(BOARD_HEIGHT):
        print("+---" * BOARD_WIDTH + "+")
        row_str = "|"
        for j in range(BOARD_WIDTH):
            row_str += " " + board[i][j] + " |"
        print(row_str)
    print("+---" * BOARD_WIDTH + "+")

def get_player_move(board, player):
    """Gets a valid move from the current player."""
    while True:
        column_str = input(f"Player {player + 1}, enter column (A-G): ").upper()
        if not column_str.isalpha() or len(column_str) != 1:
            print("Invalid input. Please enter a letter from A to G.")
            continue

        column_index = ord(column_str) - ord('A')
        if column_index < 0 or column_index >= BOARD_WIDTH:
            print("Invalid column. Please enter a letter from A to G.")
            continue

        if board[0][column_index] != ' ':
            print("Column is full. Please choose another column.")
            continue

        return column_index

def drop_checker(board, column, player_mark):
    """Drops the player's checker into the specified column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player_mark
            return

def check_win(board, player_mark):
    """Checks if the current player has won the game."""
    # Check horizontal
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player_mark and
                board[row][col + 1] == player_mark and
                board[row][col + 2] == player_mark and
                board[row][col + 3] == player_mark):
                return True

    # Check vertical
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH):
            if (board[row][col] == player_mark and
                board[row + 1][col] == player_mark and
                board[row + 2][col] == player_mark and
                board[row + 3][col] == player_mark):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player_mark and
                board[row + 1][col + 1] == player_mark and
                board[row + 2][col + 2] == player_mark and
                board[row + 3][col + 3] == player_mark):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(3, BOARD_WIDTH):
            if (board[row][col] == player_mark and
                board[row + 1][col - 1] == player_mark and
                board[row + 2][col - 2] == player_mark and
                board[row + 3][col - 3] == player_mark):
                return True

    return False

def check_draw(board):
    """Checks if the board is full, resulting in a draw."""
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            if board[row][col] == ' ':
                return False  # There's an empty space, so it's not a draw
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, NUM_PLAYERS - 1)  # Randomly choose starting player
    game_over = False

    print_board(board)  # Print initial board

    while not game_over:
        column = get_player_move(board, current_player)
        drop_checker(board, column, PLAYER_MARKS[current_player])
        print_board(board)

        if check_win(board, PLAYER_MARKS[current_player]):
            print(f"Player {current_player + 1} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % NUM_PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```