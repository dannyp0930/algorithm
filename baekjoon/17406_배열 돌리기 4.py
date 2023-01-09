def rotate(arr, R, C, S):
    r, c = R - S, C - S
    tmp = arr[r][c]
    for d in range(4):
        while 1:
            nr, nc = r + dr[d], c + dc[d]
            if not (R - S <= nr <= R + S and C - S <= nc <= C + S):
                break
            arr[nr][nc], tmp = tmp, arr[nr][nc]
            r, c = nr, nc


def arr_sum(arr):
    ans = INF
    for lst in arr:
        ans = min(ans, sum(lst))
    return ans


def dfs(cnt):
    global ans
    if cnt == K:
        copy_arr = [tmp[:] for tmp in arr]
        for i in stack:
            r, c, s = command[i]
            while s:
                rotate(copy_arr, r - 1, c - 1, s)
                s -= 1
        ans = min(ans, arr_sum(copy_arr))
        return
    for i in range(K):
        if i not in stack:
            stack.append(i)
            dfs(cnt + 1)
            stack.pop()


INF = float('inf')
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(K)]
stack = []
ans = INF
dfs(0)
print(ans)
