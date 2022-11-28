def find(x):
    if parent[x] !=x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]
ans = []
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        ans.append(edge[2])
print(sum(ans[:-1]))
