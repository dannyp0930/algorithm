import sys


def dfs(u):
    for v, w in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + w
            dfs(v)


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize
n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 루트에서 가장 먼 임의의 노드 x 구하기
dist = [-1] * (n + 1)
dist[1] = 0
dfs(1)
dist_1_x = 0
index_x = 0
for i in range(1, n + 1):
    if dist_1_x < dist[i]:
        index_x, dist_1_x = i, dist[i]

# 임의의 노드 x에서 가장 먼 y 구하기
dist = [-1] * (n + 1)
dist[index_x] = 0
dfs(index_x)
dist_x_y = 0
index_y = 0
for i in range(1, n + 1):
    if dist_x_y < dist[i]:
        index_y, dist_x_y = i, dist[i]
print(dist_x_y)
