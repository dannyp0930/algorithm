N = int(input())
M = int(input())
vip = [int(input()) for _ in range(M)]
if N == 1:
    print(1)
else:
    dp = [1] * (N + 1)
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    ans = 1
    idx = 0
    for n in vip:
        ans *= dp[n - idx - 1]
        idx = n
    ans *= dp[N - idx]
    print(ans)
