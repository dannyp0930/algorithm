def eratosthenes(N, K):
    sieve = [True] * (N + 1)
    cnt = 0
    for i in range(2, N + 1):
        if sieve[i]:
            for j in range(i, N + 1, i):
                if sieve[j]:
                    sieve[j] = False
                    cnt += 1
                if cnt == K:
                    return j


N, K = map(int, input().split())
print(eratosthenes(N, K))
