n = int(input())
memo = [0, 1, 2]
if n > 2:
    for i in range(3, n + 1):
        num = (memo[i - 1] + memo[i - 2]) % 10007
        memo.append(num)
print(memo[n])
