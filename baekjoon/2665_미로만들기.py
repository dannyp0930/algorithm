from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
q = deque([(0, 0, 0)])
visit[0][0] = 1
while q:
    r, c, b = q.popleft()
    if r == n - 1 and c == n - 1:
        print(b)
        break
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and not visit[nr][nc]:
            visit[nr][nc] = 1
            if arr[nr][nc]:
                q.appendleft((nr, nc, b))
            else:
                q.append((nr, nc, b + 1))
