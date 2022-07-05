import heapq


def dijkstra(start, end):
    dist = [INF] * N
    dist[start] = 0
    q = [(0, start)]
    while q:
        s = heapq.heappop(q)[1]
        for e, t in graph[s]:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                heapq.heappush(q, (dist[e], e))
    return dist[end]


N, M, X = map(int, input().split())
INF = 0xfffffff
graph = [[] for _ in range(N)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s - 1].append((e - 1, t))
max_dist = 0
for i in range(N):
    if i == X - 1: continue
    dist_i_x_i = dijkstra(i, X - 1) + dijkstra(X - 1, i)
    max_dist = max(max_dist, dist_i_x_i)
print(max_dist)
