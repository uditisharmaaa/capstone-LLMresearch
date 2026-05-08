# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 266
# filename        : gen_0266_gemini_01.py
# timestamp       : 2026-04-06T10:27:50Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 380
# tokens_output   : 1392
# tokens_total    : 1772
# cost_usd        : 0.000595
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

```python
import os
import random

NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    """Creates a 2D board with spaces."""
    board = []
    for _ in range(NUM_ROWS):
        row = [" "] * NUM_COLS
        board.append(row)
    return board

def print_board(board):
    """Prints the board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_input:
            print("Invalid input. Please enter a column letter (A-G).")
            continue

        if len(column_input) != 1 or column_input < "A" or column_input > "G":
            print("Invalid input. Please enter a column letter (A-G).")
            continue

        column_index = ord(column_input) - ord("A")

        if is_column_full(board, column_index):
            print("That column is full. Choose another.")
            continue

        return column_index

def is_column_full(board, column_index):
    """Checks if a column is full."""
    return board[0][column_index] != " "

def drop_checker(board, column_index, player):
    """Drops the checker to the lowest available row."""
    for row_index in range(NUM_ROWS - 1, -1, -1):
        if board[row_index][column_index] == " ":
            board[row_index][column_index] = player
            return row_index

def check_win(board, row_index, column_index, player):
    """Checks for a win in all directions."""
    return (check_horizontal_win(board, row_index, player) or
            check_vertical_win(board, column_index, player) or
            check_diagonal_win(board, row_index, column_index, player))

def check_horizontal_win(board, row_index, player):
    """Checks for a horizontal win."""
    count = 0
    for col_index in range(NUM_COLS):
        if board[row_index][col_index] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_vertical_win(board, column_index, player):
    """Checks for a vertical win."""
    count = 0
    for row_index in range(NUM_ROWS):
        if board[row_index][column_index] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    return False

def check_diagonal_win(board, row_index, column_index, player):
    """Checks for a diagonal win (both directions)."""
    return (check_positive_diagonal_win(board, row_index, column_index, player) or
            check_negative_diagonal_win(board, row_index, column_index, player))

def check_positive_diagonal_win(board, row_index, column_index, player):
    """Checks for a positive diagonal win (top-left to bottom-right)."""
    count = 0
    for i in range(-3, 4):
        r = row_index + i
        c = column_index + i
        if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def check_negative_diagonal_win(board, row_index, column_index, player):
    """Checks for a negative diagonal win (top-right to bottom-left)."""
    count = 0
    for i in range(-3, 4):
        r = row_index + i
        c = column_index - i
        if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS:
            if board[r][c] == player:
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
    player1 = PLAYER_X
    player2 = PLAYER_O
    current_player = random.choice([player1, player2])

    print_board(board)

    while True:
        column_index = get_player_move(board, current_player)
        row_index = drop_checker(board, column_index, current_player)
        print_board(board)

        if check_win(board, row_index, column_index, current_player):
            print(f"Player {current_player} won!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```