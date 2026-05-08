# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 206
# filename        : gen_0206_gemini_01.py
# timestamp       : 2026-04-06T10:15:49Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 1
# style_text      : Write in a simple, beginner-friendly style with clear variable names.
# tokens_input    : 380
# tokens_output   : 1149
# tokens_total    : 1529
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
#   Write in a simple, beginner-friendly style with clear variable names.
# ====================================================================

```python
import os
import random

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2
PLAYER_ONE = "X"
PLAYER_TWO = "O"

def create_board():
    """Creates an empty Connect 4 board."""
    board = [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

def print_board(board):
    """Prints the Connect 4 board with column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")
    for row in board:
        print("+---" * BOARD_WIDTH + "+")
        print("| " + " | ".join(row) + " |")
    print("+---" * BOARD_WIDTH + "+")

def get_player_move(board, player):
    """Gets a valid move from the player."""
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()
        
        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter from A to G.")
            continue

        try:
            column_index = ord(column_input) - ord('A')
            if not (0 <= column_index < BOARD_WIDTH):
                print("Invalid input. Column must be between A and G.")
                continue
        except:
            print("Invalid input. Please enter a letter from A to G.")
            continue
        

        if board[0][column_index] != " ":
            print("Column is full. Please choose another column.")
            continue

        return column_index

def drop_checker(board, column, player):
    """Drops the checker into the lowest available row in the column."""
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == " ":
            board[row][column] = player
            return

def check_win(board, player):
    """Checks if the player has won the game."""
    # Check horizontal
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player):
                return True

    # Check vertical
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH):
            if (board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player):
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player):
                return True

    # Check diagonal (top-right to bottom-left)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(3, BOARD_WIDTH):
            if (board[row][col] == player and
                board[row+1][col-1] == player and
                board[row+2][col-2] == player and
                board[row+3][col-3] == player):
                return True

    return False

def check_draw(board):
    """Checks if the board is full (draw)."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # Empty cell found, not a draw
    return True  # No empty cells, it's a draw

def main():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1 = PLAYER_ONE
    player2 = PLAYER_TWO
    current_player = random.choice([player1, player2])

    print_board(board)

    while True:
        column = get_player_move(board, current_player)
        drop_checker(board, column, current_player)
        print_board(board)

        if check_win(board, current_player):
            print(f"{current_player} won!")
            break

        if check_draw(board):
            print("Draw!")
            break

        # Switch to the other player
        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
```