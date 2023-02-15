N = int(input())
dp = [0] * 1001
dp[2] = 1
for i in range(4, N + 1):
    if not dp[i - 1] or not dp[i - 3]:
        dp[i] = 1
if dp[N]:
    print('SK')
else:
    print('CY')
