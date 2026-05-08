# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 168
# filename        : gen_0168_gemini_08.py
# timestamp       : 2026-04-06T10:09:38Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 8
# style_text      : Write with a focus on code readability over brevity.
# tokens_input    : 376
# tokens_output   : 1129
# tokens_total    : 1505
# cost_usd        : 0.000489
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
NUM_ROWS = 6
NUM_COLS = 7
NUM_PLAYERS = 2
PLAYER_1 = "X"
PLAYER_2 = "O"

def create_board():
    """Creates a 2D board with empty spaces."""
    board = []
    for _ in range(NUM_ROWS):
        row = [" "] * NUM_COLS
        board.append(row)
    return board

def print_board(board):
    """Prints the board with column labels."""
    os.system('clear')
    print("  A   B   C   D   E   F   G")
    for i in range(NUM_ROWS):
        print("+---+---+---+---+---+---+---+")
        row_str = "|"
        for j in range(NUM_COLS):
            row_str += " " + board[i][j] + " |"
        print(row_str)
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        column_str = input(f"Player {player}, enter column (A-G): ").upper()
        if not column_str.isalpha() or len(column_str) != 1:
            print("Invalid input. Please enter a letter A-G.")
            continue

        column = ord(column_str) - ord('A')
        if not (0 <= column < NUM_COLS):
            print("Invalid column. Please enter a letter A-G.")
            continue

        if board[0][column] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column

def drop_checker(board, column, player):
    """Drops the checker to the lowest available row in the chosen column."""
    for row in range(NUM_ROWS - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return row

def check_win(board, row, col, player):
    """Checks for a win in all directions."""
    # Check horizontal
    count = 0
    for j in range(NUM_COLS):
        if board[row][j] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for i in range(NUM_ROWS):
        if board[i][col] == player:
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
        if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS:
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
        if 0 <= r < NUM_ROWS and 0 <= c < NUM_COLS:
            if board[r][c] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def check_draw(board):
    """Checks if the board is full (draw)."""
    for col in range(NUM_COLS):
        if board[0][col] == " ":
            return False
    return True

def play_game():
    """Main function to play the Connect 4 game."""
    board = create_board()
    player1 = PLAYER_1
    player2 = PLAYER_2
    players = [player1, player2]

    # Randomly choose which player goes first
    current_player = random.choice(players)

    print_board(board)

    while True:
        column = get_player_move(board, current_player)
        row = drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, row, column, current_player):
            print(f"Player {current_player} won!")
            break

        if check_draw(board):
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    play_game()
```