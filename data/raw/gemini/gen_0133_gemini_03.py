# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 133
# filename        : gen_0133_gemini_03.py
# timestamp       : 2026-04-06T09:59:58Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1131
# tokens_total    : 1506
# cost_usd        : 0.000490
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

```python
import os
import random

# Define constant global variables
ROWS = 6
COLS = 7
NUM_PLAYERS = 2
PLAYER1 = "X"
PLAYER2 = "O"

def create_board():
    """Creates a 2D board (list of lists) initialized with spaces."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the board with column labels and separators."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Asks the player for their move and validates the input."""
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(column_input) - ord('A')  # Convert letter to column index
        if not (0 <= column < COLS):
            print("Invalid column. Please choose a column between A and G.")
            continue

        if board[0][column] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column

def drop_checker(board, column, player):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return row

def check_win(board, row, col, player):
    """Checks for a win in all directions (horizontal, vertical, diagonal)."""

    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player:
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
            if board[r][c] == player:
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
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    """Checks if the board is full (draw)."""
    for row in board:
        if " " in row:
            return False  # There's an empty space, not a draw
    return True  # No empty spaces, it's a draw

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1 = PLAYER1
    player2 = PLAYER2
    players = [player1, player2]

    # Randomly choose which player goes first
    current_player = random.choice(players)

    print_board(board)  # Initial board display

    game_over = False
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
        else:
            # Switch to the other player
            current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```