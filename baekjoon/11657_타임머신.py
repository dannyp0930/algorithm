import sys


def bellman_ford():
    for i in range(N):
        for j in range(M):
            cur, next, cost = edges[j]
            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == N - 1:
                    return True
    return False


input = sys.stdin.readline
INF = float('inf')
N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
dist = [INF] * (N + 1)
dist[1] = 0
res = bellman_ford()
if res:
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
