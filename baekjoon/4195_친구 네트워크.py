def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[y] = x
    visit[x] += visit[y]


for _ in range(int(input())):
    F = int(input())
    parent = {}
    visit = {}
    for _ in range(F):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            visit[a] = 1
        if b not in parent:
            parent[b] = b
            visit[b] = 1
        union(a, b)
        print(visit[find(a)])
