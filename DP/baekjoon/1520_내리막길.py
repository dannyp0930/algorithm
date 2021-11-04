dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nc < 0 or nr >= M or nc >= N: continue
        if arr[nr][nc] >= arr[r][c]: continue
        dp[r][c] += dfs(nr, nc)
    return dp[r][c]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
