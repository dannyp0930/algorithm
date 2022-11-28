import sys

input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
for m in range(N):
    for s in range(N):
        for e in range(N):
            if graph[s][e] == 0 and graph[s][m] and graph[m][e]:
                graph[s][e] = 1
for lst in graph:
    print(*lst)
