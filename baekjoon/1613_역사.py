import sys
input = sys.stdin.readline


n, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    s, e = map(int, input().split())
    graph[s - 1][e - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for _ in range(s:=int(input())):
    a, b = map(int, input().split())
    if graph[a - 1][b - 1]:
        print(-1)
    elif graph[b - 1][a - 1]:
        print(1)
    else:
        print(0)
