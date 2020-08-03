def solve_sudoku(S, x, y):
    # print(S[2][2][0],end='')
    if y == 9:
        if x == 8:
            print(S)
            exit(0)
        else:
            solve_sudoku(S, x + 1, 0)

    elif S[x][y] == 0:
        for k in range(1, 10):
            if feasible(S, x, y, k):
                S[x][y] = k
                solve_sudoku(S, x, y + 1)
                S[x][y] = 0
    else:
        solve_sudoku(S, x, y + 1)


def feasible(S, x, y, k):
    for i in range(9):
        if S[x][i] == k:
            return False
    for i in range(9):
        if(S[i][y] == k):
            return False

    a = int(x / 3)
    b = int(y / 3)
    for i in range(a * 3, 3 * a + 3):
        for j in range(b * 3, 3 * b + 3):
            if S[i][j] == k:
                return False
    return True


