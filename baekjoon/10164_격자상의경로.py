# DP


def go(x1, y1, x2, y2):
    R = x2 - x1 + 1
    C = y2 - y1 + 1
    dp = [[0] * C for _ in range(R)]
    for i in range(R):
        dp[i][0] = 1
    for j in range(C):
        dp[0][j] = 1
    for k in range(2, R + C - 1):
        for m in range(1, k):
            if m < 0 or k - m < 0 or m >= R or k - m >= C: continue
            dp[m][k - m] = dp[m - 1][k - m] + dp[m][k - m - 1]
    return dp[R - 1][C - 1]


N, M, K = map(int, input().split())
arr = [[j + i * M + 1 for j in range(M)] for i in range(N)]
r, c = (K - 1) // M, (K - 1) % M    # 표시된 좌표
if K == 0:     # 주어진 좌표가 없는 경우
    print(go(0, 0, N - 1, M - 1))
else:
    print(go(0, 0, r, c) * go(r, c, N - 1, M - 1))
