#  Sudoku Game in Python
**Learning / Demo Project:** Developed as part of my learning journey to practice Python
A command-line based **Sudoku Game**, created as a learning project in Python. It includes both **human interaction** and **computer-assisted solving**, with a feature that allows the player to give up and let the computer solve the puzzle.
This project is built primarily for **educational purposes** — to practice Python basics, algorithms like **backtracking**, and get hands-on with concepts like **recursion**, **input handling**, and **code structure**.

---

##  Features

-  Generates a **new random Sudoku puzzle** with a unique solution.
-  Allows **player interaction** to fill in Sudoku numbers.
-  Checks if a move is **valid** as per Sudoku rules (rows, columns, 3x3 boxes).
-  Includes a **backtracking-based solver** to auto-solve puzzles.
-  If the user gets tired, they can press `'t'` and the **computer solves the rest**.
-  Computer also attempts its own moves after the player (optional feature).
-  Simple command-line interface, no external libraries (except `random`, `sys`).

---

##  Learning Outcomes

This project was created as part of a self-guided learning journey and includes:

- Writing structured Python code with multiple functions
- Implementing classic **backtracking** algorithm
- Practicing **2D list** manipulation
- Learning how to handle **user inputs and exits**
- Using **Git & GitHub** for version control and publishing code

---

##  How to Run

1. **Clone the repo** or download the code:

    ```bash
    git clone https://github.com/YOUR_USERNAME/sudoku-game.git
    cd sudoku-game
    ```

2. **Run the game:**

    ```bash
    python sudoku_game.py
    ```

3. **Play:**
    - Enter numbers 1–9 for row, column, and number inputs.
    - Enter `q` at any prompt to quit the game.
    - Press `t` after your turn to let the computer finish solving the puzzle.

---

##  Limitations

-  No graphical interface — this is purely **text-based**.
-  No automated test cases or error logging.
-  Computer moves are **not optimal**, just basic valid tries.
-  No Input Error Correction

---

##   Improvements

-  Add a **GUI** using `Tkinter` or `Pygame`.
-  Make the computer play **smarter** with strategies.
-  Add a **score system** or move counter.
-  Add **difficulty levels** (Easy, Medium, Hard).
- ⌨ Add support for **undo** and **hint system**.

---

## References & Learning resources

- [Sudoku Solver using Backtracking – GeeksforGeeks](https://www.geeksforgeeks.org/sudoku-backtracking-7/)
- [Computerphile – Solving Sudoku with Computers (YouTube)](https://www.youtube.com/watch?v=G_UYXzGuqvM)
- [Stack Overflow – For Logic](https://stackoverflow.com/questions)
- [ChatGPT by OpenAI : for debugging and code improvements](https://chatgpt.com/)

---

###  If you found this helpful, feel free to explore the repo and suggest improvements!
