import sys


def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
ans = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        ans += c
print(ans)
