from collections import deque


def solution(board):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    R = len(board)
    C = len(board[0])
    sr, sc = -1, -1
    visit = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == "R":
                sr, sc = i, j
                break
        if sr != -1:
            break

    def move(r, c, d):
        while 1:
            r += dr[d]
            c += dc[d]
            if not (0 <= r < R and 0 <= c < C): break
            if board[r][c] == "D": break
        return r - dr[d], c - dc[d]

    q = deque([(sr, sc, 0)])
    while q:
        r, c, s = q.popleft()
        for d in range(4):
            nr, nc = move(r, c, d)
            if visit[nr][nc]: continue
            elif board[nr][nc] == "G":
                return s + 1
            else:
                visit[nr][nc] = 1
                q.append((nr, nc, s + 1))
    return -1
