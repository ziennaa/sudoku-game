import random # imports random to pick random numbers and shuffle cells
import sys # calls sys.exit() so program can end whenver user quits
# function to print the board
def print_board(board):
    '''
    displays 9*9 board in a formatted grid
    with lines separating 3*3 subgrids basically 2d list board 9*9
    '''
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")
            '''
            every time i is a multiple of 3 it print horizontal seperator
            this is row index or used for maing row
            '''
        for j in range(9):
          '''
          every time j is multiple of 3, we print vertical bars without
          for coloumns
          '''
          if j % 3 == 0 and j != 0:
                print("|", end=" ")
          print(board[i][j] if board[i][j] != 0 else ".", end=" ")
            # prints cells value if nonzero otherwise . to make empty cell
            # on the same line end=" "
        print() # for moving to next line

# function to find an empty cell in board
def find_empty(board):# searches the grid
    for i in range(9):
        for j in range(9):
          # used for scanning every row i and every col j to look for 0(indicates empty)
            if board[i][j] == 0:
                return (i, j) # returns row and col as soon as it finds empty 
    return None

# function to check if placing num at pos is valid
def is_valid(board, num, pos):# check if you can place a number at row or col
    row, col = pos
    if any(board[row][i] == num for i in range(9) if i != col): #scaNS row for duplicates
        return False
    if any(board[i][col] == num for i in range(9) if i != row): # scans entire col for duplicates
        return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False # if num appears somewhere else move illegal
    return True # if not true

# Backtracking solver
def solve_board(board):
  # here function find empty and is valid is used 
  # to fill the board , it tries all numbers from 1 to 9 at each empty cell and proceeds only if valid
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_board(board):
                return True
            board[row][col] = 0
    return False

def count_solutions(board):
  # counts all possible ways to create or complete the solutuion 
  # no empty you found sol and returns 1
  # and finds total num of solution and stores in count
    empty = find_empty(board)
    if not empty:
        return 1
    row, col = empty
    count = 0
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            count += count_solutions(board)
            board[row][col] = 0
    return count

def create_board(removals=30):
   # creates an empty board
# num cell is used to choose difficulty
# here removal check that only 1 unique sol remains using count_solutions
    board = [[0]*9 for _ in range(9)]
    solve_board(board)
    removed = 0
    while removed < removals:
        r = random.randrange(9)
        c = random.randrange(9)
        if board[r][c] != 0:
            temp = board[r][c]
            board[r][c] = 0
            copy = [row[:] for row in board]
            if count_solutions(copy) != 1:
                board[r][c] = temp
            else:
                removed += 1
    return board

def is_complete(board):
    return all(cell != 0 for row in board for cell in row)
    # returns if every cell in grid is non zero

def get_input(prompt):
    while True:
        inp = input(prompt)
        if inp.lower() == 'q': # q to exit the program
            sys.exit("Goodbye!")
        if inp.isdigit() and 1 <= int(inp) <= 9:
            return int(inp) - 1
        print("Invalid input. Enter 1-9 or 'q'.")

def player_turn(board):
    print("\n your move:")
    print_board(board)
    while True:
        row = get_input("Enter row (1-9) or 'q' to quit: ")
        col = get_input("Enter column (1-9) or 'q' to quit: ")
        if board[row][col] == 0:
            break
        print("choose another, cell already filled")
    while True:
        num = get_input("Enter number (1-9) or 'q' to quit: ") + 1
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            break
        print("invalid try again")

def computer_turn(board):
    print("\nComputer's move:")
    print_board(board)
    empties = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
    random.shuffle(empties)
    for row, col in empties:
        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                if count_solutions([r[:] for r in board]) == 1:
                    print(f"Computer placed {num} at ({row+1},{col+1})")
                    return
                board[row][col] = 0
    print("computer gives up. multiple solutions possible.")

if __name__ == "__main__":
    puzzle = create_board(removals=30)
    while True:
        player_turn(puzzle)
        cont = input("\nPress 't' if tired and let computer solve it, any other key to continue: ")
        if cont.lower() == 't':
            solve_board(puzzle)
            print_board(puzzle)
            print("\n Computer has solved the rest of the puzzle :(( Game over.")
            break
        if is_complete(puzzle):
            print_board(puzzle)
            print("Congratulations! You solved it!!!!")
            break
        computer_turn(puzzle)
        if is_complete(puzzle):
            print_board(puzzle)
            print("Computer solved it!! You lose!!!!")
            break
