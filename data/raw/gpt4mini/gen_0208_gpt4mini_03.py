# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 208
# filename        : gen_0208_gpt4mini_03.py
# timestamp       : 2026-04-06T09:29:57Z
# model           : openai/gpt-4o-mini
# model_short     : gpt4mini
# style_index     : 3
# style_text      : Write with detailed inline comments explaining every section.
# tokens_input    : 387
# tokens_output   : 957
# tokens_total    : 1344
# cost_usd        : 0.000632
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

import os
import random

# Constants for the board dimensions and number of players
ROWS = 6
COLS = 7
PLAYERS = 2

# Initialize the game board with empty spaces
def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Function to print the board with column labels
def print_board(board):
    os.system('clear')  # Clear the screen before printing
    print("   A   B   C   D   E   F   G")  # Print column headers
    print("+---+---+---+---+---+---+---+")  # Top border of the board
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")  # Print each cell in the row
        print("\n+---+---+---+---+---+---+---+")  # Border for the row

# Function to check if the move is valid
def is_valid_move(board, col):
    return board[0][col] == ' '

# Function to drop the checker in the selected column
def drop_checker(board, col, checker):
    for row in reversed(range(ROWS)):
        if board[row][col] == ' ':
            board[row][col] = checker
            return row  # Return the row where the checker was placed
    return -1  # Return -1 if the column is full (should not happen with validation)

# Function to check for a win
def check_win(board, player):
    checker = player  # The current player's checker
    # Check horizontal, vertical, and diagonal win conditions
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == checker:
                # Check horizontal
                if col + 3 < COLS and all(board[row][col + i] == checker for i in range(4)):
                    return True
                # Check vertical
                if row + 3 < ROWS and all(board[row + i][col] == checker for i in range(4)):
                    return True
                # Check diagonal (down-right)
                if row + 3 < ROWS and col + 3 < COLS and all(board[row + i][col + i] == checker for i in range(4)):
                    return True
                # Check diagonal (down-left)
                if row + 3 < ROWS and col - 3 >= 0 and all(board[row + i][col - i] == checker for i in range(4)):
                    return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(board[0][col] != ' ' for col in range(COLS))

# Main game function
def play_game():
    board = create_board()  # Create the game board
    players = ['X', 'O']  # Players
    current_player_index = random.randint(0, 1)  # Randomly select first player

    while True:
        print_board(board)  # Print the current state of the board
        current_player = players[current_player_index]  # Get the current player
        move = input(f"Player {current_player}, choose a column (A-G): ").upper()  # Player input

        # Validate input
        if move in 'ABCDEFG':
            col = ord(move) - ord('A')  # Convert column letter to index
            if is_valid_move(board, col):
                drop_checker(board, col, current_player)  # Drop the checker
                if check_win(board, current_player):  # Check if this move wins
                    print_board(board)  # Print the board one last time
                    print(f"Player {current_player} won!")  # Announce the winner
                    break  # End the game
                if check_draw(board):  # Check for a draw
                    print_board(board)  # Print the board one last time
                    print("The game is a draw!")  # Announce draw
                    break  # End the game
                current_player_index = (current_player_index + 1) % PLAYERS  # Switch players
            else:
                print("Column is full, choose another column.")  # Inform player
        else:
            print("Invalid input. Please choose a letter from A to G.")  # Inform player

# Start the game
if __name__ == "__main__":
    play_game()  # Run the game function