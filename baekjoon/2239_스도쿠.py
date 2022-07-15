def row_check(r, n):
    for c in range(9):
        if arr[r][c] == n:
            return False
    return True


def col_check(c, n):
    for r in range(9):
        if arr[r][c] == n:
            return False
    return True


def square_check(r, c, n):
    R = (r // 3) * 3
    C = (c // 3) * 3
    for i in range(R, R + 3):
        for j in range(C, C + 3):
            if arr[i][j] == n:
                return False
    return True


def dfs(idx, cnt):
    if idx == cnt:
        for lst in arr:
            print(''.join(map(str, lst)))
        exit()
    r, c = zeros[idx]
    for n in range(1, 10):
        if row_check(r, n) and col_check(c, n) and square_check(r, c, n):
            arr[r][c] = n
            dfs(idx + 1, cnt)
            arr[r][c] = 0


arr = []
zeros = []
for r in range(9):
    row = list(map(int, input()))
    for c in range(9):
        if not row[c]:
            zeros.append([r, c])
    arr.append(row)
cnt_zeros = len(zeros)
dfs(0, cnt_zeros)
