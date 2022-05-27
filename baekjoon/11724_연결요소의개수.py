import sys


def dfs(start):
    stack = [start]
    while stack:
        n = stack.pop()
        if visit[n]: continue
        visit[n] = 1
        for v in graph[n]:
            if visit[v]: continue
            stack.append(v)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visit = [0] * (N + 1)
cnt = 0
for i in range(1, N + 1):
    if visit[i]: continue
    dfs(i)
    cnt += 1
print(cnt)
