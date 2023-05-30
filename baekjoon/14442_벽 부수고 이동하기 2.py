from collections import deque


def bfs():
    q = deque([(0, 0, 0)])
    visit[0][0][0] = 1
    while q:
        r, c, k = q.popleft()
        if r == N - 1 and c == M - 1:
            return visit[r][c][k]
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            dist = visit[r][c][k]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] and k < K and not visit[nr][nc][k + 1]:
                    visit[nr][nc][k + 1] = dist + 1
                    q.append((nr, nc, k + 1))
                elif not arr[nr][nc] and not visit[nr][nc][k]:
                    visit[nr][nc][k] = dist + 1
                    q.append((nr, nc, k))
    ans = min(visit[N - 1][M - 1])
    return -1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N, M, K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visit = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
print(bfs())
