sieve = [1] * 1000000
for i in range(2, 1001):
    if sieve[i]:
        for j in range(i + i, 1000000, i):
            sieve[j] = 0

while 1:
    n = int(input())
    if not n:
        break
    for i in range(3, n // 2 + 1):
        if sieve[i] and sieve[n - i]:
            print(n, "=", i, "+", n - i)
            break