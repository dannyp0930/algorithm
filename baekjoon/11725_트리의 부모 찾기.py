import sys


def dfs(s):
    for v in graph[s]:
        if not parent[v]:
            parent[v] = s
            dfs(v)


def bfs(s):
    queue = [s]
    visit[s] = 1
    while queue:
        s = queue.pop(0)
        for v in graph[s]:
            if not visit[v]:
                visit[v] = s
                queue.append(v)


input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs
parent = [0] * (N + 1)
parent[1] = 1
dfs(1)
for i in range(2, N + 1):
    print(parent[i])

#bfs
visit = [0] * (N + 1)
bfs(1)
for j in range(2, N + 1):
    print(visit[j])