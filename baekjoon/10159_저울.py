import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][m] and graph[m][e]:
                graph[s][e] = 1
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j: continue
        if not graph[i][j] and not graph[j][i]:
            cnt += 1
    print(cnt)
