# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 268
# filename        : gen_0268_gemini_03.py
# timestamp       : 2026-04-06T10:27:58Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1177
# tokens_total    : 1552
# cost_usd        : 0.000508
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

# Define global constants for board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

# Function to create the Connect 4 board
def create_board():
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board

# Function to print the board with column labels
def print_board(board):
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")  # Print column labels
    for i in range(ROWS):
        print("+---+---+---+---+---+---+---+")  # Print row separators
        print("| " + " | ".join(board[i]) + " |")  # Print board contents
    print("+---+---+---+---+---+---+---+")

# Function to check if a column is full
def is_column_full(board, col):
    return board[0][col] != ' '

# Function to drop a checker into a column
def drop_checker(board, col, player):
    for i in range(ROWS - 1, -1, -1):
        if board[i][col] == ' ':
            board[i][col] = player
            return i  # Return the row where the checker was dropped
    return -1  # Return -1 if the column is full (shouldn't happen if input is validated)

# Function to check for a win
def check_win(board, player, row, col):
    # Check horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for i in range(ROWS):
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

# Function to check for a draw
def check_draw(board):
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == ' ':
                return False  # If there's an empty space, it's not a draw
    return True  # If no empty spaces, it's a draw

# Function to get player input
def get_player_move(board):
    while True:
        move = input("Enter column (A-G): ").upper()
        if len(move) != 1 or not 'A' <= move <= 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue

        col = ord(move) - ord('A')  # Convert letter to column index (0-6)
        if is_column_full(board, col):
            print("Column is full. Please choose another column.")
            continue

        return col  # Return the valid column index

# Main game function
def play_connect_4():
    board = create_board()
    players = ['X', 'O']
    current_player = random.choice(players)  # Randomly choose the first player
    print_board(board)  # Print the initial board

    while True:
        print(f"Player {current_player}'s turn.")
        col = get_player_move(board)  # Get a valid move from the player
        row = drop_checker(board, col, current_player)  # Drop the checker

        print_board(board)  # Print the updated board

        if check_win(board, current_player, row, col):  # Check for a win
            print(f"Player {current_player} won!")
            break

        if check_draw(board):  # Check for a draw
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = players[1] if current_player == players[0] else players[0]

# Start the game
if __name__ == "__main__":
    play_connect_4()
```