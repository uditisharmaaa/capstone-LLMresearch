# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 272
# filename        : gen_0272_gemini_07.py
# timestamp       : 2026-04-06T10:28:15Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 7
# style_text      : Write in a teaching style, as if explaining to someone learning Python.
# tokens_input    : 380
# tokens_output   : 1310
# tokens_total    : 1690
# cost_usd        : 0.000562
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
#   Write in a teaching style, as if explaining to someone learning Python.
# ====================================================================

```python
import os
import random

# Define constants for board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

# Define player symbols
PLAYER_SYMBOLS = ["X", "O"]

def create_board():
    """Creates a 2D board represented as a list of lists, initialized with spaces."""
    board = []
    for _ in range(ROWS):
        board.append([" "] * COLS)
    return board

def print_board(board):
    """Prints the Connect 4 board to the console, including column labels."""
    os.system('clear')  # Clear the screen
    print("  A   B   C   D   E   F   G")  # Column labels
    for row in board:
        row_string = "+" + "+".join(["---"] * COLS) + "+"
        print(row_string)
        print("| " + " | ".join(row) + " |")
    row_string = "+" + "+".join(["---"] * COLS) + "+"
    print(row_string)

def get_player_move(board, player_symbol):
    """Gets a valid column choice from the player."""
    while True:
        column_letter = input(f"Player {player_symbol}, enter column (A-G): ").upper()
        
        if not column_letter.isalpha() or len(column_letter) != 1:
             print("Invalid input. Please enter a letter between A and G.")
             continue

        try:
            column = ord(column_letter) - ord('A')  # Convert letter to column index (0-6)
            if 0 <= column < COLS:
                if board[0][column] == " ":  # Check if the column is not full
                    return column
                else:
                    print("That column is full. Please choose another.")
            else:
                print("Invalid column. Please enter a letter between A and G.")
        except ValueError:
            print("Invalid input. Please enter a letter between A and G.")

def drop_checker(board, column, player_symbol):
    """Drops the player's checker into the specified column."""
    for row in range(ROWS - 1, -1, -1):  # Iterate from the bottom row upwards
        if board[row][column] == " ":
            board[row][column] = player_symbol
            return row  # Return the row where the checker was placed

def check_win(board, row, col, player_symbol):
    """Checks for a win (4 in a row) horizontally, vertically, and diagonally."""

    # Check horizontal
    count = 0
    for c in range(COLS):
        if board[row][c] == player_symbol:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(ROWS):
        if board[r][col] == player_symbol:
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
            if board[r][c] == player_symbol:
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
            if board[r][c] == player_symbol:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

    return False

def is_board_full(board):
    """Checks if the board is full (draw condition)."""
    for row in board:
        if " " in row:
            return False  # If there's an empty space, the board is not full
    return True  # If no empty spaces are found, the board is full

def play_connect_4():
    """Main function to run the Connect 4 game."""
    board = create_board()
    player1_symbol = PLAYER_SYMBOLS[0]
    player2_symbol = PLAYER_SYMBOLS[1]
    
    # Randomly choose the starting player
    current_player = random.randint(0, 1)  # 0 for player 1, 1 for player 2

    print_board(board)
    
    game_over = False
    while not game_over:
        player_symbol = PLAYER_SYMBOLS[current_player]
        
        column = get_player_move(board, player_symbol)
        row = drop_checker(board, column, player_symbol)
        
        print_board(board)
        
        if check_win(board, row, column, player_symbol):
            print(f"Player {player_symbol} won!")
            game_over = True
        elif is_board_full(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch to the next player
            current_player = (current_player + 1) % PLAYERS

# Start the game
play_connect_4()
```