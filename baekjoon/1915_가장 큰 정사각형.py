import sys


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif not arr[i][j]:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        ans = max(ans, dp[i][j])
print(ans ** 2)
