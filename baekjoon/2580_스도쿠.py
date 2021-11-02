# 백트래킹


def promise(x, y):
    promise_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        # 행 검사
        if arr[i][y] in promise_num:
            promise_num.remove(arr[i][y])
        # 열 검사
        if arr[x][i] in promise_num:
            promise_num.remove(arr[x][i])

    # 박스 검사
    x, y = x // 3, y // 3
    for j in range(x * 3, (x + 1) * 3):
        for k in range(y * 3, (y + 1) * 3):
            if arr[j][k] in promise_num:
                promise_num.remove(arr[j][k])
    return promise_num


def dfs(n):
    global flag
    if flag:
        return
    if n == len(zero):
        for lst in arr:
            print(*lst)
        flag = True
        return
    else:
        x, y = zero[n]
        promise_num = promise(x, y)
        for num in promise_num:
            arr[x][y] = num
            dfs(n + 1)
            arr[x][y] = 0


arr = [list(map(int, input().split())) for _ in range(9)]
zero = [(a, b) for a in range(9) for b in range(9) if not arr[a][b]]
flag = False
dfs(0)
