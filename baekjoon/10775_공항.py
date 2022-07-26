import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
arr = [int(input()) for _ in range(P)]
ans = 0
for g in arr:
    p = find(g)
    if p == 0:
        break
    ans += 1
    union(p - 1, p)
print(ans)
