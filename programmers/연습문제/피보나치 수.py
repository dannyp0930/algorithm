# 재귀
def fibo_recur(n):
    if n < 2:
        return n
    return fibo_recur(n - 1) + fibo_recur(n - 2)


# DP
def fibo_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1
    if n > 2:
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
    return dp[n] % 1234567
