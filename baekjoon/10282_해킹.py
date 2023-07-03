import sys
import heapq
input = sys.stdin.readline


def dijkstra(c):
    heap = [[c, 0]]
    dist[c] = 0
    while heap:
        n, s = heapq.heappop(heap)
        for v, w in com[n]:
            if dist[v] == -1 or s + w < dist[v]:
                dist[v] = s + w
                heapq.heappush(heap, [v, s + w])


INF = float('inf')
for _ in range(t := int(input())):
    n, d, c = map(int, input().split())
    com = [[] * n for _ in range(n)]
    dist = [-1] * n
    for _ in range(d):
        a, b, s = map(int, input().split())
        com[b - 1].append([a - 1, s])
    dijkstra(c - 1)
    print(n - dist.count(-1), max(dist))
