# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 230
# filename        : gen_0230_gemini_10.py
# timestamp       : 2026-04-06T10:21:01Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 10
# style_text      : Write with a modular structure, breaking everything into small functions.
# tokens_input    : 378
# tokens_output   : 1109
# tokens_total    : 1487
# cost_usd        : 0.000481
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
#   Write with a modular structure, breaking everything into small functions.
# ====================================================================

```python
import os
import random

ROWS = 6
COLS = 7
PLAYERS = 2

def create_board():
    """Creates a 2D board for Connect 4."""
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for i in range(ROWS):
        print("+---+---+---+---+---+---+---+")
        print("|", end="")
        for j in range(COLS):
            print(" " + board[i][j] + " |", end="")
        print()
    print("+---+---+---+---+---+---+---+")

def get_player_move(board, player):
    """Gets a valid column choice from the player."""
    while True:
        column = input(f"Player {player}, choose a column (A-G): ").upper()
        if not column.isalpha() or len(column) != 1:
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        column_index = ord(column) - ord('A')
        if 0 <= column_index < COLS:
            if board[0][column_index] == ' ':
                return column_index
            else:
                print("That column is full. Please choose another.")
        else:
            print("Invalid column. Please choose a column between A and G.")

def drop_checker(board, column, player):
    """Drops the player's checker into the specified column."""
    for i in range(ROWS - 1, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return i  # Return the row where the checker was placed

def check_win(board, row, col, player):
    """Checks for a win in horizontal, vertical, and diagonal directions."""
    # Horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Vertical
    count = 0
    for i in range(ROWS):
        if board[i][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Diagonal (top-left to bottom-right)
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

    # Diagonal (top-right to bottom-left)
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
    """Checks if the board is full, indicating a draw."""
    for i in range(COLS):
        if board[0][i] == ' ':
            return False  # There's still an empty space
    return True  # The board is full

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1 = "X"
    player2 = "O"
    players = [player1, player2]
    current_player = random.choice(players)
    game_over = False

    print_board(board)  # Initial board print

    while not game_over:
        column = get_player_move(board, current_player)
        row = drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, row, column, current_player):
            print(f"Player {current_player} won!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```