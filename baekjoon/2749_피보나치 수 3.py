def fibonacci(n):
    m = 1000000
    p = 1500000
    a, b = 0, 1
    for _ in range(n % p):
        a, b = b % m, (a + b) % m
    return a


n = int(input())
print(fibonacci(n))
