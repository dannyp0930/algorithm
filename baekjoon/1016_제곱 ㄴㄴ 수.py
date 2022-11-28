MIN, MAX = map(int, input().split())
dp = [1] * (MAX - MIN + 1)
cnt = 0
i = 2
while i ** 2 <= MAX:
    j = MIN // i ** 2
    while (i ** 2) * j <= MAX:
        idx = (i ** 2) * j - MIN
        if 0 <= idx <= MAX - MIN:
            dp[idx] = 0
        j += 1
    i += 1
print(sum(dp))
