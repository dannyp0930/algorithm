n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = arr[0]
if n > 1:
    dp[1] = dp[0] + arr[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
print(dp[n - 1])
