# Tic-Tac-Toe with Unbeatable AI using Minimax Algorithm
# Designed for first-year B.Tech students - Simple, clean, and well-commented.

import sys

# Define symbols for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    """
    Prints the current state of the board in a clean grid format.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def is_moves_left(board):
    """
    Returns True if there are empty cells on the board, False otherwise.
    """
    return EMPTY in board

def evaluate(board):
    """
    Evaluates the board state.
    Returns:
        +10 if AI ('O') wins
        -10 if Human ('X') wins
         0 if draw or game is not finished
    """
    # Winning combinations (rows, columns, and diagonals)
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]]:
            if board[state[0]] == AI:
                return 10
            elif board[state[0]] == HUMAN:
                return -10
                
    return 0

def check_win(board, player):
    """
    Checks if the specified player (HUMAN or AI) has won the game.
    """
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for state in win_states:
        if board[state[0]] == board[state[1]] == board[state[2]] == player:
            return True
    return False

def minimax(board, depth, is_max):
    """
    The Minimax algorithm.
    It recursively simulates all possible future moves to find the best score.
    """
    score = evaluate(board)

    # If AI has won the game, return evaluated score (adjusted for depth to favor quicker wins)
    if score == 10:
        return score - depth

    # If Human has won the game, return evaluated score (adjusted for depth to delay losses)
    if score == -10:
        return score + depth

    # If there are no more moves and no winner, it's a draw
    if not is_moves_left(board):
        return 0

    # If it is the maximizer's turn (AI, 'O')
    if is_max:
        best = -1000
        # Traverse all cells
        for i in range(9):
            if board[i] == EMPTY:
                # Make the move
                board[i] = AI
                # Call minimax recursively and choose the maximum value
                best = max(best, minimax(board, depth + 1, False))
                # Undo the move (backtrack)
                board[i] = EMPTY
        return best

    # If it is the minimizer's turn (Human, 'X')
    else:
        best = 1000
        # Traverse all cells
        for i in range(9):
            if board[i] == EMPTY:
                # Make the move
                board[i] = HUMAN
                # Call minimax recursively and choose the minimum value
                best = min(best, minimax(board, depth + 1, True))
                # Undo the move (backtrack)
                board[i] = EMPTY
        return best

def find_best_move(board):
    """
    Finds the best possible move for the AI using the Minimax algorithm.
    """
    best_val = -1000
    best_move = -1

    # Traverse all cells, evaluate minimax function for all empty cells
    for i in range(9):
        if board[i] == EMPTY:
            # Make the move
            board[i] = AI
            # Compute evaluation function for this move
            move_val = minimax(board, 0, False)
            # Undo the move (backtrack)
            board[i] = EMPTY

            # If the value of the current move is better than the best value, update best
            if move_val > best_val:
                best_move = i
                best_val = move_val

    return best_move

def main():
    print("=======================================")
    print("      UNBEATABLE TIC-TAC-TOE AI        ")
    print("=======================================")
    print("Human: X  |  AI: O")
    print("Grid positions are as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("=======================================")

    # Initialize empty board
    board = [EMPTY] * 9

    # Ask the user who should play first
    while True:
        choice = input("Do you want to play first? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

    current_player = HUMAN if choice == 'y' else AI

    while is_moves_left(board) and not check_win(board, HUMAN) and not check_win(board, AI):
        if current_player == HUMAN:
            print_board(board)
            # Get human move
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if 0 <= move <= 8 and board[move] == EMPTY:
                        board[move] = HUMAN
                        break
                    else:
                        print("Invalid move! Cell is either occupied or out of bounds (1-9).")
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 9.")
            
            current_player = AI
        else:
            print("\nAI is thinking...")
            move = find_best_move(board)
            if move != -1:
                board[move] = AI
                print(f"AI chose position {move + 1}")
            current_player = HUMAN

    # Print final board
    print_board(board)

    # Check game results
    if check_win(board, AI):
        print("AI wins! Better luck next time.")
    elif check_win(board, HUMAN):
        print("Congratulations! You won! (This should not happen if AI is unbeatable!)")
    else:
        print("It's a draw! Well played.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame exited. Goodbye!")
        sys.exit(0)
