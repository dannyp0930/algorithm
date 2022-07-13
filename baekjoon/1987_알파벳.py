dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def boundary(r, c):
    return 0 <= r < R and 0 <= c < C


def bfs():
    ans = 1
    q = set([(0, 0, board[0][0])])
    while q:
        r, c, alpha = q.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if boundary(nr, nc) and not board[nr][nc] in alpha:
                q.add((nr, nc, alpha + board[nr][nc]))
                ans = max(ans, len(alpha) + 1)
    print(ans)

R, C = map(int, input().split())
board = [input() for _ in range(R)]
bfs()
