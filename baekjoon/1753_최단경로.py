import sys
import heapq


def dijkstra(s):
    dist[s] = 0
    heapq.heappush(heap, (0, s))
    while heap:
        c, u = heapq.heappop(heap)
        if c > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))


input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
INF = sys.maxsize
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
dist = [INF] * (V + 1)
heap = []
dijkstra(K)
for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
