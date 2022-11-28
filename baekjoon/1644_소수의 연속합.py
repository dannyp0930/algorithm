def find_prime(n):
    sieve = [1] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(2, n + 1) if sieve[i]]

N = int(input())
prime_list = find_prime(N)
M = len(prime_list)
ans = 0
tot = 0
e = 0
for s in range(M):
    while tot < N and e < M:
        tot += prime_list[e]
        e += 1
    if tot == N:
        ans += 1
    tot -= prime_list[s]
print(ans)
