MAX = 1000000
# 약수 합 저장
dp = [1] * (MAX + 1)
# 누적 합 저장
g = [0] * (MAX + 1)

for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    g[i] = g[i - 1] + dp[i]

for _ in range(int(input())):
    N = int(input())
    print(g[N])
