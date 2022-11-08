encode = input()
if encode[0] == '0':
    print(0)
else:
    encode = '0' + encode
    n = len(encode)
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n):
        if encode[i] != '0':
            dp[i] = dp[i - 1]
        if 10 <= int(encode[i - 1: i + 1]) <= 26:
            dp[i] += dp[i - 2]
    print(dp[n - 1] % 1000000)
