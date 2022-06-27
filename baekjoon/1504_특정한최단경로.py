import sys

class heap:
    def __init__(self, data):
        self.queue = [0, data]

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def insert(self, v, w):
        self.queue.append([v, w])
        idx = len(self.queue) - 1
        while idx != 1 and w < self.queue[idx // 2][1]:
            self.swap(idx, idx // 2)
            idx //= 2

    def delete(self):
        result = self.queue[1]
        self.swap(-1, 1)
        self.queue.pop()
        self.sort()
        return result

    def sort(self):
        parent = 1
        while 1:
            child = parent * 2
            if child + 1 < len(self.queue) and self.queue[child] > self.queue[child + 1]:
                child += 1
            if child >= len(self.queue) or self.queue[child] > self.queue[parent]:
                break
            self.swap(child, parent)
            parent = child
    
    def length(self):
        return len(self.queue)


def dijkstra(s, e):
    dist = [INF] * (N + 1)
    dist[s] = 0
    h = heap([s, 0])
    while h.length() > 1:
        u, c = h.delete()
        if c > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                h.insert(v, w)
    return dist[e]


input = sys.stdin.readline
INF = 0xfffffff
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())
dist1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
dist2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
if dist1 >= INF and dist2 >= INF:
    print(-1)
else:
    print(min(dist1, dist2))
