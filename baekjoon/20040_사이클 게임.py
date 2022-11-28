import sys


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n)]
ans = 0
for idx, (a, b) in enumerate(edges):
    if find(a) != find(b):
        union(a, b)
    else:
        ans = idx + 1
        break
print(ans)
