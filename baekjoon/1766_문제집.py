import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_order = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_order[B] += 1
heap = []
for i in range(1, N + 1):
    if not in_order[i]:
        heapq.heappush(heap, i)
res = []
while heap:
    u = heapq.heappop(heap)
    res.append(u)
    for v in graph[u]:
        in_order[v] -= 1
        if not in_order[v]:
            heapq.heappush(heap, v)
print(*res)