import sys
input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
x_list = []
y_list = []
z_list = []
for i in range(N):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
x_list.sort()
y_list.sort()
z_list.sort()
edges = []
for now in x_list, y_list, z_list:
    for i in range(1, N):
        w1, a = now[i - 1]
        w2, b = now[i]
        edges.append((a, b, abs(w1 - w2)))
edges.sort(key=lambda x: x[2])
parent = [i for i in range(N)]
ans = 0
for edge in edges:
    if find(edge[0]) != find(edge[1]):
        union(edge[0], edge[1])
        ans += edge[2]
print(ans)