#  Tic-Tac-Toe AI using Minimax Algorithm
#  Project Description

This project is a simple Tic-Tac-Toe game developed in Python where a human player competes against the computer. The computer uses the Minimax Algorithm to choose the best possible move. Because of this algorithm, the AI never loses; it can either win or force the game to end in a draw.

The game runs in the terminal and allows the player to enter moves using positions from 1 to 9.

#  How to Run
Make sure Python is installed on your system.
Open a terminal or command prompt.
Navigate to the project folder.
Run the following command:

python tic_tac_toe.py

#  Minimax Algorithm

Minimax is a decision-making algorithm used in games like Tic-Tac-Toe.

The AI checks all possible moves and their outcomes before making a decision.

If the AI wins, the move gets a positive score.
If the human wins, the move gets a negative score.
If the game ends in a draw, the score is zero.

The AI always chooses the move with the best score, which makes it impossible to beat.

#  Features

Human vs Computer gameplay
Unbeatable AI using Minimax
Input validation
Win, lose, and draw detection
Simple terminal-based interface

#  Sample Output

Human: X | AI: O

Enter your move (1-9): 5

AI is thinking...
AI chose position 1

 O |   |
---+---+---
   | X |
---+---+---
   |   |

   
#  Conclusion

This project demonstrates how the Minimax Algorithm can be used to make intelligent decisions in a game environment. It also helps in understanding basic concepts of Artificial Intelligence, game theory, and search algorithms.
