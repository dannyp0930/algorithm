from collections import deque


def solution(maps):
    
    def bfs(sr, sc, er, ec):
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        visit = [[0] * C for _ in range(R)]
        q = deque([(sr, sc)])
        visit[sr][sc] = 1
        while q:
            r, c = q.popleft()
            if r == er and c == ec:
                break
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < R and 0 <= nc < C): continue
                if maps[nr][nc] == "X": continue
                if not visit[nr][nc]:
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr, nc))
        return visit[er][ec] - 1
            
    R = len(maps)
    C = len(maps[0])
    sr = sc = er = ec = lr = lc = 0
    for r in range(R):
        for c in range(C):
            if maps[r][c] == "S":
                sr, sc = r, c
            elif maps[r][c] == "L":
                lr, lc = r, c
            elif maps[r][c] == "E":
                er, ec = r, c
    startToLever = bfs(sr, sc, lr, lc)
    if startToLever == -1:
        return -1
    leverToEnd = bfs(lr, lc, er, ec)
    if leverToEnd == -1:
        return -1
    return startToLever + leverToEnd