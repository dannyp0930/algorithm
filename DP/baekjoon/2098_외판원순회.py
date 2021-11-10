def dfs(n, visit):
    if visit == (1 << N) - 1:
        if arr[n][0]:
            return arr[n][0]
        else:
            return INF
    if dp[n][visit] != INF:
        return dp[n][visit]
    for i in range(1, N):
        if not arr[n][i]: continue
        if visit & (1 << i): continue
        dp[n][visit] = min(dp[n][visit], dfs(i, visit | (1 << i)) + arr[n][i])
    return dp[n][visit]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = float('inf')
dp = [[INF] * (1 << N) for _ in range(N)]
print(dfs(0, 1))
