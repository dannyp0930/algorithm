sieve = [1] * 10001
sieve[0], sieve[1] = 0, 0
for i in range(2, 101):
    if sieve[i]:
        for j in range(i + i, 10001, i):
            sieve[j] = 0

for _ in range(int(input())):
    n = int(input())
    a = n // 2
    b = a
    while 1:
        if sieve[a] and sieve[b]:
            print(a, b)
            break
        a -= 1
        b += 1
