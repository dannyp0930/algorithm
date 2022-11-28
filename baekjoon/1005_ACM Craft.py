import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input())):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    build = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        build[X].append(Y)
        in_degree[Y] += 1
    DP = [0] * (N + 1)
    Q = deque()
    for i in range(1, N + 1):
        if not in_degree[i]:
            Q.append(i)
            DP[i] = D[i]
    while Q:
        v = Q.popleft()
        for u in build[v]:
            in_degree[u] -= 1
            DP[u] = max(DP[u], DP[v] + D[u])
            if not in_degree[u]:
                Q.append(u)
    W = int(input())
    print(DP[W])
