MAX = 1000000
dp = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        dp[j] += i
    dp[i] += dp[i - 1]

for _ in range(int(input())):
    N = int(input())
    print(dp[N])
