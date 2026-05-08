# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 123
# filename        : gen_0123_gemini_08.py
# timestamp       : 2026-04-06T09:57:32Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1071
# tokens_total    : 1447
# cost_usd        : 0.000466
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
PLAYER_CHARS = ["X", "O"]

def create_board():
    """Creates a 2D board initialized with spaces."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the board with column labels and formatting."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player_char):
    """Gets a valid column choice from the player."""
    while True:
        column_choice = input(f"Player {player_char}, choose a column (A-G): ").upper()
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
            print("Invalid column choice. Please enter a letter between A and G.")

def drop_checker(board, column, player_char):
    """Drops the checker into the lowest available row in the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player_char
            return row

def check_win(board, row, col, player_char):
    """Checks for a win in all directions."""
    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_char:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r, c = row + i, col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r, c = row + i, col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player_char:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player_turn = random.randint(0, PLAYERS - 1)  # Randomly choose starting player

    while True:
        print_board(board)
        player_char = PLAYER_CHARS[player_turn]
        column = get_player_move(board, player_char)
        row = drop_checker(board, column, player_char)

        if check_win(board, row, column, player_char):
            print_board(board)
            print(f"Player {player_char} won!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        player_turn = (player_turn + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```