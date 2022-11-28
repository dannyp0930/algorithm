def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        dist = round(((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5, 2)
        edges.append((dist, i, j))
edges.sort()
ans = 0
for edge in edges:
    d, a, b = edge
    if find(a) != find(b):
        union(a, b)
        ans += d
print(ans)
