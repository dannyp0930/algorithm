import sys, heapq


def prim(s):
    visit = [0] * V
    ans = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        w, v = heapq.heappop(heap)
        if visit[v]: continue
        visit[v] = 1
        ans += w
        for u, w in graph[v]:
            heapq.heappush(heap, (w, u))
    print(ans)


INF = sys.maxsize
V, E = map(int, input().split())
graph = [[] for _ in range(V)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A - 1].append((B - 1, C))
    graph[B - 1].append((A - 1, C))
prim(0)
