from collections import deque
import sys
input = sys.stdin.readline


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, K = map(int, input().split())
virus = []
graph = []
for i in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(N):
        if tmp[j]:
            virus.append((tmp[j], 0, i, j))
S, X, Y = map(int, input().split())
virus.sort()
q = deque(virus)
while q:
    k, t, r, c = q.popleft()
    if t == S:
        break
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if not graph[nr][nc]:
                graph[nr][nc] = k
                q.append((k, t + 1, nr, nc))
print(graph[X - 1][Y - 1])
