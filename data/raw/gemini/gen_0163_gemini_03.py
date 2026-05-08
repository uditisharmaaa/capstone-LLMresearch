# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 163
# filename        : gen_0163_gemini_03.py
# timestamp       : 2026-04-06T10:08:33Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1242
# tokens_total    : 1617
# cost_usd        : 0.000534
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
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)] # Create a 2D list (ROWS x COLS) filled with spaces
    return board

# Function to print the board
def print_board(board):
    os.system('clear') # Clear the screen before printing

    # Print column labels
    print("  A   B   C   D   E   F   G")
    
    # Print the board with separators
    for row in board:
        print("+---+---+---+---+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+---+---+---+---+")

# Function to check if a column is full
def is_column_full(board, col):
    return board[0][col] != ' ' # Check if the top row of the column is occupied

# Function to drop a checker into the board
def drop_checker(board, row, col, checker):
    board[row][col] = checker # Place the checker at the specified row and column

# Function to get the lowest available row in a column
def get_next_open_row(board, col):
    for row in range(ROWS - 1, -1, -1): # Iterate from the bottom row upwards
        if board[row][col] == ' ':
            return row # Return the first empty row found
    return -1 # Should not happen due to input validation

# Function to check for a win
def check_win(board, checker):
    # Check horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row][col+1] == checker and board[row][col+2] == checker and board[row][col+3] == checker:
                return True

    # Check vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == checker and board[row+1][col] == checker and board[row+2][col] == checker and board[row+3][col] == checker:
                return True

    # Check positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row+1][col+1] == checker and board[row+2][col+2] == checker and board[row+3][col+3] == checker:
                return True

    # Check negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == checker and board[row-1][col+1] == checker and board[row-2][col+2] == checker and board[row-3][col+3] == checker:
                return True

    return False

# Function to handle player input and validation
def get_player_move(board, player):
    while True:
        try:
            column_input = input(f"Player {player + 1}, enter column (A-G): ").upper() # Prompt for input
            if not column_input.isalpha() or len(column_input) != 1:
                print("Invalid input. Please enter a letter from A to G.")
                continue
            
            col = ord(column_input) - ord('A') # Convert letter to column index
            if col < 0 or col >= COLS:
                print("Invalid column. Please choose a column between A and G.")
                continue

            if is_column_full(board, col):
                print("That column is full. Please choose another column.")
                continue
            
            return col # Return the valid column index
        except ValueError:
            print("Invalid input. Please enter a letter from A to G.")

# Main game function
def play_game():
    board = create_board() # Create the game board
    print_board(board) # Print the initial board

    # Randomly select the starting player
    turn = random.randint(0, PLAYERS - 1)
    checkers = ['X', 'O'] # Define checkers for players

    game_over = False
    turn_count = 0

    while not game_over:
        # Get player move
        col = get_player_move(board, turn)

        # Drop the checker
        row = get_next_open_row(board, col)
        drop_checker(board, row, col, checkers[turn])
        print_board(board)

        # Check for win
        if check_win(board, checkers[turn]):
            print(f"Player {turn + 1} won!")
            game_over = True
        else:
            turn_count += 1
            if turn_count == ROWS * COLS:
                print("It's a draw!")
                game_over = True
            else:
                # Switch to the next player
                turn = (turn + 1) % PLAYERS

# Start the game
if __name__ == "__main__":
    play_game()
```