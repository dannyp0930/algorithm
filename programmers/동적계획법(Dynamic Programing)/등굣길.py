def solution(m, n, puddles):
    mod = 1000000007
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for c, r in puddles:
        dp[r - 1][c - 1] = -1
    for i in range(n):
        for j in range(m):
            if not i and not j: continue
            if dp[i][j] == -1: continue
            if dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]
            if dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]
    return dp[-1][-1] % mod