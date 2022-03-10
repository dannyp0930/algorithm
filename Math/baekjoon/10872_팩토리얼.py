memo = [0] * 13
memo[0] = memo[1] = 1
for i in range(2, 13):
    memo[i] = i * memo[i - 1]


N = int(input())
print(memo[N])