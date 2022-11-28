import sys


def heappush(heap, c, x):
    heap.append((c, x))
    idx = len(heap) - 1
    while idx != 1 and c < heap[idx // 2][0]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx // 2


def heappop(heap):
    result = heap[1]
    heap[-1], heap[1] = heap[1], heap[-1]
    heap.pop()
    parent = 1
    while 1:
        child = parent * 2
        if child + 1 < len(heap) and heap[child][0] > heap[child + 1][0]:
            child += 1
        if child >= len(heap) or heap[child][0] > heap[parent][0]:
            break
        heap[child], heap[parent] = heap[parent], heap[child]
        parent = child
    return result


input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())
dist = [INF] * (n + 1)
parent = [0] * (n + 1)
dist[s] = 0
q = [0, (0, s)]
while len(q) > 1:
    c, u = heappop(q)
    if c > dist[u]: continue
    for v, w in graph[u]:
        cost = c + w
        if dist[v] > cost:
            dist[v] = cost
            heappush(q, cost, v)
            parent[v] = u
print(dist[e])
path = []
child = e
while 1:
    if child == 0:
        break
    path.append(child)
    child = parent[child]
print(len(path))
print(*reversed(path))
