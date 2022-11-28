from collections import deque
import sys


def is_possible(r, c):
    return 0 <= r < H and 0 <= c < W


def bfs():
    visit = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]
    q = deque()
    q.append((0, 0, 0))
    visit[0][0][0] = 0
    while q:
        r, c, cnt = q.popleft()
        if r == H - 1 and c == W - 1:
            return visit[r][c][cnt]
        if cnt < K:
            for d in range(8):
                nr, nc = r + mr[d], c + mc[d]
                if not is_possible(nr, nc):
                    continue
                if arr[nr][nc]:
                    continue
                if visit[nr][nc][cnt + 1] == -1:
                    visit[nr][nc][cnt + 1] = visit[r][c][cnt] + 1
                    q.append((nr, nc, cnt + 1))
            pass
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not is_possible(nr, nc):
                continue
            if arr[nr][nc]:
                continue
            if visit[nr][nc][cnt] == -1:
                visit[nr][nc][cnt] = visit[r][c][cnt] + 1
                q.append((nr, nc, cnt))
    return -1


input = sys.stdin.readline
# 일반 이동
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# 나이트 이동
mr = [-2, -1, 1, 2, 2, 1, -1, -2]
mc = [1, 2, 2, 1, -1, -2, -2, -1]
K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
print(bfs())
