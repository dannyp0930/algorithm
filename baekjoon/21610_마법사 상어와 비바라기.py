import sys
input = sys.stdin.readline


dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
for _ in range(M):
    d, s = map(int, input().split())
    tmp = []
    while cloud:
        r, c = cloud.pop()
        nr, nc = (r + dr[d] * s) % N, (c + dc[d] * s) % N
        graph[nr][nc] += 1
        tmp.append((nr, nc))
    for r, c in tmp:
        for i in range(1, 5):
            nr, nc = r + dr[2 * i], c + dc[2 * i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc]:
                    graph[r][c] += 1
    for r in range(N):
        for c in range(N):
            if not (r, c) in tmp and graph[r][c] >= 2:
                graph[r][c] -= 2
                cloud.append((r, c))
ans = 0
for lst in graph:
    ans += sum(lst)
print(ans)
