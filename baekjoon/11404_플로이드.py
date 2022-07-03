import sys

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] > c:
        graph[a - 1][b - 1] = c
for m in range(n):
    for s in range(n):
        for e in range(n):
            if s != e and graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]
for lst in graph:
    for i in range(n):
        if lst[i] == INF:
            lst[i] = 0
    print(*lst)
