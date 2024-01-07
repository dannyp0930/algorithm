import sys
input = sys.stdin.readline


def get_gcd(a, b):
    if a > b:
        b, a = a, b
    r = b % a
    if r == 0:
        return a
    return get_gcd(r, a)


N = int(input())
trees = [int(input()) for _ in range(N)]
trees.sort()
dist = [trees[i + 1] - trees[i] for i in range(N - 1)]
dist_set = list(set(dist))
gcd = dist_set[0]
for i in range(1, len(dist_set)):
    gcd = get_gcd(gcd, dist_set[i])
ans = 0
for d in dist:
    ans += d // gcd - 1
print(ans)
