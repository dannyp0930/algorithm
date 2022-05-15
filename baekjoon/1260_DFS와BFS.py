def dfs(graph, node, start):
    visit = [0] * (node + 1)
    stack = [start]
    ans = []
    while stack:
        n = stack.pop()
        if not visit[n]:
            visit[n] = 1
            ans.append(n)
            for v in sorted(graph[n], reverse=True):
                if not visit[v]:
                    stack.append(v)
    return ans


def bfs(graph, node, start):
    visit = [0] * (node + 1)
    queue = [start]
    ans = []

    while queue:
        n = queue.pop(0)
        if not visit[n]:
            visit[n] = 1
            ans.append(n)
            for v in graph[n]:
                if not visit[v]:
                    queue.append(v)

    return ans


N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)
for i in range(N + 1):
    G[i].sort()
print(*dfs(G, N, V))
print(*bfs(G, N, V))
