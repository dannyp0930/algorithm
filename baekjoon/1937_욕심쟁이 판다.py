import sys


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(r, c):
    if dp[r][c]: return dp[r][c]
    dp[r][c] = 1
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < n and 0 <= nc < n): continue
        if arr[nr][nc] > arr[r][c]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]


sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
ans = 0
for r in range(n):
    for c in range(n):
        ans = max(ans, dfs(r, c))
print(ans)
