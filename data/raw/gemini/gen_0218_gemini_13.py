# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 218
# filename        : gen_0218_gemini_13.py
# timestamp       : 2026-04-06T10:18:38Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 13
# style_text      : Write prioritizing correctness and clarity over elegance.
# tokens_input    : 374
# tokens_output   : 1075
# tokens_total    : 1449
# cost_usd        : 0.000467
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
PLAYER_CHARS = ["X", "O"]

def create_board():
    """Creates a 2D list representing the Connect 4 board."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets valid player input for a column."""
    while True:
        move = input(f"Player {PLAYER_CHARS[player]}, enter a column (A-G): ").upper()
        if not move.isalpha() or len(move) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        col = ord(move) - ord('A')
        if col < 0 or col >= COLS:
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][col] != " ":
            print("Column is full. Please choose a different column.")
            continue

        return col

def drop_checker(board, col, player):
    """Drops the player's checker into the specified column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = PLAYER_CHARS[player]
            return row

def check_win(board, row, col, player):
    """Checks for a win horizontally, vertically, and diagonally."""
    checker = PLAYER_CHARS[player]

    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == checker:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check diagonal (top-left to bottom-right)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col + i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == checker:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    # Check diagonal (top-right to bottom-left)
    count = 0
    for i in range(-3, 4):
        r = row + i
        c = col - i
        if 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == checker:
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

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    current_player = random.randint(0, PLAYERS - 1)  # Randomly choose starting player
    game_over = False

    print_board(board)

    while not game_over:
        col = get_player_move(board, current_player)
        row = drop_checker(board, col, current_player)
        print_board(board)

        if check_win(board, row, col, current_player):
            print(f"Player {PLAYER_CHARS[current_player]} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = (current_player + 1) % PLAYERS  # Switch to the next player

if __name__ == "__main__":
    main()
```