import sys


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0xffffff] * (N + 1) for _ in range(N + 1)]

# 자기 자신은 0으로
for n in range(1, N + 1):
    graph[n][n] = 0

# 그래프 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

# 플로이드-워셜
for m in range(1, N + 1):
    for s in range(1, N + 1):
        for e in range(1, N + 1):
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]

# 최소 케빈 베이컨 수 계산
ans = 0
min_kevin = 0xffffff
for i in range(1, N + 1):
    kevin = sum(graph[i][1:])
    if min_kevin > kevin:
        ans = i
        min_kevin = kevin
print(ans)
