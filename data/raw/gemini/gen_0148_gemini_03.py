# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 148
# filename        : gen_0148_gemini_03.py
# timestamp       : 2026-04-06T10:05:11Z
# model           : google/gemini-2.0-flash-001
# model_short     : gemini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 375
# tokens_output   : 1310
# tokens_total    : 1685
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
#   Write with detailed inline comments explaining every section.
# ====================================================================

```python
import os  # For clearing the screen
import random  # For choosing the first player

# Define global constants for board dimensions and number of players
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
NUM_PLAYERS = 2

# Function to clear the screen
def clear_screen():
    os.system('clear')

# Function to initialize the Connect 4 board
def create_board():
    board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board

# Function to print the board with column labels
def print_board(board):
    print("  A   B   C   D   E   F   G")  # Column labels
    for i in range(BOARD_HEIGHT):
        row_string = "+"
        for j in range(BOARD_WIDTH):
            row_string += "---+"
        print(row_string) # Print top border of the row
        row = "|"
        for j in range(BOARD_WIDTH):
            row += " " + board[i][j] + " |"
        print(row)
    bottom_border = "+"
    for j in range(BOARD_WIDTH):
        bottom_border += "---+"
    print(bottom_border) # Print bottom border of the row

# Function to get player input for column choice
def get_player_move(player, board):
    while True:
        column_input = input(f"Player {player}, enter column (A-G): ").upper()  # Prompt player for input
        if not column_input.isalpha() or len(column_input) != 1:
            print("Invalid input. Please enter a letter from A to G.")
            continue
        column = ord(column_input) - ord('A')  # Convert letter to column index
        if 0 <= column < BOARD_WIDTH:
            if board[0][column] == ' ':  # Check if column is not full
                return column
            else:
                print("Column is full. Please choose another column.")
        else:
            print("Invalid column. Please choose a column from A to G.")

# Function to drop the checker into the chosen column
def drop_checker(board, column, player):
    for i in range(BOARD_HEIGHT - 1, -1, -1):  # Iterate from bottom row up
        if board[i][column] == ' ':
            board[i][column] = player
            return

# Function to check for a win
def check_win(board, player):
    # Check horizontal
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH - 3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True

    # Check vertical
    for i in range(BOARD_HEIGHT - 3):
        for j in range(BOARD_WIDTH):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for i in range(BOARD_HEIGHT - 3):
        for j in range(BOARD_WIDTH - 3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True

    # Check diagonal (top-right to bottom-left)
    for i in range(BOARD_HEIGHT - 3):
        for j in range(3, BOARD_WIDTH):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True

    return False

# Function to check for a draw
def check_draw(board):
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if board[i][j] == ' ':
                return False  # There are still empty spaces, so it's not a draw
    return True  # All spaces are filled, so it's a draw

# Main game function
def play_connect_4():
    board = create_board()  # Initialize the board
    players = ['X', 'O']  # Define player checkers
    current_player = random.choice(players)  # Randomly choose the first player
    game_over = False

    clear_screen()
    print_board(board)  # Print the initial board

    while not game_over:
        column = get_player_move(current_player, board)  # Get player input
        drop_checker(board, column, current_player)  # Drop the checker

        clear_screen()
        print_board(board)  # Print the updated board

        if check_win(board, current_player):  # Check for a win
            print(f"Player {current_player} won!")
            game_over = True
        elif check_draw(board):  # Check for a draw
            print("It's a draw!")
            game_over = True
        else:  # Switch to the next player
            current_player = players[(players.index(current_player) + 1) % NUM_PLAYERS]

# Start the game
if __name__ == "__main__":
    play_connect_4()
```