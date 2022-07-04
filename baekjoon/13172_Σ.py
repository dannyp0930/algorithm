def power(n, m):
    if m == 1:
        return n % modular
    if m % 2:
        return n * power(n, m - 1) % modular
    else:
        x = power(n, m // 2)
        return x * x % modular

modular = 1000000007
ans = 0
for _ in range(int(input())):
    N, S = map(int, input().split())
    ans += S * power(N, modular - 2) % modular
print(ans % modular)
