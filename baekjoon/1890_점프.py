dr = [1, 0]
dc = [0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for r in range(N):
    for c in range(N):
        if r == N - 1 and c == N - 1:
            break
        for d in range(2):
            nr, nc = r + arr[r][c] * dr[d], c + arr[r][c] * dc[d]
            if nr >= N or nc >= N: continue
            dp[nr][nc] += dp[r][c]
print(dp[N - 1][N - 1])


# DFS 활용
# dr = [1, 0]
# dc = [0, 1]
#
#
# def dfs(r, c):
#     if r == N - 1 and c == N - 1:
#         return 1
#     if dp[r][c] != -1:
#         return dp[r][c]
#     dp[r][c] = 0
#     for d in range(2):
#         nr, nc = r + arr[r][c] * dr[d], c + arr[r][c] * dc[d]
#         if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
#         dp[r][c] += dfs(nr, nc)
#     return dp[r][c]
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# dp = [[-1] * N for _ in range(N)]
# print(dfs(0, 0))
