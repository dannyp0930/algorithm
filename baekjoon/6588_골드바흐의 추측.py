import sys
input = sys.stdin.readline


sieve = [1] * 1000000
for i in range(2, 1001):
    if sieve[i]:
        sieve[i + i::i] = [0] * len(sieve[i + i::i])
while n := int(input()):
    for i in range(3, n // 2 + 1, 2):
        if sieve[i] and sieve[n - i]:
            print(n, "=", i, "+", n - i)
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
