max_n = 123456
max_2n = max_n * 2
sieve = [1] * (max_2n + 1)
sieve[0] = 0
sieve[1] = 0
for i in range(2, int(max_2n ** 0.5) + 1):
    if sieve[i]:
        for j in range(i + i, max_2n + 1, i):
            sieve[j] = 0
while 1:
    n = int(input())
    if not n: break
    print(sum(sieve[n + 1: 2 * n + 1]))
