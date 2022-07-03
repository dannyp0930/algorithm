import sys


def bellman_ford(start):
    dist = [INF] * (N + 1)
    dist[start] = 0
    for i in range(N):
        for edge in edges:
            s, e, t = edge
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == N - 1:
                    return True
    return False


input = sys.stdin.readline
INF = sys.maxsize
for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    if bellman_ford(1):
        print('YES')
    else:
        print('NO')
