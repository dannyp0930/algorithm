# DFS
def dfs(v, cnt):
    visit_dfs[v] = cnt
    for w in G[v]:
        if visit_dfs[w] == -1:
            dfs(w, visit_dfs[v] + 1)


# BFS
def bfs(v):
    Q.append(v)
    visit_bfs[v] = 0
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if visit_bfs[w] == -1:
                visit_bfs[w] = visit_bfs[v] + 1
                Q.append(w)


n = int(input())
a, b = map(int, input().split())
m = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
visit_dfs = [-1] * (n + 1)
visit_bfs = [-1] * (n + 1)
Q = []
dfs(a, 0)
bfs(a)
print(visit_dfs[b], visit_bfs[b])