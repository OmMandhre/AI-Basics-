# game playing agent using minimax algorithm (tic-tac-toe)
import math

# Initialize the board
board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(b, player):
    # Winning combinations: rows, columns, diagonals
    win_conds = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),  # Rows
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),  # Columns
        (0, 4, 8),
        (2, 4, 6)   # Diagonals
    ]

    for cond in win_conds:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True

    return False


def is_board_full(b):
    return " " not in b


def get_available_moves(b):
    return [i for i, spot in enumerate(b) if spot == " "]


# Minimax Algorithm Implementation
def minimax(b, depth, is_maximizing):
    # Base cases: check for terminal states
    if check_winner(b, "O"):  # AI wins
        return 10 - depth

    if check_winner(b, "X"):  # Human wins
        return depth - 10

    if is_board_full(b):  # Tie
        return 0

    if is_maximizing:
        max_eval = -math.inf

        for move in get_available_moves(b):
            b[move] = "O"

            eval = minimax(b, depth + 1, False)

            b[move] = " "

            max_eval = max(max_eval, eval)

        return max_eval

    else:
        min_eval = math.inf

        for move in get_available_moves(b):
            b[move] = "X"

            eval = minimax(b, depth + 1, True)

            b[move] = " "

            min_eval = min(min_eval, eval)

        return min_eval


# Find the best move for the AI
def ai_move():
    best_val = -math.inf
    best_move = None

    for move in get_available_moves(board):
        board[move] = "O"

        move_val = minimax(board, 0, False)

        board[move] = " "

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move


# Main Game Loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and the AI is 'O'.")
    print("Board positions are numbered from 0 to 8 like this:")
    print(" 0 | 1 | 2 ")
    print("-----------")
    print(" 3 | 4 | 5 ")
    print("-----------")
    print(" 6 | 7 | 8 \n")

    while True:
        print_board()

        # Human Turn ('X')
        try:
            move = int(input("Enter your move (0-8): "))

            if move < 0 or move > 8:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            if board[move] != " ":
                print("Spot is already taken! Choose another.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            print_board()
            print("Congratulations! You beat the unbeatable AI!")
            break

        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break

        # AI Turn ('O')
        print("AI is thinking...")

        ai_choice = ai_move()
        board[ai_choice] = "O"

        if check_winner(board, "O"):
            print_board()
            print("AI wins! Better luck next time.")
            break

        if is_board_full(board):
            print_board()
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_game()
