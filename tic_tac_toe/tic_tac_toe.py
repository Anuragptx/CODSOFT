import sys

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def moves_left(board):
    return EMPTY in board

def evaluate(board):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for state in win_states:
        a, b, c = state

        if board[a] == board[b] == board[c]:
            if board[a] == AI:
                return 10
            elif board[a] == HUMAN:
                return -10

    return 0

def check_win(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for state in win_states:
        a, b, c = state
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not moves_left(board):
        return 0

    if is_max:
        best_score = -1000

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                best_score = max(best_score, minimax(board, depth + 1, False))
                board[i] = EMPTY

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                best_score = min(best_score, minimax(board, depth + 1, True))
                board[i] = EMPTY

        return best_score

def find_best_move(board):
    best_score = -1000
    best_move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def main():
    print("===== TIC TAC TOE =====")
    print("You : X")
    print("Computer : O")

    print("\nPositions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    board = [EMPTY] * 9

    while True:
        choice = input("\nDo you want to play first? (y/n): ").lower()

        if choice in ['y', 'n']:
            break

        print("Enter y or n only.")

    current_player = HUMAN if choice == 'y' else AI

    while moves_left(board) and not check_win(board, HUMAN) and not check_win(board, AI):

        if current_player == HUMAN:
            print_board(board)

            while True:
                try:
                    move = int(input("Enter position (1-9): ")) - 1

                    if 0 <= move <= 8 and board[move] == EMPTY:
                        board[move] = HUMAN
                        break
                    else:
                        print("Invalid move.")

                except ValueError:
                    print("Enter a valid number.")

            current_player = AI

        else:
            print("\nComputer is playing...")
            move = find_best_move(board)

            if move != -1:
                board[move] = AI
                print(f"Computer chose position {move + 1}")

            current_player = HUMAN

    print_board(board)

    if check_win(board, AI):
        print("Computer wins!")
    elif check_win(board, HUMAN):
        print("You win!")
    else:
        print("Match Draw!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame Closed")
        sys.exit()


