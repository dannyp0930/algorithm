import sys

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
queue = [(0, 0)]
while queue:
    r, c = queue.pop(0)
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
        if not arr[nr][nc]: continue
        if arr[nr][nc] == 1:
            arr[nr][nc] = arr[r][c] + 1
            queue.append((nr, nc))
print(arr[N - 1][M - 1])
