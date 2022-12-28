from collections import deque


def bfs(w):
    visit = [0] * (N + 1)
    q = deque([X])
    visit[X] = 1
    while q:
        n = q.popleft()
        for v, c in graph[n]:
            if not visit[v] and c >= w:
                q.append(v)
                visit[v] = 1
    if visit[Y]:
        return True
    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
s, e = 0, int(1e9)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    e = max(e, C)
X, Y = map(int, input().split())
res = 0
while s <= e:
    m = (s + e) // 2
    if bfs(m):
        res = m
        s = m + 1
    else:
        e = m - 1
print(res)
