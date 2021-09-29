# DP

def fibonacci(n):
    memo = [[1, 0], [0, 1]]
    if n > 1:
        for i in range(2, n + 1):
            cnt_0 = memo[i - 1][0] + memo[i - 2][0]
            cnt_1 = memo[i - 1][1] + memo[i - 2][1]
            memo.append([cnt_0, cnt_1])
    return memo[n][0], memo[n][1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a, b = fibonacci(N)
    print(a, b)


