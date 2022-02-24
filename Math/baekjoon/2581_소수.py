def prime_number(n):
    if n == 1:
        return False
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if not n % i:
            return False
    return True


M = int(input())
N = int(input())
result = []
for n in range(M, N + 1):
    if prime_number(n):
        result.append(n)
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
