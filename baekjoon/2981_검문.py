def GCD(a, b):
    while b:
        t = a % b
        a, b = b, t
    return a


N = int(input())
arr = sorted([int(input()) for _ in range(N)])
lst = [arr[i] - arr[i - 1] for i in range(1, N)]
gcd = lst[0]
for j in range(1, N - 1):
    gcd = GCD(gcd, arr[j + 1] - arr[j])
res = {gcd, }
for k in range(2, int(gcd ** 0.5) + 1):
    if not gcd % k:
        res.add(k)
        res.add(gcd // k)
print(*sorted(res))
