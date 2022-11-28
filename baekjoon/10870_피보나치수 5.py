# 재귀
def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num - 1) + fibo(num -2)


# memoization
def fibo_memo(num):
    if num == 0:
        return 0
    memo = [0] * (num + 1)
    memo[1] = 1
    for i in range(2, num + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[num]

n = int(input())
print(fibo(n))
print(fibo_memo(n))