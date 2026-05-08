# ====================================================================
# CAPSTONE RESEARCH PIPELINE — PROVENANCE RECORD
# ====================================================================
# generation_id  : 431
# filename        : gen_0431_opus_04.py
# timestamp       : 2026-05-07T22:33:12Z
# model           : anthropic/claude-opus-4.5
# model_short     : opus
# style_index     : 4
# style_text      : Write in a professional style following PEP 8 conventions strictly.
# tokens_input    : 421
# tokens_output   : 1355
# tokens_total    : 1776
# cost_usd        : 0.107940
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
#   Write in a professional style following PEP 8 conventions strictly.
# ====================================================================

import os
import random

ROWS = 6
COLS = 7
NUM_PLAYERS = 2


def create_board():
    """Create and return an empty game board."""
    board = []
    for _ in range(ROWS):
        row = []
        for _ in range(COLS):
            row.append(" ")
        board.append(row)
    return board


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear')


def print_board(board):
    """Print the game board with column labels."""
    clear_screen()
    
    header = "   "
    for i in range(COLS):
        header += chr(ord('A') + i) + "   "
    print(header)
    
    print("+" + "---+" * COLS)
    
    for row in range(ROWS):
        line = "|"
        for col in range(COLS):
            line += " " + board[row][col] + " |"
        print(line)
        print("+" + "---+" * COLS)


def get_column_input(player, board):
    """Get and validate column input from the player."""
    while True:
        user_input = input(f"Player {player}, choose a column (A-G): ")
        
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter A-G.")
            continue
        
        user_input = user_input.upper()
        
        if user_input < 'A' or user_input > 'G':
            print("Invalid input. Please enter a letter between A and G.")
            continue
        
        col = ord(user_input) - ord('A')
        
        if board[0][col] != " ":
            print("That column is full. Please choose another column.")
            continue
        
        return col


def drop_checker(board, col, player):
    """Drop a checker in the specified column and return the row."""
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return row
    return -1


def check_win(board, row, col, player):
    """Check if the current move results in a win."""
    if check_horizontal(board, row, player):
        return True
    if check_vertical(board, col, player):
        return True
    if check_diagonal(board, row, col, player):
        return True
    return False


def check_horizontal(board, row, player):
    """Check for 4 in a row horizontally."""
    count = 0
    for col in range(COLS):
        if board[row][col] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    return False


def check_vertical(board, col, player):
    """Check for 4 in a row vertically."""
    count = 0
    for row in range(ROWS):
        if board[row][col] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
    return False


def check_diagonal(board, row, col, player):
    """Check for 4 in a row diagonally."""
    count = 0
    start_row = row - min(row, col)
    start_col = col - min(row, col)
    r, c = start_row, start_col
    while r < ROWS and c < COLS:
        if board[r][c] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
        r += 1
        c += 1
    
    count = 0
    start_row = row - min(row, COLS - 1 - col)
    start_col = col + min(row, COLS - 1 - col)
    r, c = start_row, start_col
    while r < ROWS and c >= 0:
        if board[r][c] == player:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0
        r += 1
        c -= 1
    
    return False


def is_board_full(board):
    """Check if the board is completely full."""
    for col in range(COLS):
        if board[0][col] == " ":
            return False
    return True


def main():
    """Main game loop."""
    board = create_board()
    players = ["X", "O"]
    current_player_index = random.randint(0, NUM_PLAYERS - 1)
    
    print_board(board)
    
    while True:
        current_player = players[current_player_index]
        
        col = get_column_input(current_player, board)
        row = drop_checker(board, col, current_player)
        
        print_board(board)
        
        if check_win(board, row, col, current_player):
            print(f"{current_player} won!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player_index = (current_player_index + 1) % NUM_PLAYERS


if __name__ == "__main__":
    main()