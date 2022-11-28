def pow(x, n):
    if n == 0:
        return 1
    tmp = pow(x, n // 2)
    if n % 2:
        return tmp * tmp * x % P
    return tmp * tmp % P


N, K = map(int, input().split())
P = 1000000007
A = B = 1
for i in range(1, N + 1):
    A *= i
    A %= P
for j in range(1, K + 1):
    B *= j
    B %= P
for k in range(1, N - K + 1):
    B *= k
    B %= P
print((A * pow(B, P - 2)) % P)
