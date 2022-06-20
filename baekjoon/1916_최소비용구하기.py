import sys


def dijkstra(start):
    dist[start] = 0
    visit[start] = 1
    for _ in range(N):
        visit[start] = 1
        for e, c in graph[start]:
            dist[e] = min(dist[e], dist[start] + c)
        min_value = INF
        for i in range(1, N + 1):
            if not visit[i] and min_value > dist[i]:
                start, min_value = i, dist[i]


input = sys.stdin.readline
N = int(input())
M = int(input())
INF = 0xfffffff
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
dist = [INF] * (N + 1)
visit = [0] * (N + 1)
S, E = map(int, input().split())
dijkstra(S)
print(dist[E])