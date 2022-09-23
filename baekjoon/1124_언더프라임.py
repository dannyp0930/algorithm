def factor(n):
    m = int(n ** 0.5)
    res = []
    for i in range(2, m + 1):
        while n % i == 0:
            n //= i
            res.append(i)
    if n > 1:
        res.append(n)
    return res


def is_prime(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True


A, B = map(int, input().split())
cnt = 0
for n in range(A, B + 1):
    factor_cnt = len(factor(n))
    if is_prime(factor_cnt):
        cnt += 1
print(cnt)
