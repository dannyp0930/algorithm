MAX_VALUE = float('inf')
for _ in range(int(input())):
    K = int(input())
    pages = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]
    psum = {-1: 0}
    for i in range(K):
        psum[i] = psum[i - 1] + pages[i]
    for size in range(1, K):
        for i in range(K - 1):
            j = i + size
            if j >= K:
                break
            dp[i][j] = MAX_VALUE
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + psum[j] - psum[i - 1])
    print(dp[0][K - 1])
