def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)): #left diagonal
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)): #right diagonal
        if board[i][j] == 1:
            return False

    return True

def solve_nqueen(board, row, n):
    if row == n:
        for r in range(n):
            print(" ".join(["Q" if c == 1 else "." for c in board[r]]))
        print()
        return True
    
    res = False #recursive case
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  
            res = solve_nqueen(board, row + 1, n) or res  
            board[row][col] = 0  
    
    return res

def n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueen(board, 0, n):
        print("Solution does not exist")

n_queen(4)  
