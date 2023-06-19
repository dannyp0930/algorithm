import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(u):
    global cnt
    visit[u] = cnt
    for v in graph[u]:
        if not visit[v]:
            cnt += 1
            dfs(v)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]
visit = [0] * N
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
for lst in graph:
    lst.sort()
cnt = 1
dfs(R - 1)
for c in visit:
    print(c)
