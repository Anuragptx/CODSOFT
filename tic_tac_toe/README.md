# Unbeatable Tic-Tac-Toe AI in Python

A simple, terminal-based Tic-Tac-Toe game where a human plays against an unbeatable AI. The AI utilizes the **Minimax Algorithm** to simulate all possible outcomes and make optimal moves, ensuring it can never be defeated (it will either win or draw).

---

## 🎯 How to Run the Game

1. Make sure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:
   ```bash
   python tic_tac_toe.py
   ```

---

## 🧠 The Minimax Algorithm Explained (Simple Words)

Imagine you are playing a game of Tic-Tac-Toe and you can think ahead to all possible futures. You want to make a move that ensures the best outcome for you, assuming your opponent is also playing perfectly.

This is exactly what the **Minimax Algorithm** does. It is a decision-making algorithm used in two-player, turn-based, zero-sum games. Here is how it works:

1. **Simulate the Future**: The AI looks at the current board and simulates *every possible move* it could make. Then, it simulates *every possible response* the human could make, and so on, until the game ends (Win, Loss, or Draw).
2. **Assign Scores**: When a simulated game ends, it assigns a score:
   - **`+10` (Maximizing)**: The AI wins.
   - **`-10` (Minimizing)**: The Human wins.
   - **`0`**: The game is a draw.
3. **Backtracking**:
   - On the **AI's turn** (the Maximizer), it selects the move that yields the **highest** score.
   - On the **Human's turn** (the Minimizer), it assumes the human will choose the move that yields the **lowest** score (most disadvantageous for the AI).
4. **Optimal Play**: By working backwards from the end states, the AI calculates the score for every immediate move it can make and selects the one that guarantees at worst a draw.

---

## 🎮 Sample Game Output

Below is an example of what the gameplay looks like in the terminal:

```text
=======================================
      UNBEATABLE TIC-TAC-TOE AI        
=======================================
Human: X  |  AI: O
Grid positions are as follows:
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
=======================================
Do you want to play first? (y/n): y


   |   |   
---+---+---
   |   |   
---+---+---
   |   |   


Enter your move (1-9): 5

AI is thinking...
AI chose position 1


 O |   |   
---+---+---
   | X |   
---+---+---
   |   |   


Enter your move (1-9): 3

AI is thinking...
AI chose position 7


 O |   | X 
---+---+---
   | X |   
---+---+---
 O |   |   


Enter your move (1-9): 4

AI is thinking...
AI chose position 6


 O |   | X 
---+---+---
 X | X | O 
---+---+---
 O |   |   


Enter your move (1-9): 8

AI is thinking...
AI chose position 2


 O | O | X 
---+---+---
 X | X | O 
---+---+---
 O | X |   


Enter your move (1-9): 9


 O | O | X 
---+---+---
 X | X | O 
---+---+---
 O | X | X 


It's a draw! Well played.
```
